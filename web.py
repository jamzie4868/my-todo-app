import streamlit as st
import functions

existing_todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    existing_todos.append(todo)
    functions.write_todos(existing_todos)



st.title("My Todo App")

for index, todo in enumerate(existing_todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        existing_todos.pop(index)
        functions.write_todos(existing_todos)
        del st.session_state[todo]
        st._rerun()

st.text_input(label="", placeholder="Enter a todo:",
              on_change=add_todo, key="new_todo")

