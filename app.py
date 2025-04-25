import streamlit as st
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Authenticate with Google Sheets using secrets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_dict = json.loads(st.secrets["GOOGLE_SHEETS_CREDENTIALS"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)
sheet = client.open("KKP Survey").worksheet("Responses")

st.image("https://i.imgur.com/TqKbulk.png", width=200)

# Title and intro
st.title("🧘 Kapwa Kalinga Wellness Check-In")
st.markdown("Welcome! Please take a moment to complete this short self-check and help us design better wellness programs for our healthcare community.")

# Demographics
st.header("👤 Quick Demographic Info")

gender = st.radio("Gender", ["Female", "Male", "Non-binary", "Prefer not to say"])
age_group = st.radio("Age Group", ["18-25", "26-35", "36-45", "46-60", "60+"])
role = st.selectbox("Your Role", ["Nurse", "Physician", "Admin", "Other"])
department = st.text_input("Department / Unit")
years_exp = st.selectbox("Years of Experience", ["<1", "1-5", "6-10", "11-20", "21+"])
shift_type = st.radio("What shift do you usually work?", ["Day", "Night", "Rotating"])
pnany_member = st.radio("Are you a PNANY Member?", ["Yes", "No"])

# Burnout Assessment
st.header("💢 Burnout Self-Assessment")

q1 = st.slider("I feel emotionally drained by my work", 1, 5)
q2 = st.slider("I struggle to concentrate on tasks", 1, 5)
q3 = st.slider("I feel mentally distant from my work", 1, 5)
q4 = st.slider("I feel emotionally overreactive or numb at work", 1, 5)
burnout_score = q1 + q2 + q3 + q4

st.write(f"**Your Burnout Score:** {burnout_score}/20")

# Wellness interests
st.header("🌿 What Wellness Topics Are You Interested In?")
interests = st.multiselect("Choose all that apply:", [
    "Mindfulness", "Yoga", "Group Fitness", "Peer Support",
    "Creative Therapy", "Nutrition & Sleep", "1-on-1 Coaching"
])
other_suggestions = st.text_input("Other suggestions you'd like to see?")

# Interest in KKP Peer Support Group
st.markdown("### 💬 Interested in Peer Support?")
support_interest = st.radio(
    "Would you like to join the PNANY KKP Peer Support Group or be contacted for future Mental Health & Wellness Programs?",
    ["Yes", "No"]
)
st.markdown("📩 If yes, we will reach out to you via **wellness@pnanewyork.org**.")

# Submit form
if st.button("📩 Submit"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([
        timestamp,
        gender,
        age_group,
        role,
        department,
        years_exp,
        shift_type,
        pnany_member,
        support_interest,
        burnout_score,
        q1, q2, q3, q4,
        ", ".join(interests),
        other_suggestions
    ])
    st.success("✅ Your response has been recorded. Thank you!")

st.markdown(
    "<div style='text-align: center;'>"
    "<img src='https://i.imgur.com/J6FyF0Z.png' width='150'>"
    "</div>",
    unsafe_allow_html=True
)

