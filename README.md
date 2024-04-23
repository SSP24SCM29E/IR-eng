ABSTRACT

This project endeavors to create a robust and efficient web document retrieval system using Python, with a focus on scalability, accuracy, and user-friendliness. The system will consist of three main components: a web crawler, an indexer, and a query processor, leveraging popular libraries such as Scrapy, Scikit-Learn, and Flask.

Development

First, Scrapy will be used to develop the web crawler, which will enable users to start crawling from a seed URL or domain and specify parameters like maximum pages and depth. To increase efficiency, this component will include features for both distributed and concurrent crawling, which will be especially helpful when managing large-scale crawling tasks.
The indexer will then be implemented and an inverted index in pickle format will be created using Scikit-Learn. In order to accurately and quickly represent the content of crawled documents, this index will make use of cosine similarity calculation and TF-IDF scoring. 
The Flask-built query processor will process JSON-formatted user queries and carry out error-checking and validation to guarantee robustness. It will give users pertinent information by returning top-K ranked results based on the indexed documents. 

Objectives

The objectives include developing a scalable web crawler with Scrapy, constructing an efficient indexer using Scikit-Learn for accurate content representation, and creating a user-friendly query processor with Flask. The system aims for robustness through query validation and error-checking, ensuring accurate results. 

OVERVIEW

Solution Outline:

The system employs Scikit-Learn, Flask, and Scrapy for indexing, query processing, and web crawling respectively. It aims for accuracy, scalability, and user-friendliness. Optional features such as query expansion and concurrent crawling enhance its effectiveness. Robustness is ensured through error-checking and query validation. 

Relevant Literature:

Relevant literature encompasses foundational texts like "Introduction to Information Retrieval" by Manning et al., and "Mining the Web: Discovering Knowledge from Hypertext Data" by Soumen Chakrabarti, focusing on web crawling and indexing techniques. Papers on TF-IDF scoring, cosine similarity, and advanced similarity search provide valuable insights into system design.

Proposed System:

The new system will work like a well-organized team, with different parts handling different tasks: 
Scrapy will explore the web, Scikit-Learn will organize what's found, and Flask will help users find what they need. It'll have extra features like doing multiple searches at once and making searches more flexible. We're making sure it's tough by checking and fixing mistakes in searches. And we're making it easy for you to use, taking hints from what users like you find helpful.

DESIGN

System capabilities

1. Web Crawling: With the help of Scrapy, the system will be able to browse the internet and gather web documents.
2. Indexing: The system will effectively arrange and store the gathered web documents for easy retrieval by using Scikit-Learn.
3. Query Processing: By sifting through the indexed documents, Flask enables the system to receive user queries and provide pertinent results.

Interactions

Web Crawling to Indexing: The indexer will organize and store the web documents that the web crawler has collected.
Processing of User Queries: The query processor receives user queries and uses the index to search through the documents to find pertinent results.

Integration

The indexer will receive gathered documents from the web crawler, guaranteeing that newly found content is quickly indexed for later retrieval.
In order to deliver a seamless user experience, the query processor will work with the indexer to retrieve pertinent documents based on user queries.

ARCHITECTURE

Software Components

1. Web crawler, also known as a scrapy, is in charge of searching the internet and gathering web documents.
2. The Scikit-Learn Indexer arranges and saves the gathered web documents for easy access.

3. Query Processor (Flask): This tool takes user queries and searches through the indexed documents to find relevant results.

Interfaces

1. Web Crawling Interface: In order to gather web documents, this interface enables communication between the web crawler and external websites.
2. Indexing Interface: Enables web crawler and indexer communication to arrange and store gathered documents.
3. Query Processing Interface: Provides users with the ability to ask the system questions and obtain pertinent search results.

Implementation

1. Web Crawling: With settings for maximum pages, depth, and seed URLs, Scrapy will be used to crawl the internet.
2. Indexing: TF-IDF scoring and cosine similarity will be used to create an inverted index for effective document retrieval, which will be implemented using Scikit-Learn.
3. QueryProcessing: Flask will be used to process user queries, verify inputs, and provide pertinent search results by looking through the documents that have been indexed.

Operation

Install Python and Install Linux in windows
- `wsl –install`
  
- Install required libraries
- `pip install scrapy`
- `pip install scikit-learn`
- `pip install beautifulsoup4`
- `pip install flask`
- `pip install requests`

Instructions to run the project


Step 1: To run the project go to the spiders folder in the terminal and enter

`Scrapy crawl <file name>`

The TF-IDF scores and cosine similarity for the html documents will be calculated and stored in a index.pkl file

Step 2: To access the index.pkl file go to access pickle folder in terminal and run the python file and the content of the file will be displayed in the terminal.

Step 3: To start the Flask server, go to Flask folder in the terminal and run the Python file in that folder.

Step 4: Now, the flask server is initiated. Open New Terminal and make a request to the flask server with a query in the below format:
`curl -X POST http://localhost:5000/query -H "Content-Type: application/json" -d '{"query": "flutter"}'`

Now, you can see the json format response from the server which encompasses cosine similarity and document name of the top k results.

Conclusion  

To sum up, our project was successful in creating a complete web document retrieval system that included elements for web crawling, indexing, and query processing. The system's accuracy, scalability, and user-friendliness were all met by utilizing Scrapy, Scikit-Learn, and Flask.

Using Scrapy to efficiently crawl the web, we gathered a wide variety of web documents. After that, these documents were arranged and saved using Scikit-Learn's indexing features for easy retrieval. User-friendly query processing was made possible by Flask, allowing users to submit queries and obtain pertinent search results.

Ultimately, the system generated cosine similarity values satisfactorily, giving users insightful information about document similarity. For later use and analysis, these values were saved in a JSON file. 

Testcases/Outputs:

