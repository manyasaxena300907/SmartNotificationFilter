"""app.py - Streamlit interface (Day 7).

Run with:  streamlit run app.py
"""
import streamlit as st

# from src.predict import predict_message
# from src.history import save_to_history, load_history

st.set_page_config(page_title="Smart Notification Filter")
st.title("Smart Notification Filter")
st.write("Paste a message and check whether it is important.")

message = st.text_area("Message")

if st.button("Classify"):
    if not message.strip():
        st.warning("Please type or paste a message first.")
    else:
        # TODO (Day 7):
        # 1. label = predict_message(message)
        # 2. if label == 1: st.error("IMPORTANT: ...")
        # 3. else: save_to_history(message); st.info("Saved to history.")
        st.write("Prediction will appear here.")

st.subheader("History (not important messages)")
# TODO (Day 7): st.dataframe(load_history())
