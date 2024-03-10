import streamlit as st
import functions

tasks = functions.getTasks()


def addTask():
    task = st.session_state["newTask"] + "\n"
    if len(task) < 3:
        st.warning("Task length needs to be a minimum of 3")
    elif task in tasks:
        st.warning("Item already in the list.")
    else:
        tasks.append(task.title())
        functions.writeTasks(tasks)


st.title("To Do App")
st.subheader("Tasks List:")

for index, task in enumerate(tasks):
    if len(task) < 2:
        pass
    else:
        checkbox = st.checkbox(task.title(), key=task)
        if checkbox:
            tasks.pop(index)
            functions.writeTasks(tasks)
            del st.session_state[task]
            st.rerun()


st.text_input(label="Enter a task:",
              placeholder="Add new task...",
              on_change=addTask, key="newTask")
