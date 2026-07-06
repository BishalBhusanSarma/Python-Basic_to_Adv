import streamlit as st
import requests


Base_url = "https://task-api-3x27.onrender.com"


st.title("Task App")
st.divider()

with st.container(border=True):
#+++++++++++++++++++++++++++++++


 # to add tasks


    st.header("Add Task")
    with st.container(border=True):
        new_task = st.text_input("Enter your task")
        status = st.radio("Completed?", [0,1], format_func=lambda x: "Yes" if x==1 else "No", key="status")

        if st.button("Add task"):
            data = { "task": new_task, "status": status}

            response = requests.post(f"{Base_url}/add-task", json=data)
            with st.container(border=True):
                st.write(response.json()["message"])


    st.divider()
    #+++++++++++++++++++++++++++++++++++



    # to search tasks 
    st.header("Search Task")
    with st.container(border=True):
        s_id = st.text_input("Input id", key="s_inp")
        if st.button("Search task", key="s_btn"):
            response_s = requests.get(f"{Base_url}/by_task_id/{s_id}").json()
            if "message" in response_s:
                st.write(response_s["message"])
            else:
                st.write(f"ID is: {response_s[0]}")
                st.write(f"Task is: {response_s[1]}")
                st.write(f"status is Completed?: {"Yes" if response_s[2]==1 else "No"}")
            




    #+++++++++++++++++++++++++++++++++++



    # to edit tasks 

    st.header("Edit Task")
    with st.container(border=True):

        u_id = st.text_input("Input id", key="u_id")
        u_task = st.text_input("Enter updated task", key="u_task")
        u_status = st.radio("Completed?", [0,1], format_func=lambda x: "Yes" if x==1 else "No", key="u_status")
        if st.button("Update task", key="u_btn"):

            data = {"task": u_task, "status":u_status}
            response = requests.put(f"{Base_url}/update/{u_id}", json=data)
            with st.container(border=True):
                st.write(response.json()["message"])



    st.divider()
    #+++++++++++++++++++++++++++++++++++


    # to delete tasks

    st.header("Delete Task")
    with st.container(border=True):
        d_id = st.text_input("Enter task ID to delete")
        if st.button("Delete Task"):
            response_d = requests.delete(f"{Base_url}/delete/{d_id}")
            with st.container(border=True):
                    st.write(response_d.json()["message"])


st.divider()
#+++++++++++++++++++++++++++++++++++


# to Show tasks

st.header("Show Tasks")
with st.container(border=True):

    response_s = requests.get(f"{Base_url}/")


    task = response_s.json()
    if isinstance(task, dict):
        st.write(task["message"])
    else:
        for t in task:
            with st.container(border=True):
                with st.container(border=True):
                    st.write(f"Id: {t[0]}")

                st.write(f"Task: {t[1]}")
                
                st.write(f"Completed?: {"Yes" if t[2]==1 else "No"}")
            
                

