import streamlit as st
import functions


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

# Show todos list
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)


st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')