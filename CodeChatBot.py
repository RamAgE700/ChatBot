import streamlit as st
import requests

# Set your Gemini API key here
API_KEY = 'AIzaSyAlkMqarUExaxDatDQ0t-1udhy9H7vrzLM'  # Replace with your actual API key
API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent'  # Updated correct endpoint

def generate_code_explanation(code_snippet):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'contents': [{
            'parts': [{
                'text': f"Explain the following code: \n\n{code_snippet}"
            }]
        }]
    }
    
    # Include the API key in the URL
    response = requests.post(f"{API_URL}?key={API_KEY}", headers=headers, json=data)
    
    # Print the full response for debugging
    print("Response Status Code:", response.status_code)
    print("Response Body:", response.json())  # Print the entire response body

    if response.status_code == 200:
        response_data = response.json()
        # Adjust according to the actual response structure
        if 'candidates' in response_data and len(response_data['candidates']) > 0:
            return response_data['candidates'][0]['content']['parts'][0]['text']
        else:
            return 'No candidates found in response.'
    else:
        return f"Error: {response.status_code} - {response.text}"

def main():
    st.title("Code Explanation Chatbot")
    st.write("Enter the code snippet you need explained below:")
    
    code_snippet = st.text_area("Code Snippet", "")
    
    if st.button("Generate Explanation"):
        if code_snippet:
            with st.spinner("Generating explanation..."):
                explanation = generate_code_explanation(code_snippet)
                st.success("Explanation generated successfully!")
                st.write(explanation)
        else:
            st.warning("Please enter a code snippet.")

if __name__ == "__main__":
    main()