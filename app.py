import streamlit as st
from multiapp import MultiApp

app = MultiApp()

# Add all your application here
app.add_app("Hey", form.app)

# The main app
app.run()
