import streamlit as st
from multiapp import MultiApp

app = MultiApp()

# Add all your application here
app.add_app("Fill a form", form.app)
app.add_app("For future features", feature.app)

# The main app
app.run()
