import scrapy
from pathlib import Path
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import re

class WebCrawler(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['flutter.dev']
    start_urls = ['https://flutter.dev/learn']

    custom_settings = {
        'DEPTH_LIMIT': 2,  # Set maximum depth
        'CLOSESPIDER_PAGECOUNT': 20,  # Set maximum page count
    }
    page_counter = 0
    docs = []
    doc_names = []

    def parse(self, response):
        self.page_counter += 1
        file_name = self.validate_filename(response.url.split("/")[-1]) + '.html'
        self.doc_names.append(file_name)  
        if self.page_counter > self.settings.get('CLOSESPIDER_PAGECOUNT'):
            return
        if response.meta['depth'] > self.settings.get('DEPTH_LIMIT'):
            return
        with open(file_name, "wb") as f:
            f.write(response.body)
        self.log(f"Saved file {file_name}")

        with open(file_name, "rb") as f:
            html_content = f.read().decode('utf-8')
            soup = BeautifulSoup(html_content, 'html.parser')
            text = soup.get_text()
            clean_text = self.cleantext(text)
            self.docs.append(clean_text)

        for next_page in response.css('a::attr(href)').getall():
            yield response.follow(next_page, callback=self.parse)

    def closed(self, reason):
        self.create_index()

    def create_index(self):
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(self.docs)
        cosine_sim_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

        index = {}
        for idx, (doc_name, doc) in enumerate(zip(self.doc_names, self.docs)):
            index[idx] = {
                'document_name': doc_name,
                'document': doc,
                'tfidf_vector': tfidf_matrix[idx],
                'cosine_similarities': cosine_sim_matrix[idx]
            }

        with open('index.pkl', 'wb') as f:
            pickle.dump(index, f)

    def validate_filename(self, filename):
        return re.sub(r'[<>:"/\\|?*]', '_', filename)

    def cleantext(self, text):
        clean_text = re.sub(r'<.*?>', '', text)
        clean_text = re.sub(r'\\[ntr]', '', clean_text)
        clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', clean_text)
        clean_text = re.sub(r'\s+', ' ', clean_text)
        clean_text = clean_text.lower()
        return clean_text