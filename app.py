import streamlit as st

# Define a simple set of credentials
USER_CREDENTIALS = {
    "username": "user1",
    "password": "password123"
}

def login():
    st.title("Arealstatistikk 2.0")
    # Input fields for username and password
    username = st.text_input("Brukernavn")
    password = st.text_input("Passord", type="password")
    
    if st.button("Logg inn"):
        if username == USER_CREDENTIALS["username"] and password == USER_CREDENTIALS["password"]:
            st.session_state.logged_in = True
            st.rerun()
            st.success("Innlogget.")
        else:
            st.error("Ugyldig brukernavn eller passord.")

def protected_page():
    # Set up the main page
    st.set_page_config(layout="wide")

    st.markdown(
    """
    <style>
    .reportview-container .main .block-container {
        padding: 0;
    }
    .center {
        display: center;
        justify-content: center;
        align-items: center;
        height: 100vh; /* Optional: centers vertically in viewport */
    }
    </style>
    """,
    unsafe_allow_html=True,
    )
    # Embed your Power BI report here
    powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiZDE4MzA4MjAtZmQ3Ny00NjE5LTg3MTQtMzQ2Y2ExMmU2NDMyIiwidCI6ImMxNjZiOWM0LTUwNTMtNGVlYy05NjY1LWFiYTA3ODJkMDgwNCIsImMiOjh9"

    # This sets the width and height of the iframe
    st.components.v1.html(f"""
        <iframe width="900" height="600" src="{powerbi_url}" frameborder="0" allowfullscreen="true"></iframe>
    """, height=600)

    # Example of adding additional components to a protected page
    if st.button("Logg ut"):
        st.session_state.logged_in = False
        st.success("Logget ut.")
        st.rerun()  # Reload to show the login page again

def main():
    # Initialize session state for login status
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        login()
    else:
        protected_page()

if __name__ == "__main__":
    main()




