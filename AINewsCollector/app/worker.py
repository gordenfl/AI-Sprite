import streamlit as st
from news_fetcher import get_news
from llm_chain import summarize_news



st.title("GORDON AI news general assistant") #设置网页的title

news_item = get_news(int(st.query_params.get("size", 10))) #获取size条, 如果size不存在就是10条
summaries = summarize_news(news_item)

for i, summary in enumerate(summaries):
    st.subheader(f"News {i+1}: " + summary[0])
    st.write(summary[1])
