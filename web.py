import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo_to_add = st.session_state['point'] + "\n"
    todos.append(todo_to_add)
    functions.write_todos(todos)


st.title("L1 support checklist")
st.write("Points to follow through the shift")



for index, list_todo in enumerate(todos):
    checkbox = st.checkbox(list_todo, key=list_todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[list_todo]
        st.experimental_rerun()


st.text_input("", placeholder="Add a point",
              on_change=add_todo, key="point")


