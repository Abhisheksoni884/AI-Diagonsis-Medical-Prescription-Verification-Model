from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import pytesseract
from PIL import Image

load_dotenv()
pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\tesseract.exe'   #This extensiom is required for using the tesseract 

class functionality :
    
    def extract_text_from_image(image_path):
        """
        This function is used for extract the text from the images by using tesseract
        Attributes : 
            image_path = it consist a path of the image 

        return : cleaned extracted text 
        """
        try:
            text = pytesseract.image_to_string(image_path, lang= 'eng')
            cleaned_text = text.strip()
            return cleaned_text
        
        except Exception as e:
            print(f"Error: {e}")

    # Set up chain for model
    def setup_chain(choice):
        """
        This function is used for set up the chain in which initialised the prompt, define the LLm model for use and created a model chain

        Attributes : 
            choice : Model choice that the end user has selected for retrieving the data from the LLM.

        return : model chain ( Prompt | LLM | String output-parser)
        """
        
        # set the prompting
        prompt_temp = ChatPromptTemplate.from_template("""
        You are a professional doctor. And, your work is to verify the prescription that user will give you and suggest the dosage plan and recommend to either take it or not. The data is sensitive, so be professional and polite. The patient will give the prescription details in text or image format. if some prescription are written wrong then recommend them to not to take it and recommend according to your knowledge.
        But it should must accurate before recommending, according to health problem of patient.
            
        Note : if you are not sure about the recommending a medicine then do not recommend it cause it is topic of patient health. So be professional for that thing.
                                                    
        Instruction : Describe everything deeply.
                                                    
            1. Detect the health problem of the patient by reading the prescription medicines and explain it.                                     
            2. Verify the Prescription medicine names.                                     
            3. if verified then describe about the Medicine that are written in prescription.
                                                    
                - Describe the medicine.
                - Give the Dosage plan of atleast 3 days and it will shown in Tabular form (Mandatory).
                    - example : Dosage Plan (3 Days):

                        Day	Dosage	Frequency	Notes
                        Day 1	500 mg	Every 4-6 hours	Max 4 doses per day
                        Day 2	500 mg	Every 4-6 hours	Max 4 doses per day
                        Day 3	500 mg	Every 4-6 hours	Max 4 doses per day
                                                       
                - Medical insights for diagnosis and treatment.
                - recommendation.
                - Alternatives.                                
                - side effects and their reasons.
                                                    
            4. if are not verified then give the overview about the medicine that the medicine is taken for this health problem not for this.
                                                    
                - Give Alternatives.
                - if you have do not knowledge then just tell the patient that you do not have knowledge about this thing.
                                                    
        Validation : 
                                                    
            1. Data should be so accurate that you are shown, verify it before shown.
            2. Output should be well structured format.
            3. Remove optional AI messages.
               
                                                                                                                                                    
        Questions: {input}""")
        
        # multiple models
        models = {
            "Llama3-70B": "llama3-70b-8192",
            "Llama3-8B": "llama3-8b-8192",
            "Mixtral-8x": "Mixtral-8x7b-32768",
        }

        # load the LLM model
        llm = ChatGroq(model_name = models[choice], temperature = 0.1)

        output_parser = StrOutputParser()

        #create a model chain 
        llm_chain = prompt_temp | llm | output_parser
        return llm_chain


    def generate_response(query, chain_of_llm):
        """
        This function is used for generating response according to user query
        Attributes : 
            query : it has query that user has inserted.
            chain_of_llm = It has a model chain

        return : it will give response according to user query
        """

        #Invoke the retrieval chain 
        response = chain_of_llm.invoke({'input': query})
        return response