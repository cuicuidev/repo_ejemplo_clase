import streamlit as st
import seaborn as sns

def main():
    st.dataframe(sns.load_dataset("iris"))

if __name__ == "__main__":
    main()