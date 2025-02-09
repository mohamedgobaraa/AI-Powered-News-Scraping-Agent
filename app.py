import streamlit as st
from groq import Groq
import requests
from bs4 import BeautifulSoup
import json

st.title("News Scraping AI Agent 🕵️‍♂️")
st.caption("This app allows you to scrape a website using Groq LLM")

GROQ_API_KEY = "YOUR_API_KEY"

client = Groq(api_key=GROQ_API_KEY)

def scrape_website(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for script in soup(["script", "style"]):
            script.decompose()
            
        text = soup.get_text(separator=' ', strip=True)
        
        return text
    except Exception as e:
        raise Exception(f"Failed to scrape website: {str(e)}")

def analyze_with_groq(text, prompt):
    try:
        system_prompt = """
        You are an advanced web scraping and data extraction assistant. Your role is to:

1. Extract structured data from any provided HTML, text, or web content
2. Support modern scraping techniques including:
   - Dynamic content handling
   - JavaScript rendering
   - Rate limiting and polite scraping
   - Cookie and session management
   - Proxy rotation
   - Browser fingerprint randomization
   - Captcha handling

RESPONSE FORMAT:
- All responses must be valid JSON objects
- Include metadata fields:
  - timestamp
  - source_url
  - scraping_method
  - success_status
- Structure extracted data in nested JSON as needed
- Handle errors gracefully with error codes and messages
- Support pagination and incremental scraping
- Include data validation results

GUIDELINES:
- Respect robots.txt and site policies
- Implement appropriate delays between requests
- Handle anti-bot measures appropriately
- Cache results when possible
- Monitor for changes in site structure
- Validate output schema
- Clean and normalize extracted data
- Support multiple output formats if requested

The response will be in the user's language and contain only the JSON structure without additional commentary.

Never forget any "," while writing the json file 

"""

        user_message = f"""Based on this text from the website:

{text[:8000]}...

User's request: {prompt}

Return ONLY a JSON object with the extracted information. Ensure the response is valid JSON."""

        completion = client.chat.completions.create(
            model="deepseek-r1-distill-llama-70b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.1,
            max_tokens=1000
        )
        
        response_text = completion.choices[0].message.content.strip()
        
        try:
            return json.loads(response_text)
        except json.JSONDecodeError:
            start = response_text.find('{')
            end = response_text.rfind('}') + 1
            if start != -1 and end != 0:
                cleaned_json = response_text[start:end]
                return json.loads(cleaned_json)
            else:
                raise Exception("Could not extract valid JSON from response")
            
    except Exception as e:
        raise Exception(f"Failed to analyze content: {str(e)}")

col1, col2 = st.columns(2)

with col1:
    url = st.text_input("Enter the URL of the website you want to scrape")

with col2:
    user_prompt = st.text_input("What do you want the AI agent to extract from the website?")

if st.button("Analyze Website"):
    if not url or not user_prompt:
        st.error("Please provide both a URL and a prompt.")
    else:
        try:
            with st.spinner("Scraping website..."):
                content = scrape_website(url)
                st.info("Website scraped successfully!")
                
                st.info("Analyzing content...")
                result = analyze_with_groq(content, user_prompt)
                
                st.success("Analysis completed successfully!")
                
                with st.expander("View Results", expanded=True):
                    st.json(result)
                
                st.download_button(
                    label="Download Results as JSON",
                    data=json.dumps(result, indent=2),
                    file_name="analysis_results.json",
                    mime="application/json"
                )
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.error("Please check your URL and try again.")