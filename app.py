import streamlit as st

club_info = {
    "name": "Campus Rescue Station",
    "day": "Monday - Friday",
    "time": "10:00 AM - 4:00 PM",
    "location": "Campus Library Desk"
}

activities = [
    "Borrow a phone charger",
    "Borrow an umbrella",
    "Borrow a calculator",
    "Borrow a notebook"
]

st.title(club_info["name"])
st.caption("A fictional CIS 211 course project. These are not real campus arrangements.")


st.header("About Our Service")

# This section explains the purpose of the service.
st.markdown("""
**Campus Rescue Station** is a fictional campus service where students can borrow useful items they forgot at home. We offer things like phone chargers and calculators to help students during their school day. *Our goal is to make college life a little easier.*
""")

st.header("What You Can Borrow")

# This loop displays every item from the activities list.
for item in activities:
    st.write("•", item)

st.header("Service Details")

# These details come from the club_info dictionary.
st.write("Days:", club_info["day"])
st.write("Hours:", club_info["time"])
st.write("Location:", club_info["location"])

st.header("Before You Visit")

# These steps explain how students can use the service.
st.markdown("""
- Bring your student ID.
- Ask the staff if the item you need is available.
- Return borrowed items before the desk closes.

For more campus information, visit the [Medgar Evers College website](https://www.mec.cuny.edu/).
""")
