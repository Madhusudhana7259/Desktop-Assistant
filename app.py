from src.helper import voice_input,text_to_speech,llm_model_object
import streamlit as st

def main():
    st.title("Desktop assistant")

    if st.button("Ask Me anything"):
        with st.spinner("Listining..."):
            text = voice_input()
            spe = llm_model_object(text)
            text_to_speech(spe)

            audio_file = open("speech.mp3", 'rb')
            audio_bytes = audio_file.read()
            
            st.text_area(label="Response:", value=spe, height=350)
            st.audio(audio_bytes, format='audio/mp3')
            st.download_button(label="Download Speech",
                                data=audio_bytes,
                                file_name="speech.mp3",
                                mime="audio/mp3")




if __name__=="__main__":
    main()

