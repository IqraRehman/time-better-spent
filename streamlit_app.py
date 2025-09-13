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
    
    activities_data = [
        {
            "id": "cookie-baking",
            "title": "Bake 52 Different Types of Cookies!",
            "description": "Transform your cleaning time into a delicious baking adventure! From classic chocolate chip to exotic lavender shortbread, master the art of cookie making one week at a time.",
            "min_hours": 40,
            "max_hours": 45,
            "imageUrl": "https://images.unsplash.com/photo-1558961363-fa8fdf82db35?w=800&h=400&fit=crop",
            "detailedTimeline": """🍪 **Your Cookie Journey (40-45 hours total)**

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
            "timeRequirement": {"minHours": 40, "maxHours": 45}
        }
    ]
    
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

# Initialize session state
if 'show_results' not in st.session_state:
    st.session_state.show_results = False
if 'house_data' not in st.session_state:
    st.session_state.house_data = {}

def show_home_page():
    # Embed exact React HTML structure with Tailwind CSS
    components.html("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
        <script>
            tailwind.config = {
                theme: {
                    extend: {
                        colors: {
                            primary: 'hsl(43, 96%, 56%)',
                            background: 'hsl(0, 0%, 100%)',
                            foreground: 'hsl(222.2, 84%, 4.9%)',
                            'muted-foreground': 'hsl(215.4, 16.3%, 46.9%)',
                            border: 'hsl(214.3, 31.8%, 91.4%)',
                            card: 'hsl(0, 0%, 100%)'
                        }
                    }
                }
            }
        </script>
        <style>
            body { font-family: 'Inter', sans-serif; }
            .gradient-text {
                background: linear-gradient(to right, hsl(43, 96%, 56%), hsl(43, 96%, 56%, 0.6));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
        </style>
    </head>
    <body class="min-h-screen bg-gradient-to-b from-primary/10 to-background p-4">
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
                        <form id="houseForm" onsubmit="submitForm(event)">
                            <div class="grid grid-cols-3 gap-4 mb-6">
                                <div>
                                    <label class="block text-sm font-medium text-foreground mb-2">Square Feet</label>
                                    <input type="number" id="squareFeet" min="500" max="10000" value="2000" step="100"
                                           class="w-full px-3 py-2 border border-border rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary">
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-foreground mb-2">Number of Bedrooms</label>
                                    <input type="number" id="bedrooms" min="1" max="5" value="3" step="1"
                                           class="w-full px-3 py-2 border border-border rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary">
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-foreground mb-2">Number of Bathrooms</label>
                                    <input type="number" id="bathrooms" min="1" max="6" value="2" step="1"
                                           class="w-full px-3 py-2 border border-border rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary">
                                </div>
                            </div>
                            <button type="submit" 
                                    class="w-full bg-primary hover:bg-primary/90 text-white font-medium py-3 px-6 rounded-md transition-all duration-200 hover:-translate-y-0.5 hover:shadow-lg">
                                ✨ Show Me What I Could Do Instead!
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>

        <script>
            function submitForm(event) {
                event.preventDefault();
                const squareFeet = document.getElementById('squareFeet').value;
                const bedrooms = document.getElementById('bedrooms').value;
                const bathrooms = document.getElementById('bathrooms').value;
                
                // Send data to Streamlit
                window.parent.postMessage({
                    type: 'calculate',
                    data: {
                        squareFeet: parseInt(squareFeet),
                        bedrooms: parseInt(bedrooms),
                        bathrooms: parseInt(bathrooms)
                    }
                }, '*');
            }
        </script>
    </body>
    </html>
    """, height=600)

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
            body {{ font-family: 'Inter', sans-serif; }}
            .prose pre {{ white-space: pre-line; }}
        </style>
    </head>
    <body class="min-h-screen bg-gradient-to-b from-primary/10 to-background p-4">
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
                            <div class="grid grid-cols-2 gap-4">
                                <div>
                                    <label class="block text-sm font-medium text-foreground mb-2">Full Name</label>
                                    <input type="text" id="name" required
                                           class="w-full px-3 py-2 border border-border rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary">
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-foreground mb-2">Email</label>
                                    <input type="email" id="email" required
                                           class="w-full px-3 py-2 border border-border rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary">
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-foreground mb-2">Zip Code</label>
                                    <input type="text" id="zip" required
                                           class="w-full px-3 py-2 border border-border rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary">
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-foreground mb-2">Phone (Optional)</label>
                                    <input type="tel" id="phone"
                                           class="w-full px-3 py-2 border border-border rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary">
                                </div>
                            </div>
                            
                            <div class="bg-primary/5 p-4 rounded-lg">
                                <p class="text-lg font-medium text-primary mb-2">House Details:</p>
                                <p class="text-muted-foreground">{house_data['squareFeet']} sq ft, {house_data['bedrooms']} bedrooms, {house_data['bathrooms']} bathrooms</p>
                            </div>
                            
                            <button type="submit" 
                                    class="w-full bg-primary hover:bg-primary/90 text-white font-medium py-3 px-6 rounded-md transition-all duration-200">
                                🎉 Get My Free Quote + $40 Off!
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
                window.parent.postMessage({{type: 'goHome'}}, '*');
            }}
        </script>
    </body>
    </html>
    """, height=1200)

# Main app logic
def main():
    # Listen for messages from embedded HTML
    if st.session_state.show_results:
        show_results_page(st.session_state.house_data)
    else:
        show_home_page()

# Handle form submission (would need additional setup for message passing)
st.sidebar.header("Controls")
if st.sidebar.button("Reset to Home"):
    st.session_state.show_results = False
    st.rerun()

# Test data for demo
if st.sidebar.button("Show Results Demo"):
    total_minutes, monthly_hours = calculate_cleaning_time(2000, 3, 2)
    st.session_state.house_data = {
        'squareFeet': 2000,
        'bedrooms': 3,
        'bathrooms': 2,
        'calculatedMinutes': total_minutes
    }
    st.session_state.show_results = True
    st.rerun()

if __name__ == "__main__":
    main()