import streamlit as st
import pandas as pd
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import math
import requests
from urllib.parse import quote

# Configure page to exactly match Replit layout
st.set_page_config(
    page_title="Time Better Spent - Bee Friends Cleaners",
    page_icon="🧹",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Exact CSS to match Replit design structure with same color tokens
st.markdown("""
<style>
    /* Import Inter font to match Replit */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    /* CSS tokens - exact match to Replit theme.json */
    :root {
        --primary: 43 96% 56%;
        --background: 0 0% 100%;
        --foreground: 222.2 84% 4.9%;
        --muted-foreground: 215.4 16.3% 46.9%;
        --border: 214.3 31.8% 91.4%;
        --card: 0 0% 100%;
    }
    
    /* Override Streamlit's default theme to match Replit exactly */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background: linear-gradient(to bottom, hsl(var(--primary) / 0.1), hsl(var(--background))) !important;
        color: hsl(var(--foreground)) !important;
    }
    
    /* Global styling to match Replit exactly */
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }
    
    /* Main container with exact Replit gradient using tokens */
    .main > div {
        background: linear-gradient(to bottom, hsl(var(--primary) / 0.1), hsl(var(--background)));
        min-height: 100vh;
        padding: 1rem;
    }
    
    /* Container matching max-w-2xl mx-auto */
    .main-container {
        max-width: 42rem;
        margin: 0 auto;
        padding-top: 2rem;
    }
    
    .results-container {
        max-width: 48rem;
        margin: 0 auto;
        padding-top: 2rem;
    }
    
    /* Header styling - exact match to Replit */
    .header-section {
        text-align: center;
        margin-bottom: 2rem;
        padding-top: 2rem;
    }
    
    .main-title {
        font-size: 2.25rem;
        font-weight: 700;
        background: linear-gradient(to right, hsl(var(--primary)), hsl(var(--primary) / 0.6));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        line-height: 1.1;
    }
    
    .main-subtitle {
        color: hsl(var(--muted-foreground));
        font-size: 1.125rem;
        margin-bottom: 2rem;
    }
    
    /* Card styling to match Replit Card component */
    .replit-card {
        background: hsl(var(--card));
        border-radius: 0.5rem;
        border: 1px solid hsl(var(--border));
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
        overflow: hidden;
        margin: 1.5rem auto;
        max-width: 36rem;
    }
    
    .card-content {
        padding: 1.5rem;
    }
    
    /* Results specific styling */
    .results-title {
        font-size: 2.25rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-align: center;
        color: hsl(var(--foreground));
    }
    
    .results-subtitle {
        color: hsl(var(--muted-foreground));
        font-size: 1.125rem;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    /* Activity card styling */
    .activity-card {
        background: hsl(var(--card));
        border-radius: 0.5rem;
        border: 1px solid hsl(var(--border));
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
        overflow: hidden;
        margin: 1.5rem auto;
    }
    
    /* Hero image section */
    .hero-image {
        height: 16rem;
        background-size: cover;
        background-position: center;
        background-color: hsl(var(--muted-foreground) / 0.1);
        display: flex;
        align-items: center;
        justify-content: center;
        color: hsl(var(--muted-foreground));
        font-size: 3rem;
    }
    
    .activity-header {
        padding: 1.5rem 1.5rem 0 1.5rem;
    }
    
    .activity-title {
        font-size: 1.875rem;
        font-weight: 700;
        color: hsl(var(--foreground));
        margin-bottom: 0;
    }
    
    .activity-content {
        padding: 1.5rem;
    }
    
    .activity-description {
        font-size: 1.25rem;
        color: hsl(var(--muted-foreground));
        margin: 1.5rem 0;
        line-height: 1.6;
    }
    
    /* Time investment section - matches bg-primary/5 */
    .time-investment {
        background-color: hsl(var(--primary) / 0.05);
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin: 1.5rem 0;
    }
    
    .time-investment-label {
        font-size: 1.125rem;
        font-weight: 500;
        color: hsl(var(--primary));
        margin-bottom: 0.5rem;
    }
    
    .time-investment-value {
        color: hsl(var(--muted-foreground));
        font-size: 1rem;
    }
    
    /* Journey section styling */
    .journey-section {
        margin: 1.5rem 0;
    }
    
    .journey-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: hsl(var(--primary));
        margin-bottom: 1rem;
    }
    
    .journey-content {
        line-height: 1.75;
        color: hsl(var(--foreground));
    }
    
    /* Quote section - matches bg-primary/10 */
    .quote-section {
        background-color: hsl(var(--primary) / 0.1);
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-top: 1.5rem;
    }
    
    .quote-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: hsl(var(--primary));
        margin-bottom: 0.5rem;
    }
    
    .quote-subtitle {
        color: hsl(var(--muted-foreground));
        margin-bottom: 1rem;
    }
    
    /* Share section */
    .share-section {
        margin-top: 1.5rem;
        padding-top: 1.5rem;
        border-top: 1px solid hsl(var(--border));
    }
    
    .share-title {
        font-size: 1.125rem;
        font-weight: 500;
        color: hsl(var(--primary));
        margin-bottom: 0.5rem;
    }
    
    .share-description {
        font-size: 0.875rem;
        color: hsl(var(--muted-foreground));
        margin-bottom: 1.5rem;
    }
    
    /* Button styling to match Replit */
    .stButton > button {
        background-color: hsl(var(--primary)) !important;
        color: white !important;
        border: none !important;
        border-radius: 0.375rem !important;
        font-weight: 500 !important;
        transition: all 0.2s !important;
    }
    
    .stButton > button:hover {
        background-color: hsl(var(--primary) / 0.9) !important;
        transform: translateY(-1px) !important;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    
    /* Form styling */
    .stNumberInput > div > div > input,
    .stTextInput > div > div > input {
        border-radius: 0.375rem !important;
        border: 1px solid hsl(var(--border)) !important;
    }
    
    .stNumberInput > div > div > input:focus,
    .stTextInput > div > div > input:focus {
        border-color: hsl(var(--primary)) !important;
        box-shadow: 0 0 0 3px hsl(var(--primary) / 0.1) !important;
    }
</style>
""", unsafe_allow_html=True)

# Core calculation function
def calculate_cleaning_time(square_feet, bedrooms, bathrooms):
    """Calculate cleaning time based on house specifications"""
    hours_per_clean = (square_feet / 750) + (bedrooms * 0.333) + (bathrooms * 0.333)
    total_minutes = round(hours_per_clean * 60)
    monthly_hours = round((total_minutes / 60) * 4, 1)
    return total_minutes, monthly_hours

# Activity matching function
def find_matching_activities(monthly_hours):
    """Find activities that match the available time from cleaning"""
    total_hours = monthly_hours * 6
    
    matching_activities = []
    for activity in activities_data:
        avg_hours = (activity["min_hours"] + activity["max_hours"]) / 2
        if abs(total_hours - avg_hours) <= avg_hours * 0.1:
            matching_activities.append(activity)
    
    if not matching_activities:
        closest_match = min(activities_data, 
                          key=lambda x: abs(total_hours - (x["min_hours"] + x["max_hours"]) / 2))
        matching_activities = [closest_match]
    
    return matching_activities

# Activities data with image URLs
activities_data = [
    {
        "id": "cookie-baking",
        "title": "Bake 52 Different Types of Cookies!",
        "description": "Transform your cleaning time into a delicious baking adventure! From classic chocolate chip to exotic lavender shortbread, master the art of cookie making one week at a time.",
        "category": "culinary",
        "subcategory": "baking", 
        "min_hours": 40,
        "max_hours": 45,
        "image_url": "https://images.unsplash.com/photo-1558961363-fa8fdf82db35?w=800&h=400&fit=crop",
        "timeline": """🍪 **Your Cookie Journey (40-45 hours total)**

**Foundation Phase (15 hours)**
Instead of cleaning for 16 hours:
• Basic techniques (4 hours) - Based on CIA's "Baking Fundamentals" Course
• Ingredient science (3 hours) - King Arthur Baking School curriculum  
• Temperature control (4 hours) - From "The Professional Chef" (10th Edition)
• Basic recipe mastery (4 hours) - America's Test Kitchen methodology

**Classic Cookies (12 hours)**
• Chocolate chip perfection (3 hours) - Jacques Torres technique
• Sugar cookie techniques (3 hours)
• Oatmeal cookie variants (3 hours)
• Shortbread mastery (3 hours)

**Advanced Techniques (13 hours)**
• French macarons (5 hours) - Pierre Hermé's technique
• Complex sandwich cookies (4 hours)
• Decorative techniques (4 hours)

Each 3-hour baking session produces:
• 24-36 cookies
• New skill mastery
• Shareable treats""",
        "expert_quote": "A complete beginner can master basic to intermediate cookie baking in 40-45 hours of dedicated practice. - Christina Tosi, James Beard Award Winner"
    },
    {
        "id": "watercolor-painting", 
        "title": "Master Watercolor Painting",
        "description": "Turn your cleaning hours into beautiful watercolor masterpieces! Learn techniques from basic washes to advanced color mixing and create stunning artwork.",
        "category": "art",
        "subcategory": "painting",
        "min_hours": 30,
        "max_hours": 40,
        "image_url": "https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?w=800&h=400&fit=crop",
        "timeline": """🎨 **Your Watercolor Journey (30-40 hours total)**

**Foundation Skills (12 hours)**
• Color theory and mixing (4 hours)
• Brush techniques and control (4 hours) 
• Paper and material knowledge (4 hours)

**Core Techniques (18 hours)**
• Wet-on-wet techniques (6 hours)
• Wet-on-dry precision work (6 hours)
• Layering and glazing (6 hours)

**Advanced Projects (10 hours)**
• Landscape compositions (4 hours)
• Portrait techniques (3 hours)
• Abstract expressions (3 hours)

What You'll Create:
• 15+ finished paintings
• Personal art style
• Portfolio-ready pieces
• Relaxation and mindfulness""",
        "expert_quote": "30-40 hours of focused watercolor practice will develop solid foundational skills and personal artistic voice. - David Hockney"
    }
]

# Main app function
def main():
    # Home page layout
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Header section - exact match to Replit
    st.markdown("""
    <div class="header-section">
        <h1 class="main-title">Time Better Spent</h1>
        <p class="main-subtitle">See what amazing things you could do instead of cleaning your house</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Card container - exact match to Replit Card
    st.markdown('<div class="replit-card"><div class="card-content">', unsafe_allow_html=True)
    
    # Form inputs in columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        square_feet = st.number_input(
            "Square Feet",
            min_value=500,
            max_value=10000,
            value=2000,
            step=100
        )
    
    with col2:
        bedrooms = st.number_input(
            "Number of Bedrooms", 
            min_value=1,
            max_value=5,
            value=3,
            step=1
        )
    
    with col3:
        bathrooms = st.number_input(
            "Number of Bathrooms",
            min_value=1, 
            max_value=6,
            value=2,
            step=1
        )
    
    # Calculate button
    if st.button("Show Me What I Could Do Instead!", use_container_width=True):
        calculate_and_display_results(square_feet, bedrooms, bathrooms)
    
    st.markdown('</div></div></div>', unsafe_allow_html=True)

def calculate_and_display_results(square_feet, bedrooms, bathrooms):
    # Calculate cleaning time
    total_minutes, monthly_hours = calculate_cleaning_time(square_feet, bedrooms, bathrooms)
    
    # Results container
    st.markdown('<div class="results-container">', unsafe_allow_html=True)
    
    # Header section
    st.markdown(f"""
    <div class="header-section">
        <h1 class="results-title">Instead of spending {round(monthly_hours)} hours cleaning each month...</h1>
        <p class="results-subtitle">Here's something amazing you could do!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Find matching activities  
    matching_activities = find_matching_activities(monthly_hours)
    activity = matching_activities[0]
    
    # Activity card - exact structure match
    st.markdown(f"""
    <div class="activity-card">
        <div class="hero-image" style="background-image: url('{activity['image_url']}');">
            🎨
        </div>
        <div class="activity-header">
            <h2 class="activity-title">{activity['title']}</h2>
        </div>
        <div class="activity-content">
            <p class="activity-description">{activity['description']}</p>
            
            <div class="time-investment">
                <p class="time-investment-label">Time Investment:</p>
                <p class="time-investment-value">{activity['min_hours']}-{activity['max_hours']} hours total</p>
            </div>
            
            <div class="journey-section">
                <h3 class="journey-title">Your Journey</h3>
                <div class="journey-content">
                    {activity['timeline'].replace(chr(10), '<br>')}
                </div>
            </div>
            
            <div class="quote-section">
                <h3 class="quote-title">Ready to Get Started?</h3>
                <p class="quote-subtitle">Get your house professionally cleaned and use your free time for {activity['title'].lower()}! Get a free quote now and receive a special $40 off coupon.</p>
    """, unsafe_allow_html=True)
    
    # Quote form
    with st.form("quote_form"):
        form_col1, form_col2 = st.columns(2)
        
        with form_col1:
            name = st.text_input("Full Name")
            email = st.text_input("Email")
        
        with form_col2:
            zip_code = st.text_input("Zip Code")
            phone = st.text_input("Phone (Optional)")
        
        st.write(f"**House:** {square_feet} sq ft, {bedrooms} bedrooms, {bathrooms} bathrooms")
        
        submitted = st.form_submit_button("🎉 Get My Free Quote + $40 Off!")
        
        if submitted:
            if name and email and zip_code:
                st.success("🎉 Thank you! We'll send your personalized quote within 24 hours, plus your $40 off coupon!")
                st.balloons()
            else:
                st.error("Please fill in all required fields")
    
    # Share section
    share_text = f"I could save {round(monthly_hours)} hours per month by hiring Bee Friends Cleaners! Instead of cleaning, I could {activity['title'].lower()}. Use code TAKE40OFF for $40 off!"
    
    st.markdown(f"""
        <div class="share-section">
            <p class="share-title">🎉 Spread the Joy! Help Friends Reclaim Their Time</p>
            <p class="share-description">Found an amazing alternative to cleaning? Share your discovery and special $40 off coupon with friends!</p>
        </div>
    </div>
    </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Share buttons
    share_col1, share_col2, share_col3 = st.columns(3)
    
    with share_col1:
        if st.button("📱 Share on Twitter"):
            twitter_url = f"https://twitter.com/intent/tweet?text={quote(share_text)}"
            st.markdown(f"[Open Twitter]({twitter_url})")
    
    with share_col2:
        if st.button("📘 Share on Facebook"):
            facebook_url = f"https://www.facebook.com/sharer/sharer.php?u=https://beefriendcleaners.com&quote={quote(share_text)}"
            st.markdown(f"[Open Facebook]({facebook_url})")
    
    with share_col3:  
        if st.button("💼 Share on LinkedIn"):
            linkedin_url = f"https://www.linkedin.com/sharing/share-offsite/?url=https://beefriendcleaners.com&summary={quote(share_text)}"
            st.markdown(f"[Open LinkedIn]({linkedin_url})")

# Sidebar
with st.sidebar:
    st.header("About Bee Friends Cleaners")
    st.write("Professional house cleaning services with eco-friendly products and exceptional customer care.")
    
    st.subheader("Contact")
    st.write("📞 (555) 123-CLEAN")
    st.write("📧 hello@beefriends.com")
    st.write("🌐 beefriendcleaners.com")

if __name__ == "__main__":
    main()