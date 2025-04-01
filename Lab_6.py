
import streamlit as st
from transformers import pipeline
def main():
  st.title("Hugging Face Model Demo")
  input_text=st.text_input("Enter your text","")
  model=pipeline("sentiment-analysis",model="distibert-base-uncased-finetuned-sst-2-english")
  if st.button("Analyze"):
    result=model(input_text)
    st.write("Prediction :",rsult[0]['label'],"|score:",result[0]['score'])
  if __name__==" __main__":
   main()
