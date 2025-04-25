import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Authenticate with Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

#creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
##
import json

# Authenticate with Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_dict = json.loads(st.secrets["GOOGLE_SHEETS_CREDENTIALS"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)
sheet = client.open("KKP Survey").worksheet("Responses")

##

client = gspread.authorize(creds)
sheet = client.open("KKP Survey").worksheet("Responses")

# UI Layout
st.title("🧘 Kapwa Kalinga Wellness Check-In")
st.markdown("Welcome! Please take a moment to complete this short self-check and help us design better wellness programs for our healthcare community.")

st.header("💢 Burnout Self-Assessment")

# Burnout questions
q1 = st.slider("I feel emotionally drained by my work", 1, 5)
q2 = st.slider("I struggle to concentrate on tasks", 1, 5)
q3 = st.slider("I feel mentally distant from my work", 1, 5)
q4 = st.slider("I feel emotionally overreactive or numb at work", 1, 5)
burnout_score = q1 + q2 + q3 + q4

st.write(f"**Your Burnout Score:** {burnout_score}/20")

# Wellness interests
st.header("🌿 What Wellness Topics Are You Interested In?")
interests = st.multiselect("Choose all that apply:",
    ["Mindfulness", "Yoga", "Group Fitness", "Peer Support", "Creative Therapy", "Nutrition & Sleep", "1-on-1 Coaching"])

other_suggestions = st.text_input("Other suggestions you'd like to see?")

# Submit form
if st.button("📩 Submit"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp, burnout_score, q1, q2, q3, q4, ", ".join(interests), other_suggestions])
    st.success("✅ Your response has been recorded. Thank you!")
