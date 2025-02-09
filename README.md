# 🤖 AI-Powered News Scraping Agent

An advanced web scraping system leveraging Groq LLM and BeautifulSoup4 for intelligent content extraction and analysis. Built with Streamlit for seamless user interaction and real-time processing.

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
