# 🤖 AI-Powered News Scraping Agent

An advanced web scraping system leveraging Groq LLM and BeautifulSoup4 for intelligent content extraction and analysis. Built with Streamlit for seamless user interaction and real-time processing.

## 👥 Author & Contact
- **Created by**: Mohammad Gobara
- **LinkedIn**: [Mohammad Gobara](https://www.linkedin.com/in/mohamed-gobara/)
- **GitHub**: [@mohamedgobaraa](https://github.com/mohamedgobaraa)

## 🌟 Key Features

- **AI-Powered Analysis**: Integration with Groq LLM for context-aware data extraction
- **Intelligent Parsing**: Advanced HTML structure recognition
- **Dynamic Content Handling**: Supports JavaScript-rendered content
- **Structured Output**: Clean JSON formatting with nested hierarchies
- **Real-time Processing**: Immediate feedback and visualization

## 📦 Requirements

```txt
streamlit>=1.42.0
groq>=0.18.0
beautifulsoup4>=4.13.3
requests>=2.32.3
python-dotenv>=1.0.1

etc ...
```

## 🛠️ Installation

### Option 1: Using pip (Recommended for most users)

1. **Create a virtual environment**:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

### Option 2: Using Conda (Recommended for data scientists)

1. **Create and activate conda environment**:
```bash
# Create environment
conda create -n llm_scraper python=3.10.11

# Activate environment
conda activate llm_scraper

# Install requirements
conda install pip
pip install -r requirements.txt
```

## 🚀 Running the Application

After installation, follow these steps to run the application:

1. **Ensure your environment is activated**:
```bash
# If using conda
conda activate llm_scraper

# If using venv (Windows)
.\venv\Scripts\activate

# If using venv (Linux/Mac)
source venv/bin/activate
```

2. **Run the Streamlit app**:
```bash
streamlit run app.py
```

3. **Access the application**:
- The app will automatically open in your default web browser
- If not, navigate to the URL shown in the terminal (typically http://localhost:8501)


