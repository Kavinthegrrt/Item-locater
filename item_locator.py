import streamlit as st

# Initialize session state for stored items
if "items" not in st.session_state:
    st.session_state["items"] = {}

# App title
st.title("Item Locator")

# Adding a new item
st.header("Add an Item")
item_name = st.text_input("Item Name", placeholder="e.g., Wallet")
item_location = st.text_input("Location", placeholder="e.g., In the top drawer")
item_description = st.text_area("Description", placeholder="e.g., A brown leather wallet with some cash inside")

if st.button("Save Item"):
    if item_name and item_location:
        st.session_state["items"][item_name] = {
            "location": item_location,
            "description": item_description,
        }
        st.success(f"'{item_name}' has been saved!")
    else:
        st.error("Please provide both the item name and location.")

# Finding a lost item
st.header("Find a Lost Item")
if st.session_state["items"]:
    selected_item = st.selectbox("Select the item you've lost", st.session_state["items"].keys())

    if st.button("Find Item"):
        item_details = st.session_state["items"][selected_item]
        st.write(f"**Location:** {item_details['location']}")
        st.write(f"**Description:** {item_details['description']}")
else:
    st.write("No items have been added yet.")

# Display all stored items
st.header("All Stored Items")
if st.session_state["items"]:
    for item, details in st.session_state["items"].items():
        st.write(f"- **{item}**: Located at **{details['location']}**")
else:
    st.write("No items to display.")


