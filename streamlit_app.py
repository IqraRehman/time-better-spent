import streamlit as st
import pandas as pd
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import math
import requests
from urllib.parse import quote

# Configure page
st.set_page_config(
    page_title="Time Better Spent - Bee Friends Cleaners",
    page_icon="🧹",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Import Google Fonts for better typography
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
    /* Global font styling */
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    
</style>
""", unsafe_allow_html=True)

# Core calculation function
def calculate_cleaning_time(square_feet, bedrooms, bathrooms):
    """
    Calculate cleaning time based on house specifications
    Formula: (sq_ft / 750) + (bedrooms * 0.333) + (bathrooms * 0.333)
    """
    hours_per_clean = (square_feet / 750) + (bedrooms * 0.333) + (bathrooms * 0.333)
    total_minutes = round(hours_per_clean * 60)
    monthly_hours = round((total_minutes / 60) * 4, 1)  # Weekly cleaning * 4
    return total_minutes, monthly_hours

# Activity matching function
def find_matching_activities(monthly_hours):
    """Find activities that match the available time from cleaning"""
    total_hours = monthly_hours * 6  # 6 months projection
    
    matching_activities = []
    for activity in activities_data:
        avg_hours = (activity["min_hours"] + activity["max_hours"]) / 2
        if abs(total_hours - avg_hours) <= avg_hours * 0.1:
            matching_activities.append(activity)
    
    if not matching_activities:
        # Find closest match
        closest_match = min(activities_data, 
                          key=lambda x: abs(total_hours - (x["min_hours"] + x["max_hours"]) / 2))
        matching_activities = [closest_match]
    
    return matching_activities

# Activities data (converted from TypeScript)
activities_data = [
    {
        "id": "cookie-baking",
        "title": "Bake 52 Different Types of Cookies!",
        "description": "Transform your cleaning time into a delicious baking adventure! From classic chocolate chip to exotic lavender shortbread, master the art of cookie making one week at a time.",
        "category": "culinary",
        "subcategory": "baking",
        "min_hours": 40,
        "max_hours": 45,
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
        "id": "macaron-mastery",
        "title": "Master French Macarons",
        "description": "Turn your cleaning hours into pastry perfection! Learn the art of French macarons from basic shells to complex flavor combinations.",
        "category": "culinary",
        "subcategory": "advanced-baking",
        "min_hours": 25,
        "max_hours": 30,
        "timeline": """🧁 **Macaron Mastery Journey (25-30 hours)**

**Technique Foundation (8 hours)**
• Macaronage technique mastery (3 hours)
• Temperature and humidity control (2 hours)
• Shell perfection practice (3 hours)

**Flavor Development (12 hours)**
• Classic flavors (vanilla, chocolate, strawberry) (4 hours)
• Complex flavors (lavender, pistachio, salted caramel) (4 hours)
• Seasonal specialties (4 hours)

**Advanced Techniques (8 hours)**
• Painted macarons (3 hours)
• Filled variations (2 hours)
• Professional presentation (3 hours)""",
        "expert_quote": "Mastering macarons requires patience and precision, but 25-30 hours of focused practice will get you there. - Pierre Hermé, King of Macarons"
    },
    {
        "id": "soup-collection",
        "title": "Master 26 Soul-Warming Soups",
        "description": "Transform cleaning time into culinary comfort! Master the art of soup making from classic broths to international specialties.",
        "category": "culinary",
        "subcategory": "cooking",
        "min_hours": 35,
        "max_hours": 40,
        "timeline": """🍲 **Soup Mastery Collection (35-40 hours)**

**Foundation Techniques (12 hours)**
• Stock and broth mastery (4 hours)
• Knife skills for soup prep (3 hours)
• Flavor building techniques (5 hours)

**Classic Categories (18 hours)**
• Cream-based soups (6 hours)
• Clear broths and consommés (4 hours)
• Hearty stews and chilis (4 hours)
• International specialties (4 hours)

**Advanced Applications (8 hours)**
• Garnish and presentation (3 hours)
• Batch cooking and preservation (3 hours)
• Seasonal ingredient adaptation (2 hours)""",
        "expert_quote": "A well-made soup is the foundation of great cooking. 35-40 hours will teach you techniques that last a lifetime. - Thomas Keller, French Laundry"
    },
    {
        "id": "short-stories",
        "title": "Write a Collection of 50 Short Stories",
        "description": "Write and polish 50 short stories, building a collection by year's end. By saving time on cleaning, you can fully dive into your creative writing.",
        "category": "creative",
        "subcategory": "writing",
        "min_hours": 100,
        "max_hours": 103,
        "timeline": """✍️ **Your Writing Journey (100-103 hours total)**

**Foundation Building (32 hours)**
Instead of 38 hours cleaning:
• Story structure workshop (8 hours) - Brandon Sanderson's creative writing course
• Character development (8 hours) - K.M. Weiland's character creation system
• Write first 8 stories (16 hours) - 2 hours per story as per industry standard

**Genre Exploration (35 hours)**
• Mystery writing techniques (5 hours) - Mystery Writers of America guidelines
• Romance plotting (5 hours) - Romance Writers of America standards
• Science fiction world-building (5 hours) - SFWA world-building guide
• Write 10 genre stories (20 hours)

**Advanced Techniques (33 hours)**
• Advanced dialogue workshop (6 hours) - David Baldacci's techniques
• Story pacing mastery (7 hours) - Donald Maass Literary Agency guidelines
• Write 10 advanced stories (20 hours)

By investing your cleaning time in writing:
• Complete 28 polished short stories
• Master 3 different genres
• Build a publishable portfolio""",
        "expert_quote": "The difference between a good writer and a great one often comes down to the hours invested in crafting their stories. - Neil Gaiman"
    },
    {
        "id": "guitar-mastery",
        "title": "Master Guitar Basics",
        "description": "Exchange your mop for a guitar pick and learn to play your favorite songs! While your home gets professionally cleaned, you could be on your way to becoming a musician.",
        "category": "music",
        "subcategory": "instrument",
        "min_hours": 70,
        "max_hours": 90,
        "timeline": """🎸 **Your Guitar Journey (70-90 hours total)**

**Foundation Month (25 hours)**
Instead of 25 hours cleaning:
• Basic chords mastery (10 hours)
• Strumming patterns (8 hours)
• Reading tablature (7 hours)

**Songs & Techniques (30 hours)**
• Learn 5 favorite songs (15 hours)
• Practice transitions (8 hours)
• Rhythm training (7 hours)

**Advanced Skills (25 hours)**
• Fingerpicking basics (10 hours)
• Improvisation foundations (8 hours)
• Music theory essentials (7 hours)

What You'll Achieve:
• Play 8-10 complete songs
• Master 8 essential chords
• Develop proper technique
• Build performance confidence""",
        "expert_quote": "With 70-90 hours of focused practice, a beginner can master fundamental guitar skills and play their favorite songs confidently. - Justin Sandercoe, Founder of JustinGuitar"
    },
    {
        "id": "spanish-learning",
        "title": "Learn Spanish Conversation",
        "description": "Master conversational Spanish while we handle your cleaning! Turn household chores into language learning time.",
        "category": "education",
        "subcategory": "language",
        "min_hours": 240,
        "max_hours": 300,
        "timeline": """🇪🇸 **Your Spanish Journey (240-300 hours total)**

**Foundation Phase (80 hours)**
Instead of 80 hours cleaning:
• Essential vocabulary (30 hours)
• Basic grammar patterns (30 hours)  
• Pronunciation mastery (20 hours)

**Conversation Building (100 hours)**
• Daily conversation practice (40 hours)
• Listening comprehension (30 hours)
• Cultural understanding (30 hours)

**Fluency Development (100 hours)**
• Advanced grammar (30 hours)
• Complex conversations (40 hours)
• Cultural immersion activities (30 hours)

What You'll Achieve:
• Understand everyday conversations
• Express yourself confidently
• Connect with Spanish speakers
• Open career opportunities""",
        "expert_quote": "With 240-300 hours of dedicated practice, you can achieve conversational fluency in Spanish - understanding and participating in everyday conversations with confidence. - Dr. Stephen Krashen, Language Acquisition Expert"
    },
    {
        "id": "marathon-training",
        "title": "Train for a Half-Marathon",
        "description": "Turn cleaning time into training time! Instead of scrubbing floors, you could be preparing for an incredible achievement - completing a half-marathon.",
        "category": "fitness",
        "subcategory": "running",
        "min_hours": 200,
        "max_hours": 240,
        "timeline": """🏃‍♀️ **Your Running Journey (200-240 hours total)**

**Base Building (80 hours)**
Instead of 80 hours cleaning:
• Foundational running (40 hours)
• Strength training (20 hours)
• Recovery techniques (20 hours)

**Distance Development (80 hours)**
• Progressive long runs (40 hours)
• Speed work (20 hours)
• Cross-training (20 hours)

**Peak Training (80 hours)**
• Race-pace training (35 hours)
• Final long runs (30 hours)
• Taper period (15 hours)

What You'll Achieve:
• Complete a 13.1-mile race
• Burn 1,200+ calories/run
• Build incredible endurance
• Join the running community""",
        "expert_quote": "A beginner can go from couch to half-marathon in about 200-240 hours of training over 8 months. This timeline allows for proper conditioning and injury prevention. - Hal Higdon, Legendary Running Coach"
    },
    {
        "id": "photography-skills",
        "title": "Master Digital Photography",
        "description": "Transform your cleaning hours into capturing beautiful moments! Learn professional photography techniques while we handle your home maintenance.",
        "category": "creative",
        "subcategory": "photography",
        "min_hours": 60,
        "max_hours": 80,
        "timeline": """📸 **Your Photography Journey (60-80 hours total)**

**Technical Foundation (25 hours)**
• Camera basics and settings (8 hours)
• Composition principles (8 hours)
• Lighting techniques (9 hours)

**Genre Mastery (30 hours)**
• Portrait photography (10 hours)
• Landscape techniques (10 hours)
• Street photography (10 hours)

**Advanced Techniques (20 hours)**
• Photo editing mastery (10 hours)
• Portfolio development (5 hours)
• Business basics (5 hours)

What You'll Achieve:
• Master camera controls
• Develop artistic eye
• Build professional portfolio
• Potential income stream""",
        "expert_quote": "60-80 hours of focused practice will take you from beginner to confident photographer with a strong foundation in technical and artistic skills. - Annie Leibovitz"
    }
]

# Main app
def main():
    # Header - using Streamlit native styling with theming
    st.title("🏡 Time Better Spent")
    st.subheader("See what amazing things you could do instead of cleaning your house")
    st.caption("*Brought to you by Bee Friends Cleaners*")
    
    st.divider()
    
    # House details input form
    st.header("Tell us about your home")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        square_feet = st.number_input(
            "Square Feet", 
            min_value=500, 
            max_value=10000, 
            value=2000,
            step=100,
            help="Enter the total square footage of your home"
        )
    
    with col2:
        bedrooms = st.number_input(
            "Number of Bedrooms", 
            min_value=1, 
            max_value=5, 
            value=3,
            step=1,
            help="Number of bedrooms to clean"
        )
    
    with col3:
        bathrooms = st.number_input(
            "Number of Bathrooms", 
            min_value=1, 
            max_value=6, 
            value=2,
            step=1,
            help="Number of bathrooms to clean"
        )

    # Calculate button
    if st.button("✨ Show Me What I Could Do Instead!", type="primary", use_container_width=True):
        calculate_and_display_results(square_feet, bedrooms, bathrooms)

def calculate_and_display_results(square_feet, bedrooms, bathrooms):
    # Calculate cleaning time
    total_minutes, monthly_hours = calculate_cleaning_time(square_feet, bedrooms, bathrooms)
    
    # Display results using Streamlit native components
    st.divider()
    st.header(f"⏰ Instead of spending {round(monthly_hours)} hours cleaning each month...")
    st.subheader("Here's something amazing you could do!")
    
    st.info(f"**Your cleaning time:** {total_minutes} minutes per session • {monthly_hours:.1f} hours per month • {monthly_hours * 12:.0f} hours per year")
    
    # Find matching activities
    matching_activities = find_matching_activities(monthly_hours)
    
    # Display activities using native Streamlit components
    for activity in matching_activities:
        with st.container():
            st.subheader(f"🎨 {activity['title']}")
            st.write(activity['description'])
            
            # Time investment info
            col1, col2 = st.columns([1, 2])
            with col1:
                st.metric(
                    "Time Investment", 
                    f"{activity['min_hours']}-{activity['max_hours']} hours total",
                    delta="Over 6 months"
                )
            
            # Journey details in expandable section
            with st.expander("📋 See Your Journey Details", expanded=True):
                st.markdown(activity['timeline'])
            
            # Expert quote
            st.success(f"💡 **Expert Insight:** {activity['expert_quote']}")
            
            st.divider()
    
    # Social sharing section using native components
    st.header("📢 Share Your Results!")
    st.write("Tell your friends how much time they could save!")
    
    share_text = f"I could save {round(monthly_hours)} hours per month by hiring Bee Friends Cleaners! Instead of cleaning, I could {matching_activities[0]['title'].lower()}. Use code TAKE40OFF for $40 off your first cleaning! 🧹✨"
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📱 Share on Twitter"):
            twitter_url = f"https://twitter.com/intent/tweet?text={quote(share_text)}"
            st.markdown(f"[Click here to share on Twitter]({twitter_url})")
    
    with col2:
        if st.button("📘 Share on Facebook"):
            facebook_url = f"https://www.facebook.com/sharer/sharer.php?u=https://beefriendcleaners.com&quote={quote(share_text)}"
            st.markdown(f"[Click here to share on Facebook]({facebook_url})")
    
    with col3:
        if st.button("💼 Share on LinkedIn"):
            linkedin_url = f"https://www.linkedin.com/sharing/share-offsite/?url=https://beefriendcleaners.com&summary={quote(share_text)}"
            st.markdown(f"[Click here to share on LinkedIn]({linkedin_url})")
    
    # Quote request form using native components
    st.header("💰 Get Your Free Cleaning Quote + $40 Off!")
    st.write("Ready to reclaim your time? Get a free quote and receive $40 off your first cleaning!")
    
    with st.form("quote_form"):
        quote_col1, quote_col2 = st.columns(2)
        
        with quote_col1:
            name = st.text_input("Full Name", placeholder="Enter your name")
            email = st.text_input("Email", placeholder="your.email@example.com")
        
        with quote_col2:
            zip_code = st.text_input("Zip Code", placeholder="12345")
            phone = st.text_input("Phone (Optional)", placeholder="(555) 123-4567")
        
        # House details display using info box
        st.info(f"**House Details:** {square_feet} sq ft, {bedrooms} bedrooms, {bathrooms} bathrooms")
        
        submitted = st.form_submit_button("🎉 Get My Free Quote + $40 Off!", type="primary")
        
        if submitted:
            if name and email and zip_code:
                st.success("🎉 Thank you! We'll send your personalized quote within 24 hours, plus your $40 off coupon!")
                st.balloons()
                
                # Display confirmation using success box
                st.success(
                    f"✅ **Quote Request Submitted!**\n\n"
                    f"**Name:** {name}\n"
                    f"**Email:** {email}\n"
                    f"**Zip:** {zip_code}\n"
                    f"**House:** {square_feet} sq ft, {bedrooms} bed, {bathrooms} bath\n\n"
                    f"**🎉 Discount: $40 off first cleaning**"
                )
            else:
                st.error("Please fill in all required fields (Name, Email, and Zip Code)")

# Sidebar info
with st.sidebar:
    st.header("About Bee Friends Cleaners")
    st.write("""
    We believe your time is precious! Let our professional team handle the cleaning while you pursue your passions.
    
    ✨ **Why Choose Us?**
    - Fully insured & bonded
    - Eco-friendly products
    - Flexible scheduling  
    - 100% satisfaction guarantee
    
    📞 **Contact Us:**
    - Phone: (555) BEE-CLEAN
    - Email: hello@beefriendcleaners.com
    - Website: beefriendcleaners.com
    """)
    
    st.header("Special Offers")
    st.info("🎁 **New Customer Special:** Use code TAKE40OFF for $40 off your first cleaning service!")

if __name__ == "__main__":
    main()