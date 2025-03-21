# import libraries
import  streamlit as st
from classes import functionality
from PIL import Image

if __name__ == "__main__" :

    # Set up Streamlit UI 
    st.markdown("""
    <style>
        .stApp {
        background: url("https://img.freepik.com/free-photo/health-still-life-with-copy-space_23-2148854031.jpg?t=st=1741592237~exp=1741595837~hmac=eaa9c74bc644d12e86ff4a0c148bbf4895f2685e3989eb959885300bc.5f209f6&w=1800");
        background-size: cover;
        color: black;
        }
        .stButton {
        color : black;
        }
        .stSidebar{
        background-color : black;
        color : white;
        } 
        .stTextInput input::placeholder {
            color: black;
        } 
    </style>""", unsafe_allow_html=True)

    st.title("AI Diagonsis Model for prescription Verification ")
    st.markdown("## Hey, How can i help you?")
    st.sidebar.title("Select the LLM model")
    st.session_state.choice = st.sidebar.selectbox("",["Llama3-70B","Llama3-8B","Mixtral-8x"])

    st.sidebar.write("About")
    st.sidebar.write(""" 
    A dual-purpose AI chatbot that assists both patients in identifying potential health conditions, based on prescription (image) llm extracts medicine names and explains their usage, dosage, and alternatives, and help doctors in retrieving real-time medical insights for diagnosis and treatment.
    """)
    
    st.session_state.chain = functionality.setup_chain(st.session_state.choice)
    st.session_state.uploaded_file = st.file_uploader("Choose a your file", type = ["pdf","jpg","jpeg","png"])
    st.session_state.user_input = st.text_input("",placeholder= "Enter your prescription here")

    if st.button("Generate Response"): 
        if st.session_state.user_input :
            st.session_state.response = functionality.generate_response(st.session_state.user_input, st.session_state.chain)        
            #get the response from the LLM
            st.write(f"Chatbot : {st.session_state.response}")

        elif st.session_state.uploaded_file: 
            try : 
                image = Image.open(st.session_state.uploaded_file)
                extracted_text = functionality.extract_text_from_image(image)
                if extracted_text :
                    st.write("Extracted text from the image: \n\n", extracted_text)
                    # Use the extracted text to generate a response
                    st.session_state.response = functionality.generate_response(extracted_text, st.session_state.chain)
                    st.write(f"{st.session_state.response}")
                else :
                    st.write("Prescription details are not cleared")
            except Exception as e :
                st.write(f"Error : {e}")

        else :
            st.write("Please first enter the prescription details or upload the image.")





