import streamlit as st
import random

# Initialize lists
names = ['Nick', 'Willow', 'Jake', 'Sydney', 'Timmy', 'Christina', 'Brennan']
assignee = ['Nick', 'Willow', 'Jake', 'Sydney', 'Timmy', 'Christina', 'Brennan']

# Function to generate assignments with constraints
def assign_without_conflicts(names, assignee):
    while True:
        shuffled_names = names[:]
        random.shuffle(shuffled_names)
        if all(
            name != assignee and
            not (name == 'Sydney' and assignee == 'Jake') and
            not (name == 'Jake' and assignee == 'Sydney') and
            not (name == 'Nick' and assignee == 'Willow') and
            not (name == 'Willow' and assignee == 'Nick') and
            not (name == 'Christina' and assignee == 'Brennan') and
            not (name == 'Brennan' and assignee == 'Willow')
            for name, assignee in zip(shuffled_names, assignee)
        ):
            return dict(zip(assignee, shuffled_names))

# Streamlit UI
st.title("Secret Santa Picker")

# Button to generate assignments
if 'assignments' not in st.session_state:
    st.session_state.assignments = None

if st.button("Generate Assignments"):
    st.session_state.assignments = assign_without_conflicts(names, assignee)
    st.success("Assignments generated!")

# Check if assignments have been generated
if st.session_state.assignments:
    st.write("Assignments are ready! Select a name to see their assigned name or view all.")

    # Dropdown to select a name with blank and "ALL" option
    selected_name = st.selectbox("Select a name:", options=[""] + ["ALL"] + names, format_func=lambda x: "Select an option" if x == "" else x)

    # Handle dropdown selection
    if selected_name == "ALL":
        st.write("### All Assignments:")
        for key, value in st.session_state.assignments.items():
            st.write(f"**{key}** is assigned to **{value}**.")
    elif selected_name and selected_name != "":
        st.write(f"**{selected_name}** is assigned to **{st.session_state.assignments[selected_name]}**.")
else:
    st.warning("Click the 'Generate Assignments' button to start.")

# To display an image
st.image("/Users/NickThomas 1/git/PythonProjects/christmasSecretSanta/santa.jpg", width=300)
