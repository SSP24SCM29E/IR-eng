import os
import pickle
from flask import Flask, jsonify, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the pre-built document search index
index_file_path = os.path.join(os.path.dirname(__file__), '..', 'spiders', 'index.pkl')
with open(index_file_path, 'rb') as f:
    search_index = pickle.load(f)

# Create a tool for converting text to numerical features
text_to_feature_converter = TfidfVectorizer()

# Preprocess document text from the index and create a feature matrix
document_features = text_to_feature_converter.fit_transform([doc['document'] for doc in search_index.values()])

# Create a Flask web application instance
app = Flask(__name__)

# Route for the root URL
@app.route('/', methods=['GET'])
def get_cosine_similarity():
    user_query = request.args.get('query', 'flutter')
    print("User query:", user_query)  # Add this line
    if not user_query:
        return jsonify({'error': 'No query provided'})
    user_query_features = text_to_feature_converter.transform([user_query])
    print("User query features:", user_query_features)  # Add this line
    similarity_scores = cosine_similarity(user_query_features, document_features).flatten()
    print("Similarity scores:", similarity_scores)  # Add this line
    number_of_results = min(10, len(similarity_scores))
    top_documents = similarity_scores.argsort()[-number_of_results:][::-1]
    search_results = []
    for document_index in top_documents:
        document = search_index[document_index]
        search_results.append({
            'similarity_score': similarity_scores[document_index],
            'document_name': document['document_name'],
            'document_snippet': document['document'][:100]
            
        })
    return jsonify(search_results)


# Run the web application
if __name__ == '__main__':
    app.run(debug=True)