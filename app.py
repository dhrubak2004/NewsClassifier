import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

app = Flask(__name__)
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(temperature=0, model="llama-3.3-70b-versatile")

prompt = ChatPromptTemplate.from_template("""
You are a news article classifier. Classify the following news article into ONE of these categories:
- Politics
- Technology
- Sports
- Business
- Entertainment
- Health
- Science
- World
- Environment
- Crime

Also provide:
1. Confidence level (High/Medium/Low)
2. A one line reason for the classification
3. Top 3 keywords from the article

Respond in this exact format:
Category: <category>
Confidence: <confidence>
Reason: <reason>
Keywords: <keyword1>, <keyword2>, <keyword3>

Article:
{article}
""")

chain = prompt | model | StrOutputParser()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()
    article = data.get("article", "").strip()
    
    if not article:
        return jsonify({"error": "No article provided"}), 400
    
    if len(article) < 20:
        return jsonify({"error": "Article too short"}), 400

    try:
        result = chain.invoke({"article": article})
        
        lines = result.strip().split('\n')
        parsed = {}
        for line in lines:
            if line.startswith("Category:"):
                parsed["category"] = line.replace("Category:", "").strip()
            elif line.startswith("Confidence:"):
                parsed["confidence"] = line.replace("Confidence:", "").strip()
            elif line.startswith("Reason:"):
                parsed["reason"] = line.replace("Reason:", "").strip()
            elif line.startswith("Keywords:"):
                parsed["keywords"] = line.replace("Keywords:", "").strip().split(", ")

        return jsonify(parsed)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)