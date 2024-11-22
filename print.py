import streamlit as sl ;

def toprint():
    sl.write("this from moduel")



sl.title("SRU marks")
def mark(t,h):
    return t+h
    
tab1,tab2=sl.tabs(["grading imarks","nfo"])
with tab1:
    col1,col2=sl.columns(2)
    
    with col1:
        t=sl. number_input("TELUGU",value=1)
        h=sl.number_input("hindi",value=1)
        sl.write(t+h)
        
       
  
    with col2:
       sl.write("this is on hold for now")
       sl.write("this second line")
       
    