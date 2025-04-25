import streamlit as st
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import random


# Authenticate with Google Sheets using secrets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_dict = json.loads(st.secrets["GOOGLE_SHEETS_CREDENTIALS"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)
sheet = client.open("KKP Survey").worksheet("Responses")

#st.image("https://i.imgur.com/TqKbulk.png", width=200)

st.markdown(
    "<div style='text-align: center;'>"
    "<img src='https://i.imgur.com/TqKbulk.png' width='200'>"
    "</div>",
    unsafe_allow_html=True
)


# Title and intro
st.title("🧘 Kapwa Kalinga Program Needs Assessment")
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
# st.header("💢 Burnout Self-Assessment")

# st.markdown("""
# **Burnout Scoring Scale**  
# 1 = Least / Never  5 = Most / Always
# """)


# q1 = st.slider("I feel emotionally drained by my work", 1, 5)
# q2 = st.slider("I struggle to concentrate on tasks", 1, 5)
# q3 = st.slider("I feel mentally distant from my work", 1, 5)
# q4 = st.slider("I feel emotionally overreactive or numb at work", 1, 5)

st.header("💢 Burnout Self-Assessment")

st.markdown("**Burnout Scoring Scale**")

# Display labels on both ends of the scale
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.write("⬅️ Least / Never")
with col3:
    st.write("Most / Always ➡️")

# Burnout sliders
q1 = st.slider("I feel emotionally drained by my work", 1, 5)
q2 = st.slider("I struggle to concentrate on tasks", 1, 5)
q3 = st.slider("I feel mentally distant from my work", 1, 5)
q4 = st.slider("I feel emotionally overreactive or numb at work", 1, 5)


burnout_score = q1 + q2 + q3 + q4

st.write(f"**Your Burnout Score:** {burnout_score}/20")

if burnout_score <= 8:
    st.success("✅ Low Risk of Burnout – Keep up your self-care habits!")
elif 9 <= burnout_score <= 13:
    st.warning("⚠️ Moderate Risk – You may be showing early signs of burnout.")
elif 14 <= burnout_score <= 16:
    st.error("🔴 High Risk – Consider taking steps toward stress reduction and support.")
else:
    st.error("🚨 Very High Risk – Please prioritize self-care and seek peer or professional support.")

st.header("🧘 Current Self-Care and Wellness Practices")

## baseline info
# st.markdown("""
# **How often do you currently engage in the following?**  
# (1 = Not at all  5 = Alwaysy)
# """)
##

st.markdown("**How often do you currently engage in the following?**")

# Display scale labels on both ends
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.write("⬅️ Not at all")
with col3:
    st.write("Always ➡️")

##

sleep = st.slider("Sleep hygiene (consistent, restful sleep)", 1, 5)
exercise = st.slider("Physical activity (e.g., walking, stretching, workouts)", 1, 5)
nutrition = st.slider("Healthy nutrition and hydration habits", 1, 5)
mindfulness = st.slider("Mindfulness or meditation practices", 1, 5)
social_support = st.slider("Spending time with supportive people", 1, 5)
spirituality = st.slider("Spiritual or faith-based practices (e.g., prayer, reflection)", 1, 5)
mental_health_access = st.slider("Seeking mental health support (counseling, therapy)", 1, 5)
##

# Wellness interests
# st.header("🌿 What Wellness Topics Are You Interested In?")

# st.markdown("""
# _These wellness activities are informed by evidence-based research from WHO, ANA Healthy Nurse Healthy Nation™, burnout recovery frameworks (Maslach, Schaufeli), CDC guidelines, and trauma-informed care best practices._

# _Select all topics that you would be interested in attending or learning more about:_
# """)

# interests = st.multiselect("Choose all that apply:", [
#     "Mindfulness & Meditation",
#     "Yoga or Stretching",
#     "Creative Arts Therapy (Art, Music, Dance)",
#     "Group Fitness or Walking Clubs",
#     "Spiritual or Faith-based Reflection",
#     "One-on-One Peer Support or Coaching",
#     "Mental Health Counseling or Therapy",
#     "Journaling & Reflective Writing",
#     "Sleep Health Education",
#     "Nutrition & Hydration Habits",
#     "Time Management & Work-Life Balance",
#     "Resilience and Emotional Intelligence Training",
#     "Gratitude Practices",
#     "Digital Detox or Tech-life Balance",
#     "Nature or Outdoor Wellness Activities",
#     "Stress Reduction Workshops",
#     "Trauma-Informed Care & Support Groups"
# ])

st.markdown("### 🌿 What Wellness Topics Are You Interested In?")

