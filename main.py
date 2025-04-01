import streamlit as st
import toml
from langchain_groq import ChatGroq
from langchain_core.prompts import  ChatPromptTemplate


from dotenv import load_dotenv # loading keys
# load_dotenv()
# Load the config file
config = toml.load("config.toml")

# Access the API key
api_key = config["api"]["key"]
print(api_key)

st.markdown(
    "<h1 style =' color: Green'> Collabry Translation Model </h1>",
    unsafe_allow_html=True
)

# Add a backgorund 
st.markdown(
    """
    <style>
    body {
        background-color: lightblue;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.divider()


st.markdown("<h2 style = 'color:Green'> Translate text to any language </h2>", unsafe_allow_html=True)

language_to_translate = st.selectbox(
    label="Language to translate to",
    options= ["English", "Arabic", "Spanish", "Frensh", "Hindi", "Japanese"]

)

text_to_translate = st.text_area("Paste text here:")

button = st.button("Translate")



# intitalize models 

#models 
groq =  ChatGroq(model="llama-3.3-70b-versatile")

# result =  groq.invoke("What is the most spoken language?")
# st.write(result.content)

# chat prompt templete 
templete =  ChatPromptTemplate.from_messages(
    [("system", "You are a professional translator. Your task is to translate the following texts to {language} return only translated text not any adding or info")
     , ("user", "{text}")]
)

# st.write(templete)

prompt = templete.invoke({
    "language":  language_to_translate,
    "text" : text_to_translate
})

st.write(prompt)

# invoke texts to pompt
# result = groq.invoke(prompt)

# st.write(result)

if button and text_to_translate.strip() != "":
    place_holder = st.empty()

    with st.spinner("Translating...."):
    #create an empty container to get response 
        place_holder.text(groq.invoke(prompt).content)
elif button:
    st.error("Please Provide Text to translate!")
