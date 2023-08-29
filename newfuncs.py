import streamlit as st
import time

def wait(second: int):
	time.sleep(second)
	
if st.toggle("Grand Prize Opertunety"):
	with st.status(label="parsing", expanded=True, state="running") as status:
		st.write("**Parsing...**")
		wait(3)
		st.write("**Parsing Done!**")
		wait(3)
		st.write("**Gifted!**")
		status.update(label="completed!", expanded=True, state="complete")
		wait(3)
		status.update(label="error example", expanded=True, state="error")