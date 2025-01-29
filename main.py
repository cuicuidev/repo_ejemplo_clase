import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def read_csv(path):
    return pd.read_csv(path, encoding="utf-8")

def plot_df(df, col):
    sns.histplot(df, x=col)
    plt.show()

def main():
    st.dataframe(sns.load_dataset("iris"))

if __name__ == "__main__":
    main()