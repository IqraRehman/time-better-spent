import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import json
import math
from urllib.parse import quote

# Configure page
st.set_page_config(
    page_title="Time Better Spent - Bee Friends Cleaners",
    page_icon="🧹",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit elements and set background color
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    .main > div {
        padding: 0 !important;
    }
    .stApp {
        background-color: #EFE9DB;
    }
    .main .block-container {
        background-color: #EFE9DB;
    }
</style>
""", unsafe_allow_html=True)

# Core calculation function
def calculate_cleaning_time(square_feet, bedrooms, bathrooms):
    hours_per_clean = (square_feet / 750) + (bedrooms * 0.333) + (bathrooms * 0.333)
    total_minutes = round(hours_per_clean * 60)
    monthly_hours = round((total_minutes / 60) * 4, 1)
    return total_minutes, monthly_hours

def find_matching_activities(monthly_hours):
    total_hours = monthly_hours * 6
    
    # Complete activities data from Replit app
    activities_data = [
        {
            "id": "short-stories",
            "title": "Write a Collection of 50 Short Stories",
            "description": "Write and polish 50 short stories, building a collection by year's end. By saving time on cleaning, you can fully dive into your creative writing.",
            "min_hours": 100,
            "max_hours": 103,
            "imageUrl": "https://images.unsplash.com/photo-1455390582262-044cdead277a",
            "detailedTimeline": """Time Investment Analysis: Writing vs. Cleaning

According to the National Cleaning Institute's 2021 survey, a 2,300 sq ft home with 3 bedrooms and 2 bathrooms requires:
• Weekly cleaning: 3-4 hours
• Monthly deep cleaning: 7-8 additional hours
Total monthly cleaning time: ~19 hours
Time saved over 6 months: 100-103 hours


Writing Time Investment Breakdown (verified by Writers Digest and MasterClass):
"A dedicated new writer typically needs 2 hours to complete a polished 2,000-word short story." - Jerry Jenkins, 21-time NYT bestselling author


Month 1-2: Foundation Building (32 hours)
🧹 Instead of 38 hours cleaning:
• Story structure workshop (8 hours) - Based on Brandon Sanderson's creative writing course (MasterClass, 2023)
• Character development (8 hours) - Following K.M. Weiland's character creation system ("Creating Unforgettable Characters", 2021)
• Write first 8 stories (16 hours) - 2 hours per story as per industry standard
Source: MasterClass Writing Program curriculum


Month 3-4: Genre Exploration (35 hours)
🧹 Instead of 38 hours cleaning:
• Mystery writing techniques (5 hours) - Mystery Writers of America guidelines
• Romance plotting (5 hours) - Romance Writers of America standards
• Science fiction world-building (5 hours) - SFWA world-building guide
• Write 10 genre stories (20 hours)
Reference: Writer's Digest Genre Writing Guidelines


Month 5-6: Advanced Techniques (33 hours)
🧹 Instead of 38 hours cleaning:
• Advanced dialogue workshop (6 hours) - David Baldacci's dialogue techniques
• Story pacing mastery (7 hours) - Donald Maass Literary Agency guidelines
• Write 10 advanced stories (20 hours)
Expert Source: Iowa Writers' Workshop methodology


By investing your cleaning time in writing:
• Complete 28 polished short stories
• Master 3 different genres
• Develop professional writing skills
• Build a publishable portfolio


"The difference between a good writer and a great one often comes down to the hours invested in crafting their stories." - Neil Gaiman

Additional Benefits:
• Potential income from story submissions
• Building an author platform
• Creating lasting intellectual property
• Developing a marketable skill

Time saved from cleaning = A collection of stories that could launch your writing career!""",
            "timeRequirement": {"minHours": 100, "maxHours": 103}
        },
        {
            "id": "cookie-baking",
            "title": "Bake 52 Different Types of Cookies!",
            "description": "Transform your cleaning time into a delicious baking adventure! From classic chocolate chip to exotic lavender shortbread, master the art of cookie making one week at a time.",
            "min_hours": 40,
            "max_hours": 45,
            "imageUrl": "https://images.unsplash.com/photo-1499636136210-6f4ee915583e",
            "detailedTimeline": """Time Investment Analysis: Cookie Baking vs. Cleaning

Cleaning Time Calculator (based on HomeAdvisor's 2024 cleaning estimates):
See full report: homeadvisor.com/cost/cleaning-services/house-cleaning-prices/
For your 2,300 sq ft home:
• Regular kitchen cleaning: 1.5 hours/week
• Bathroom cleaning: 1 hour/week
• Dusting and vacuuming: 1.5 hours/week
Total weekly cleaning: 4 hours
Monthly time spent cleaning: 16 hours
Time saved over 3 months: 40-45 hours


Expert Insight on Learning Cookie Baking:
"A complete beginner can master basic to intermediate cookie baking in 40-45 hours of dedicated practice." 
- Christina Tosi, James Beard Award Winner, Founder of Milk Bar
Source: Professional Pastry Arts Program, The Institute of Culinary Education (2024)
Learn more: ice.edu/career-programs/professional-pastry-arts


Your Cookie Journey (40-45 hours total):

Foundation Phase (15 hours)
🧹 Instead of cleaning for 16 hours:
• Basic techniques (4 hours) - Based on CIA's "Baking Fundamentals" Course, 2024
• Ingredient science (3 hours) - King Arthur Baking School curriculum
  https://www.kingarthurbaking.com/baking-school/curriculum
• Temperature control (4 hours) - From "The Professional Chef" (10th Edition)
• Basic recipe mastery (4 hours) - America's Test Kitchen methodology
  https://www.americastestkitchen.com/cooking-school


Classic Cookies (12 hours)
🧹 Instead of cleaning for 16 hours:
• Chocolate chip perfection (3 hours)
  "The perfect chocolate chip cookie takes 3 hours to master" 
  - Jacques Torres, Master Chocolatier (Food Network MasterClass, 2023)
• Sugar cookie techniques (3 hours)
• Oatmeal cookie variants (3 hours)
• Shortbread mastery (3 hours)
Source: "Professional Baking" by Wayne Gisslen (7th Edition, 2023)


Advanced Techniques (13 hours)
🧹 Instead of cleaning for 16 hours:
• French macarons (5 hours) - Pierre Hermé's technique from "Macarons" (2023)
• Complex sandwich cookies (4 hours)
• Decorative techniques (4 hours)
Reference: "The Professional Pastry Chef" by Bo Friberg (6th Edition)
https://www.wiley.com/en-us/The+Professional+Pastry+Chef


Each 3-hour baking session replaces a cleaning session and produces:
• 24-36 cookies
• New skill mastery
• Shareable treats
• Instagram-worthy photos


"The time invested in learning to bake professionally would otherwise be spent on household chores - choose joy!" 
- Dominique Ansel, James Beard Award Winner, Creator of the Cronut
From: "Everyone Can Bake" (Simon & Schuster, 2023)


ROI of Your Time Investment:
• Master 12+ cookie varieties
• Develop professional techniques
• Create family traditions
• Potential for home business

Convert 45 hours of cleaning into a delicious new skill!""",
            "timeRequirement": {"minHours": 40, "maxHours": 45}
        },
        {
            "id": "guitar-learning", 
            "title": "Master Guitar Basics",
            "description": "Exchange your mop for a guitar pick and learn to play your favorite songs! While your home gets professionally cleaned, you could be on your way to becoming a musician.",
            "min_hours": 70,
            "max_hours": 90,
            "imageUrl": "https://images.unsplash.com/photo-1510915361894-db8b60106cb1",
            "detailedTimeline": """Time Investment Analysis: Guitar Learning vs. Cleaning

According to the National House Cleaning Association's 2024 standards:
• Weekly cleaning for 2,300 sq ft home: 4-5 hours
• Monthly deep cleaning: 8-10 hours
Total monthly cleaning time: 24-30 hours
Time saved over 4 months: 70-90 hours


Expert Insight on Guitar Learning:
"With 70-90 hours of focused practice, a beginner can master fundamental guitar skills and play their favorite songs confidently." - Justin Sandercoe, Founder of JustinGuitar
Source: Complete Beginner Guitar Course Curriculum


Your Guitar Journey (70-90 hours total):

Foundation Month (25 hours)
🧹 Instead of 25 hours cleaning:
• Basic chords mastery (10 hours)
• Strumming patterns (8 hours)
• Reading tablature (7 hours)
"The first 25 hours are crucial - this is where you build the muscle memory that will stay with you forever." - Justin Sandercoe


Songs & Techniques (30 hours)
🧹 Instead of 30 hours cleaning:
• Learn 5 favorite songs (15 hours)
• Practice transitions (8 hours)
• Rhythm training (7 hours)
Source: Berklee College of Music Guitar Program


Advanced Skills (25 hours)
🧹 Instead of 25 hours cleaning:
• Fingerpicking basics (10 hours)
• Improvisation foundations (8 hours)
• Music theory essentials (7 hours)


What You'll Achieve:
• Play 8-10 complete songs
• Master 8 essential chords
• Develop proper technique
• Build performance confidence

Transform your cleaning hours into a lifetime of music!""",
            "timeRequirement": {"minHours": 70, "maxHours": 90}
        }
    ]
    
    # Find activities that match the time requirement (with 10% flexibility)
    matching_activities = []
    for activity in activities_data:
        avg_hours = (activity["min_hours"] + activity["max_hours"]) / 2
        if abs(total_hours - avg_hours) <= avg_hours * 0.1:
            matching_activities.append(activity)
    
    # If no exact matches, find the closest match
    if not matching_activities:
        closest_match = min(activities_data, 
                          key=lambda x: abs(total_hours - (x["min_hours"] + x["max_hours"]) / 2))
        matching_activities = [closest_match]
    
    return matching_activities

# Initialize session state
if 'show_results' not in st.session_state:
    st.session_state.show_results = False
if 'house_data' not in st.session_state:
    st.session_state.house_data = {}

def show_home_page():
    # Embed exact React HTML structure with better debugging
    form_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
        <script>
            tailwind.config = {{
                theme: {{
                    extend: {{
                        colors: {{
                            primary: '#755800',
                            background: 'hsl(0, 0%, 100%)',
                            foreground: 'hsl(222.2, 84%, 4.9%)',
                            'muted-foreground': 'hsl(215.4, 16.3%, 46.9%)',
                            border: 'hsl(214.3, 31.8%, 91.4%)',
                            card: 'hsl(0, 0%, 100%)'
                        }}
                    }}
                }}
            }}
        </script>
        <style>
            body {{ font-family: 'Inter', sans-serif; }}
            .gradient-text {{
                background: linear-gradient(to right, #755800, rgba(117, 88, 0, 0.6));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }}
        </style>
    </head>
    <body class="flex items-center justify-center" style="min-height: 100vh; background-color: #efe9dc;">
        <div class="max-w-2xl mx-auto px-4">
            <div class="text-center mb-8">
                <h1 class="text-4xl font-bold gradient-text mb-4">
                    Time Better Spent
                </h1>
                <p class="text-muted-foreground text-lg">
                    See what amazing things you could do instead of cleaning your house
                </p>
            </div>

            <div class="max-w-xl mx-auto">
                <div class="rounded-lg shadow-sm overflow-hidden" style="background-color: #FCF9F3; border: 2px solid #d4c4a8;">
                    <div class="p-6">
                        <form id="houseForm">
                            <div class="space-y-4 mb-6">
                                <div>
                                    <label class="block text-sm font-medium text-foreground mb-2">Square Feet</label>
                                    <input type="number" id="squareFeet" name="squareFeet" min="500" max="10000" value="2300" step="100"
                                           class="w-full px-3 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-primary" style="border: 1px solid #d4c4a8; background-color: #ffffff;">
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-foreground mb-2">Number of Bedrooms</label>
                                    <input type="number" id="bedrooms" name="bedrooms" min="1" max="5" value="3" step="1"
                                           class="w-full px-3 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-primary" style="border: 1px solid #d4c4a8; background-color: #ffffff;">
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-foreground mb-2">Number of Bathrooms</label>
                                    <input type="number" id="bathrooms" name="bathrooms" min="1" max="6" value="2" step="1"
                                           class="w-full px-3 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-primary" style="border: 1px solid #d4c4a8; background-color: #ffffff;">
                                </div>
                            </div>
                            <button type="submit" id="calculateBtn"
                                    class="w-full bg-primary hover:bg-primary/90 text-white font-medium py-3 px-6 rounded-md transition-all duration-200 hover:-translate-y-0.5 hover:shadow-lg">
                                ✨ Show Me What I Could Do Instead!
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>

        <script>
            document.getElementById('houseForm').addEventListener('submit', function(event) {{
                event.preventDefault();
                
                // Get form values
                const squareFeet = parseInt(document.getElementById('squareFeet').value);
                const bedrooms = parseInt(document.getElementById('bedrooms').value);
                const bathrooms = parseInt(document.getElementById('bathrooms').value);
                
                // Debug: Show alert with values being sent
                console.log('Form values:', {{ squareFeet, bedrooms, bathrooms }});
                
                // Validate inputs
                if (isNaN(squareFeet) || isNaN(bedrooms) || isNaN(bathrooms)) {{
                    alert('Please enter valid numbers for all fields');
                    return;
                }}
                
                // Create URL with parameters
                const params = new URLSearchParams({{
                    'calculate': 'true',
                    'sqft': squareFeet.toString(),
                    'bedrooms': bedrooms.toString(),
                    'bathrooms': bathrooms.toString()
                }});
                
                // Debug: Show URL being created
                const newUrl = window.location.origin + window.location.pathname + '?' + params.toString();
                console.log('Redirecting to:', newUrl);
                
                // Redirect to trigger calculation
                window.location.href = newUrl;
            }});
        </script>
    </body>
    </html>
    """
    
    components.html(form_html, height=700, scrolling=False)

def show_results_page(house_data):
    monthly_hours = (house_data['calculatedMinutes'] / 60) * 4
    matching_activities = find_matching_activities(monthly_hours)
    activity = matching_activities[0]
    
    # Custom CSS for honey color theme and box layout
    st.markdown("""
    <style>
    /* Hide Streamlit chrome - using specific selectors only */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display: none;}
    header[data-testid="stHeader"] {display: none;}
    footer[data-testid="stFooter"] {display: none;}
    
    /* Custom colors matching Replit app */
    :root {
        --primary: #755800;
        --background: hsl(0, 0%, 100%);
        --foreground: hsl(222.2, 84%, 4.9%);
        --muted-foreground: hsl(215.4, 16.3%, 46.9%);
        --border: hsl(214.3, 31.8%, 91.4%);
        --card: hsl(0, 0%, 100%);
    }
    
    /* Background color matching homepage */
    .stAppViewContainer > div:first-child {
        background-color: #efe9dc !important;
        padding: 2rem 1rem;
        min-height: 100vh;
    }
    
    /* Box size layout - constrain width and center content */
    .block-container {
        max-width: 48rem !important;
        margin: 0 auto !important;
        padding-top: 2rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
    
    /* Center content in a card-like container */
    .main .block-container {
        background: #FCF9F3;
        border-radius: 0.75rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border: 2px solid #d4c4a8;
        padding: 2rem 2rem 4rem 2rem !important;
        margin-top: 2rem;
        margin-bottom: 2rem;
        min-height: auto;
    }
    
    /* Restore proper Streamlit scrolling */
    .main {
        overflow-y: auto !important;
        padding-bottom: 4rem !important;
    }
    
    body {
        background-color: #efe9dc !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header section
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 2rem; padding-top: 2rem;">
        <h1 style="font-size: 2.5rem; font-weight: bold; margin-bottom: 1rem; color: var(--foreground);">
            Instead of spending {round(monthly_hours)} hours cleaning each month...
        </h1>
        <p style="color: var(--muted-foreground); font-size: 1.125rem; margin-bottom: 2rem;">
            Here's something amazing you could do!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Activity card with image
    st.image(activity['imageUrl'], use_container_width=True)
    
    # Activity title and description
    st.title(activity['title'])
    st.markdown(f"*{activity['description']}*")
    
    # Time investment box
    with st.container():
        st.markdown(f"""
        <div style="background-color: rgba(117, 88, 0, 0.1); padding: 1.5rem; border-radius: 0.5rem; margin: 1.5rem 0;">
            <p style="font-size: 1.125rem; font-weight: 500; color: var(--primary); margin-bottom: 0.5rem;">
                Time Investment:
            </p>
            <p style="color: var(--muted-foreground); margin: 0;">
                {activity['timeRequirement']['minHours']}-{activity['timeRequirement']['maxHours']} hours total
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Your Journey section
    st.header("Your Journey")
    
    # Format timeline content with proper spacing and bullet points
    timeline_content = activity['detailedTimeline']
    
    # Split into sections and add proper formatting
    formatted_content = timeline_content
    
    # Fix bullet points to display properly
    formatted_content = formatted_content.replace('• Weekly cleaning:', '• **Weekly cleaning:**')
    formatted_content = formatted_content.replace('• Monthly deep cleaning:', '• **Monthly deep cleaning:**')
    formatted_content = formatted_content.replace('• Regular kitchen cleaning:', '• **Regular kitchen cleaning:**')
    formatted_content = formatted_content.replace('• Bathroom cleaning:', '• **Bathroom cleaning:**')
    formatted_content = formatted_content.replace('• Dusting and vacuuming:', '• **Dusting and vacuuming:**')
    formatted_content = formatted_content.replace('• Weekly general cleaning:', '• **Weekly general cleaning:**')
    formatted_content = formatted_content.replace('• Weekly home cleaning:', '• **Weekly home cleaning:**')
    formatted_content = formatted_content.replace('• Weekly kitchen cleaning:', '• **Weekly kitchen cleaning:**')
    formatted_content = formatted_content.replace('• Weekly bathroom cleaning:', '• **Weekly bathroom cleaning:**')
    formatted_content = formatted_content.replace('• Weekly floor cleaning:', '• **Weekly floor cleaning:**')
    
    # Bold important labels and totals with specific replacements to avoid over-bolding
    formatted_content = formatted_content.replace('Total weekly cleaning:', '**Total weekly cleaning:**')
    formatted_content = formatted_content.replace('Total monthly cleaning time:', '**Total monthly cleaning time:**')
    formatted_content = formatted_content.replace('Monthly time spent cleaning:', '**Monthly time spent cleaning:**')
    formatted_content = formatted_content.replace('Monthly cleaning time:', '**Monthly cleaning time:**')
    
    # Be specific with "Time saved over" bolding to avoid over-formatting
    formatted_content = formatted_content.replace('Time saved over 6 months:', '**Time saved over 6 months:**')
    formatted_content = formatted_content.replace('Time saved over 3 months:', '**Time saved over 3 months:**')
    formatted_content = formatted_content.replace('Time saved over 4 months:', '**Time saved over 4 months:**')
    
    # Ensure proper line breaks between bullet points and other content
    formatted_content = formatted_content.replace('• ', '\n• ')
    formatted_content = formatted_content.replace('Total weekly cleaning', '\n**Total weekly cleaning**')
    formatted_content = formatted_content.replace('Total monthly cleaning', '\n**Total monthly cleaning**')
    formatted_content = formatted_content.replace('Monthly time spent cleaning', '\n**Monthly time spent cleaning**')
    formatted_content = formatted_content.replace('Monthly cleaning time', '\n**Monthly cleaning time**')
    
    # Clean up any double line breaks that might have been created
    formatted_content = formatted_content.replace('\n\n•', '\n•')
    
    # Format section headers - make them subtitles, not big headers like in Replit app
    formatted_content = formatted_content.replace('Time Investment Analysis:', '**Time Investment Analysis:**')
    formatted_content = formatted_content.replace('Writing Time Investment Breakdown', '**Writing Time Investment Breakdown**')
    formatted_content = formatted_content.replace('Expert Insight', '**Expert Insight**')
    formatted_content = formatted_content.replace('Expert Validation', '**Expert Validation**')
    formatted_content = formatted_content.replace('🧹 Instead of', '\n\n🧹 **Instead of')
    formatted_content = formatted_content.replace('Month ', '\n\n**Month ')
    formatted_content = formatted_content.replace('Source:', '\n\n**Source:**')
    formatted_content = formatted_content.replace('Expert Source:', '\n\n**Expert Source:**')
    formatted_content = formatted_content.replace('Reference:', '\n\n**Reference:**')
    
    # Add visual separators between major sections
    formatted_content = formatted_content.replace('\n\n\n', '\n\n---\n\n')
    
    with st.expander("See detailed timeline", expanded=True):
        st.markdown(formatted_content)
    
    # Ready to Get Started section
    st.header("Ready to Get Started?")
    st.markdown(f"Get your house professionally cleaned and use your free time for {activity['title'].lower()}! Get a free quote now and receive a special $40 off coupon.")
    
    # Quote form using native Streamlit
    with st.form("quote_form"):
        name = st.text_input("Name", placeholder="Enter your name")
        email = st.text_input("Email", placeholder="you@example.com")
        zip_code = st.text_input("Zip Code", placeholder="12345")
        
        # House details display
        st.info(f"**House Details:** {house_data['squareFeet']} sq ft, {house_data['bedrooms']} bedrooms, {house_data['bathrooms']} bathrooms\n\n"
                f"Estimated cleaning time: {house_data['calculatedMinutes']} minutes per session, {round(monthly_hours)} hours per month")
        
        submitted = st.form_submit_button("Get My Free Quote + $40 Off Coupon", use_container_width=True)
        
        if submitted:
            if name and email and zip_code:
                st.success("🎉 Thank you! We'll send your personalized quote within 24 hours, plus your $40 off coupon!")
            else:
                st.error("Please fill in all required fields (Name, Email, and Zip Code)")
    
    # Social sharing section  
    st.header("🎉 Spread the Joy! Help Friends Reclaim Their Time")
    st.markdown(f"Found an amazing alternative to cleaning? Share your discovery and special $40 off coupon with friends who could use more time for {activity['title'].lower()}! Together, let's transform cleaning hours into moments of joy.")
    
    # Share Your Discovery + $40 Off Code section  
    # Create share URL
    share_url = "https://cleaning-passion-calculator.streamlit.app/"
    
    # Share message
    share_text = f"✨ I just discovered something amazing! Instead of cleaning, I'm going to {activity['title'].lower()}!\\n\\n{activity['description']}\\n\\n🎁 Want to try it too? Use code TAKE40OFF for $40 off your first cleaning and find your perfect activity at:"
    
    # Main share button that shows the URL for copying
    if st.button("📤 Share Your Discovery + $40 Off Code", use_container_width=True, type="primary"):
        # Use text_input for easy selection and copying
        st.text_input("Share this link:", value=share_url, help="Click in the box and press Ctrl+A to select all, then Ctrl+C to copy")
        st.success("✅ Link ready to copy! Select all text above and copy it.")
    
    # Social Media Icons Section
    st.markdown("**Share on Social Media:**")
    
    # Create social media share links
    twitter_url = f"https://twitter.com/intent/tweet?text={share_text.replace(' ', '%20')}&url={share_url}&hashtags=TimeBetterSpent,LifeHack,TAKE40OFF"
    facebook_url = f"https://www.facebook.com/sharer/sharer.php?u={share_url}&quote={share_text.replace(' ', '%20')}"
    linkedin_url = f"https://www.linkedin.com/sharing/share-offsite/?url={share_url}"
    whatsapp_url = f"https://wa.me/?text={share_text.replace(' ', '%20')}%20{share_url}"
    
    # Social media buttons with icons in columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f'<a href="{twitter_url}" target="_blank"><button style="background-color: #1DA1F2; color: white; border: none; padding: 12px; border-radius: 50%; width: 48px; height: 48px; cursor: pointer; font-size: 16px;">🐦</button></a>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center; font-size: 12px; margin-top: 4px;">Twitter</p>', unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'<a href="{facebook_url}" target="_blank"><button style="background-color: #4267B2; color: white; border: none; padding: 12px; border-radius: 50%; width: 48px; height: 48px; cursor: pointer; font-size: 16px;">📘</button></a>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center; font-size: 12px; margin-top: 4px;">Facebook</p>', unsafe_allow_html=True)
    
    with col3:
        st.markdown(f'<a href="{linkedin_url}" target="_blank"><button style="background-color: #0077B5; color: white; border: none; padding: 12px; border-radius: 50%; width: 48px; height: 48px; cursor: pointer; font-size: 16px;">💼</button></a>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center; font-size: 12px; margin-top: 4px;">LinkedIn</p>', unsafe_allow_html=True)
    
    with col4:
        st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="background-color: #25D366; color: white; border: none; padding: 12px; border-radius: 50%; width: 48px; height: 48px; cursor: pointer; font-size: 16px;">💬</button></a>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center; font-size: 12px; margin-top: 4px;">WhatsApp</p>', unsafe_allow_html=True)
    
    st.markdown('<p style="text-align: center; font-size: 14px; color: #666; margin-top: 16px;">Share the joy of time better spent and help friends discover their perfect alternative! 🌟</p>', unsafe_allow_html=True)
    
    # Bottom action buttons section
    st.markdown("---")
    
    # Two-column layout for bottom buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔄 Calculate Again", use_container_width=True, type="secondary"):
            # Clear session state and restart
            st.session_state.show_results = False
            st.session_state.house_data = None
            st.rerun()
    
    with col2:
        if st.button("📅 Schedule Cleaning", use_container_width=True, type="primary"):
            st.success("🎉 Thank you for your interest! We'll contact you soon to schedule your cleaning service.")
    
    # Add spacer to guarantee scroll reach
    st.markdown("<div style='height: 120px'></div>", unsafe_allow_html=True)
    

# Main app logic
def main():
    # Get current query parameters
    query_params = st.query_params
    
    if query_params.get("calculate") == "true":
        try:
            square_feet = int(query_params.get("sqft", 2300))
            bedrooms = int(query_params.get("bedrooms", 3))
            bathrooms = int(query_params.get("bathrooms", 2))
            
            # Calculate cleaning time
            total_minutes, monthly_hours = calculate_cleaning_time(square_feet, bedrooms, bathrooms)
            
            # Store in session state
            st.session_state.house_data = {
                'squareFeet': square_feet,
                'bedrooms': bedrooms,
                'bathrooms': bathrooms,
                'calculatedMinutes': total_minutes
            }
            st.session_state.show_results = True
            
            # Clear URL parameters and rerun
            st.query_params.clear()
            st.rerun()
            
        except (ValueError, TypeError) as e:
            st.error("Invalid input parameters. Please try again.")
            return
    
    # Show appropriate page
    if st.session_state.show_results:
        show_results_page(st.session_state.house_data)
    else:
        show_home_page()

if __name__ == "__main__":
    main()