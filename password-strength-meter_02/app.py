import streamlit as st
import re
import random
import string

# --- Password Strength Checking Function ---
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

# --- Password Generator ---
def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

# --- Streamlit UI ---
st.set_page_config(page_title="🔐 Password Strength Meter", layout="centered")
st.title("🔐 Password Strength Meter")
st.markdown("Check how strong your password is and get suggestions!")

password = st.text_input("🔑 Enter your password", type="password")

if st.button("Check Strength"):
    if not password:
        st.warning("Please enter a password first.")
    else:
        score, issues = check_password_strength(password)

        if score == 4:
            st.success("✅ Strong Password! Great job!")
        elif score == 3:
            st.info("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using suggestions below.")

        for issue in issues:
            st.write(issue)

# Optional password suggestion
st.markdown("---")
st.subheader("💡 Need a strong password?")
if st.button("Generate Strong Password"):
    strong_pass = generate_strong_password()
    st.code(strong_pass, language="text")
