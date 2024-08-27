import streamlit as st
import psycopg2
import pandas as pd

# Set up authentication
def authenticate(username, password):
    # Replace this with your actual authentication logic
    return username == "admin" and password == "password"

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname='votes_e29f',
    user='votes_e29f_user',
    password='OyKZT8cTOkwF0EdmVmxSg2Zu5tGBj8O6',
    host='dpg-cr6p3pd6l47c7397q0qg-a',
    port='5432'
)
cursor = conn.cursor()

# Authentication
st.sidebar.title("Login")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if authenticate(username, password):
    st.title("Vote Counts")

    # Query the database to get the vote counts
    for position in ["President", "Secretary", "Vice President", "Assistant Secretary"]:
        st.subheader(f"Votes for {position}")
        query = "SELECT candidate, COUNT(*) as count FROM votes WHERE position = %s GROUP BY candidate"
        cursor.execute(query, (position,))
        df = pd.DataFrame(cursor.fetchall(), columns=["Candidate", "Count"])

        # Display the vote counts in a table
        st.table(df)
else:
    st.error("Invalid username or password")

conn.close()