st.markdown("""
_These wellness activities are informed by evidence-based research from WHO, ANA Healthy Nurse Healthy Nation™, burnout recovery frameworks (Maslach, Schaufeli), CDC guidelines, and trauma-informed care best practices._

_Select all topics that you would be interested in attending or learning more about:_
""")

# List of wellness interests
interest_options = [
    "Mindfulness & Meditation",
    "Yoga or Stretching",
    "Creative Arts Therapy (Art, Music, Dance)",
    "Group Fitness or Walking Clubs",
    "Spiritual or Faith-based Reflection",
    "One-on-One Peer Support or Coaching",
    "Mental Health Counseling or Therapy",
    "Journaling & Reflective Writing",
    "Sleep Health Education",
    "Nutrition & Hydration Habits",
    "Time Management & Work-Life Balance",
    "Resilience and Emotional Intelligence Training",
    "Gratitude Practices",
    "Digital Detox or Tech-life Balance",
    "Nature or Outdoor Wellness Activities",
    "Stress Reduction Workshops",
    "Trauma-Informed Care & Support Groups"
]

# Create three columns
col1, col2, col3 = st.columns(3)

# Collect checked interests
interests = []

for i, option in enumerate(interest_options):
    if i % 3 == 0:
        with col1:
            if st.checkbox(option):
                interests.append(option)
    elif i % 3 == 1:
        with col2:
            if st.checkbox(option):
                interests.append(option)
    else:
        with col3:
            if st.checkbox(option):
                interests.append(option)


# 🔵 ADD THIS MISSING FIELD
other_suggestions = st.text_area("Any other wellness topics or suggestions? (Optional)")

# Interest in KKP Peer Support Group
st.markdown("### 💬 Interested in Peer Support?")
support_interest = st.radio(
    "Would you like to join the PNANY KKP Peer Support Group or be contacted for future Mental Health & Wellness Programs?",
    ["Yes", "No"]
)

##

#st.markdown("📩 If yes, we will reach out to you via **wellness@pnanewyork.org**")

st.markdown("📩 If yes, we will reach out to you via [wellness@pnanewyork.org](mailto:wellness@pnanewyork.org)")

st.markdown("### 📝 Optional Contact Info")

contact_name = st.text_input("Name (optional)")
contact_email = st.text_input("Email address (optional)")


# Submit form
# if st.button("📩 Submit"):
#     #timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# ##
    
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     date_prefix = datetime.now().strftime("%Y%m%d")
#     random_digits = str(random.randint(1000, 9999))
#     confirmation_number = f"KKP-{date_prefix}-{random_digits}"

# ##    
#     st.write("Collected values:", [
#         timestamp,
#         gender,
#         age_group,
#         role,
#         department,
#         years_exp,
#         shift_type,
#         pnany_member,
#         support_interest,
#         burnout_score,
#         q1, q2, q3, q4,
#         sleep, exercise, nutrition, mindfulness, social_support, spirituality, mental_health_access,
#         ", ".join(interests),
#         other_suggestions,
#         contact_name,
#         contact_email,
#         confirmation_number
#     ])


# #
#     st.success("✅ Your response has been recorded. Thank you for prioritizing your wellness with us. 🌿")

# st.info(f"📋 Your Confirmation Number: **{confirmation_number}**")
# st.caption("Please save this number for your reference.")
##

# Submit form
if st.button("📩 Submit"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_prefix = datetime.now().strftime("%Y%m%d")
    random_digits = str(random.randint(1000, 9999))
    confirmation_number = f"KKP-{date_prefix}-{random_digits}"

    # Save to Google Sheet
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
        sleep, exercise, nutrition, mindfulness, social_support, spirituality, mental_health_access,
        ", ".join(interests),
        other_suggestions,
        contact_name,
        contact_email,
        confirmation_number  # <-- added here
    ])

    # Show success message
    st.success("✅ Your response has been recorded. Thank you for prioritizing your wellness with us. 🌿")
    st.info(f"📋 Your Confirmation Number: **{confirmation_number}**")
    st.caption("Please save this number for your reference.")

##
st.markdown(
    "<div style='text-align: center;'>"
    "<img src='https://i.imgur.com/J6FyF0Z.png' width='300'>"
    "</div>",
    unsafe_allow_html=True)


st.markdown("---")


st.caption("Together, We Thrive.")

st.caption("This wellness tool is brought to you by PNANY Kapwa Kalinga Program 💙")

st.caption("Reference: Schaufeli, W.B., Desart, S. and De Witte, H. (2020). *Burnout Assessment Tool (BAT)—development, validity, and reliability*. International Journal of Environmental Research and Public Health, 17(24), p. 9495. https://doi.org/10.3390/ijerph17249495")


