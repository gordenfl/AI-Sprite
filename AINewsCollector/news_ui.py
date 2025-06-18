import streamlit as st
from news_fetcher import get_news
from llm_chain import summarize_news



st.title("AI news general assistant")

news_item = get_news()
summaries = summarize_news(news_item)

for i, summary in enumerate(summaries):
    st.subheader(f"News {i+1}: " + summary[0])
    st.write(summary[1])