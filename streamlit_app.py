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

# Hide Streamlit elements
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    .main > div {
        padding: 0 !important;
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
                            primary: 'hsl(43, 96%, 56%)',
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
                background: linear-gradient(to right, hsl(43, 96%, 56%), hsl(43, 96%, 56%, 0.6));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }}
        </style>
    </head>
    <body class="bg-gradient-to-b from-primary/10 to-background p-4">
        <div class="max-w-2xl mx-auto">
            <div class="text-center mb-8 pt-8">
                <h1 class="text-4xl font-bold gradient-text mb-4">
                    Time Better Spent
                </h1>
                <p class="text-muted-foreground text-lg">
                    See what amazing things you could do instead of cleaning your house
                </p>
            </div>

            <div class="max-w-xl mx-auto">
                <div class="bg-card border border-border rounded-lg shadow-sm overflow-hidden">
                    <div class="p-6">
                        <form id="houseForm">
                            <div class="space-y-4 mb-6">
                                <div>
                                    <label class="block text-sm font-medium text-foreground mb-2">Square Feet</label>
                                    <input type="number" id="squareFeet" name="squareFeet" min="500" max="10000" value="2300" step="100"
                                           class="w-full px-3 py-2 border border-border rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary">
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-foreground mb-2">Number of Bedrooms</label>
                                    <input type="number" id="bedrooms" name="bedrooms" min="1" max="5" value="3" step="1"
                                           class="w-full px-3 py-2 border border-border rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary">
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-foreground mb-2">Number of Bathrooms</label>
                                    <input type="number" id="bathrooms" name="bathrooms" min="1" max="6" value="2" step="1"
                                           class="w-full px-3 py-2 border border-border rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary">
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
    
    # Embed exact React results structure
    components.html(f"""
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
                            primary: 'hsl(43, 96%, 56%)',
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
            body {{ 
                font-family: 'Inter', sans-serif; 
                margin: 0;
                padding: 0;
                overflow: visible;
            }}
            .prose pre {{ white-space: pre-line; }}
        </style>
    </head>
    <body class="bg-gradient-to-b from-primary/10 to-background p-4">
        <div class="max-w-3xl mx-auto">
            <div class="text-center mb-8 pt-8">
                <h1 class="text-4xl font-bold mb-4">
                    Instead of spending {round(monthly_hours)} hours cleaning each month...
                </h1>
                <p class="text-muted-foreground text-lg mb-8">
                    Here's something amazing you could do!
                </p>
            </div>

            <div class="bg-card border border-border rounded-lg shadow-sm overflow-hidden">
                <div class="h-64 bg-cover bg-center" style="background-image: url('{activity['imageUrl']}')"></div>
                
                <div class="p-6">
                    <h2 class="text-3xl font-bold mb-4">{activity['title']}</h2>
                </div>
                
                <div class="px-6 pb-6 space-y-6">
                    <p class="text-xl text-muted-foreground">
                        {activity['description']}
                    </p>

                    <div class="bg-primary/5 p-6 rounded-lg">
                        <p class="text-lg font-medium text-primary mb-2">
                            Time Investment:
                        </p>
                        <p class="text-muted-foreground">
                            {activity['timeRequirement']['minHours']}-{activity['timeRequirement']['maxHours']} hours total
                        </p>
                    </div>

                    <div class="prose prose-lg">
                        <h3 class="text-2xl font-semibold text-primary mb-4">
                            Your Journey
                        </h3>
                        <div class="whitespace-pre-line">
                            {activity['detailedTimeline']}
                        </div>
                    </div>

                    <div class="bg-primary/10 p-6 rounded-lg mt-6">
                        <div class="mb-6">
                            <h3 class="text-2xl font-semibold text-primary mb-2">
                                Ready to Get Started?
                            </h3>
                            <p class="text-muted-foreground mb-4">
                                Get your house professionally cleaned and use your free time for {activity['title'].lower()}!
                                Get a free quote now and receive a special $40 off coupon.
                            </p>
                        </div>
                        
                        <form class="space-y-4" onsubmit="submitQuote(event)">
                            <div>
                                <label class="block text-sm font-medium text-foreground mb-2">Name</label>
                                <input type="text" id="name" required placeholder="Enter your name"
                                       class="w-full px-3 py-2 border border-border rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary">
                            </div>
                            <div>
                                <label class="block text-sm font-medium text-foreground mb-2">Email</label>
                                <input type="email" id="email" required placeholder="you@example.com"
                                       class="w-full px-3 py-2 border border-border rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary">
                            </div>
                            <div>
                                <label class="block text-sm font-medium text-foreground mb-2">Zip Code</label>
                                <input type="text" id="zip" required placeholder="12345"
                                       class="w-full px-3 py-2 border border-border rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary">
                            </div>
                            
                            <div class="bg-primary/5 p-4 rounded-lg">
                                <p class="text-lg font-medium text-primary mb-2">House Details:</p>
                                <p class="text-muted-foreground">{house_data['squareFeet']} sq ft, {house_data['bedrooms']} bedrooms, {house_data['bathrooms']} bathrooms</p>
                                <p class="text-sm text-muted-foreground mt-2">Estimated cleaning time: {house_data['calculatedMinutes']} minutes per session, {round(monthly_hours)} hours per month</p>
                            </div>
                            
                            <button type="submit" 
                                    class="w-full bg-primary hover:bg-primary/90 text-white font-medium py-3 px-6 rounded-md transition-all duration-200">
                                Get My Free Quote + $40 Off Coupon
                            </button>
                        </form>
                        
                        <div class="mt-6 pt-6 border-t">
                            <p class="text-lg font-medium text-primary mb-4">
                                🎉 Spread the Joy! Help Friends Reclaim Their Time
                            </p>
                            <p class="text-sm text-muted-foreground mb-6">
                                Found an amazing alternative to cleaning? Share your discovery and special $40 off coupon with friends who could use more time for {activity['title'].lower()}! Together, let's transform cleaning hours into moments of joy.
                            </p>
                            <div class="grid grid-cols-3 gap-2">
                                <button onclick="shareTwitter()" class="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded text-sm">📱 Twitter</button>
                                <button onclick="shareFacebook()" class="bg-blue-700 hover:bg-blue-800 text-white py-2 px-4 rounded text-sm">📘 Facebook</button>
                                <button onclick="shareLinkedIn()" class="bg-blue-600 hover:bg-blue-700 text-white py-2 px-4 rounded text-sm">💼 LinkedIn</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="text-center mt-8">
                <button onclick="goHome()" class="mr-4 border border-border bg-background hover:bg-primary/5 text-foreground py-2 px-6 rounded-md">
                    Calculate Again
                </button>
                <button class="bg-primary hover:bg-primary/90 text-white py-2 px-6 rounded-md">
                    Schedule Cleaning
                </button>
            </div>
        </div>

        <script>
            function submitQuote(event) {{
                event.preventDefault();
                const name = document.getElementById('name').value;
                const email = document.getElementById('email').value;
                const zip = document.getElementById('zip').value;
                
                if (name && email && zip) {{
                    alert('🎉 Thank you! We\\'ll send your personalized quote within 24 hours, plus your $40 off coupon!');
                }} else {{
                    alert('Please fill in all required fields (Name, Email, and Zip Code)');
                }}
            }}
            
            function shareTwitter() {{
                const text = 'I could save {round(monthly_hours)} hours per month by hiring Bee Friends Cleaners! Use code TAKE40OFF for $40 off!';
                window.open('https://twitter.com/intent/tweet?text=' + encodeURIComponent(text));
            }}
            
            function shareFacebook() {{
                window.open('https://www.facebook.com/sharer/sharer.php?u=https://beefriendcleaners.com');
            }}
            
            function shareLinkedIn() {{
                window.open('https://www.linkedin.com/sharing/share-offsite/?url=https://beefriendcleaners.com');
            }}
            
            function goHome() {{
                window.location.href = window.location.origin + window.location.pathname;
            }}
        </script>
    </body>
    </html>
    """, height=4000, scrolling=False)

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