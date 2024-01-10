import streamlit as st
import openai
import langchain
from dotenv import load_dotenv
import os
from langchain_community.document_loaders import PyPDFLoader
from PyPDF2 import PdfReader
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import OpenAI


def main():
    
    # load api_key
    if not load_dotenv():
        print("Could not load .env file or it is empty. Please check if it exists and is readable.")
        exit(1)
    
    # page style
    st.set_page_config(
        page_title="Quizzer❔",
        page_icon="❔" 
    )
    
    st.header('Quizzer❔')
    
    noq = st.selectbox(
        "Number of questions for your quiz:",
        key='number_of_questions',
        options=["5", "10", "15", "20", "25", "30"]
    )
    
    pdf = st.file_uploader("Upload your PDF", type="pdf")
    cancel_button = st.button('Cancel')
    
    
    if cancel_button:
        st.stop()
        
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        pdf_text = ""                       # Initialize a string to accumulate extracted text
        for page in pdf_reader.pages:       # Loop through each page in the PDF
            pdf_text += page.extract_text() 
        
        # st.write(pdf_text)
        
        # Quizzing
        api_key = os.getenv("OPENAI_API_KEY")
        llm = OpenAI(openai_api_key=api_key)
        
        prompt_template = PromptTemplate.from_template(
            '''Provide {noq} questions and answers for each questions from this text: 
            {pdf_file}'''
        )
        
        quiz_prompt = prompt_template.format(noq=noq, pdf_file=pdf_text)
        llm_chain = LLMChain(prompt=quiz_prompt, llm=llm)
        questions = llm_chain.run()
        st.write(questions)
    


if __name__ == '__main__':
    main()