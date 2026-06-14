# 📰 News Classifier

An AI-powered news article classification web app built with Flask and Groq's LLaMA 3.3 70B model.

![News Classifier](https://newsclassifier-759q.onrender.com)

---

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
4. [Usage](#usage)
5. [Supported Categories](#supported-categories)
6. [Live Demo](#live-demo)

---

## Features
- Paste any news article and get instant AI-powered classification
- Identifies category with confidence level (High/Medium/Low)
- Provides a one-line reason for classification
- Extracts top 3 keywords from the article
- Clean dark-themed UI

---

## Technologies Used
- **Flask** — Web framework
- **Groq LLaMA 3.3 70B** — AI classification model (free tier)
- **LangChain** — LLM orchestration
- **Docker** — Containerized deployment
- **Gunicorn** — Production WSGI server

---

## Supported Categories
| Category | Example Topics |
|---|---|
| Politics | Elections, Government, Policy |
| Technology | AI, Software, Gadgets |
| Sports | Football, Cricket, Olympics |
| Business | Markets, Economy, Startups |
| Entertainment | Movies, Music, Celebrity |
| Health | Medicine, Fitness, Nutrition |
| Science | Research, Space, Discovery |
| World | International News, Diplomacy |
| Environment | Climate, Nature, Conservation |
| Crime | Law, Justice, Security |

---

## Setup Instructions

### Prerequisites
- Python 3.11+
- Groq API key (free at [console.groq.com](https://console.groq.com))

### Local Installation

1. Clone the repository:
```bash
   git clone https://github.com/dhrubak2004/NewsClassifier.git
   cd NewsClassifier
```

2. Install dependencies:
```bash
   pip install -r requirements.txt
```

3. Create a `.env` file:
```env
   GROQ_API_KEY=your_groq_api_key
```

4. Run the app:
```bash
   python app.py
```

5. Open [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Usage
1. Paste any news article into the text box
2. Click **"Classify Article"**
3. View the result:
   - **Category** — the news topic
   - **Confidence** — High / Medium / Low
   - **Reason** — why it was classified that way
   - **Keywords** — top 3 keywords from the article

---

## Live Demo
🔗 [https://newsclassifier-759q.onrender.com](https://newsclassifier-759q.onrender.com)

---

## Future Improvements
- Add support for URL input (auto-fetch article from link)
- Multi-language classification
- Batch classification of multiple articles
- Export results as CSV

---

## License
This project is licensed under the MIT License.
