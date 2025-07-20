from dotenv import load_dotenv

load_dotenv()
import os
import re
import sqlite3

import google.generativeai as genai
import streamlit as st

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel(model_name='gemini-1.5-flash')
    response=model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()


    return rows


def clean_sql(sql_text):
    return re.sub(r"```(?:sql)?", "", sql_text).strip()

prompt =[ '''You are an expert SQL query generator.

Given a natural language question and a table schema, generate the correct SQL query that answers the question. 
The input can be phrased in any way — you must understand the intent and generate the correct query.
Do not include any explanation or formatting — return only the SQL query.

Here is an example to guide the format (not all inputs will follow this pattern exactly):

Schema:
Table: students
Columns: name, class, section, marks

Example:
Input: Show names and marks of students who scored more than 90.
Output: SELECT name, marks FROM students WHERE marks > 90;

Now respond to this input:
'''
]


st.set_page_config(page_title='I can retrieve any sql query')
st.header('Gemini App to retrieve SQL data')

question=st.text_input('input:',key='input')

submit=st.button('Ask the Question')

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    cleaned_sql = clean_sql(response)
    print("sql query after cleaning is,",clean_sql)
    data=read_sql_query(cleaned_sql,"students.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)

