import streamlit as st
import main
import pandas as pd
st.title("Notes App")

# add notes
st.subheader("Add Notes")
col1, col2 = st.columns(2)
with col1:
#     id = st.text_input("Enter id")
# with col2:
    task = st.text_input("Enter task")
with col2:
    desc = st.text_input("Enter description")
with col2:
    if st.button("Add note"):
        
        result = main.post_add_notes(task, desc)
        st.success(result["message"])




colo1, colo2= st.columns([2,1])
with colo1:
    
    st.subheader("Update Notes")
    colu1, colu2, colu3 = st.columns(3)
    with colu1:
        id_u = st.text_input("Enter id for update")
    with colu2:
        task_u = st.text_input("Enter task for update")
    with colu3:
        desc_u = st.text_input("Description for update")
    with colu2:
        if st.button("Update"):
            result = main.post_update(id_u,task_u, desc_u)
            st.success(result["message"])


with colo2:
# Delete section
    st.subheader("Delete Note")

    note_id = st.text_input("Enter Note ID")
    if st.button("Delete"):

        if note_id:

            result = main.delete_notes_by_id(note_id)

            st.success(result["message"])


#update





# Show all notes
try:
    st.subheader("All notes")

    updated_notes = main.get_all()


    df = pd.DataFrame(updated_notes).sort_values(by="ID", ascending=True)

    st.dataframe(df, hide_index=True)
except:
    st.text("No notes found")
