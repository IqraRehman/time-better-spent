# Time Better Spent - Streamlit Version

A Python Streamlit application that calculates how much time you spend cleaning your home and suggests alternative activities you could do instead.

Built for Bee Friends Cleaners to help customers see the value of professional cleaning services.

## Features

- **House cleaning time calculator** based on square footage and rooms
- **Alternative activity suggestions** with time comparisons and expert citations
- **Quote request system** with form validation
- **Social sharing functionality** with discount codes
- **Responsive design** that works on mobile, tablet, and desktop
- **Expert testimonials** and detailed activity timelines

## Live Demo

The app is ready to deploy on Streamlit Cloud!

## Quick Start

### Option 1: Deploy to Streamlit Cloud (Recommended)

1. **Fork the GitHub Repository**: https://github.com/IqraRehman/time-better-spent
2. **Go to Streamlit Cloud**: https://share.streamlit.io/
3. **Connect your GitHub account**
4. **Deploy the app** by selecting:
   - Repository: `your-username/time-better-spent`
   - Branch: `main`
   - Main file path: `streamlit_app.py`
5. **Click Deploy!**

### Option 2: Run Locally

```bash
# Install dependencies
pip install streamlit pandas requests

# Run the app
streamlit run streamlit_app.py
```

The app will open at `http://localhost:8501`

## Activities Included

The app includes 8 comprehensive activity suggestions:

1. **🍪 Bake 52 Different Types of Cookies** (40-45 hours)
2. **🧁 Master French Macarons** (25-30 hours)  
3. **🍲 Master 26 Soul-Warming Soups** (35-40 hours)
4. **✍️ Write 50 Short Stories** (100-103 hours)
5. **🎸 Master Guitar Basics** (70-90 hours)
6. **🇪🇸 Learn Spanish Conversation** (240-300 hours)
7. **🏃‍♀️ Train for Half-Marathon** (200-240 hours)
8. **📸 Master Digital Photography** (60-80 hours)

Each activity includes:
- Expert citations and testimonials
- Detailed learning timelines
- Skill progression breakdowns
- Resource recommendations

## How It Works

1. **Input your house details**: square footage, bedrooms, bathrooms
2. **Get your cleaning time calculation**: Based on industry standards (750 sq ft per hour + 20 mins per bedroom/bathroom)
3. **See matching activities**: Algorithm matches your available time to suitable activities
4. **Request a quote**: Built-in form for lead generation
5. **Share your results**: Social media integration with discount codes

## Tech Stack

- **Frontend**: Streamlit (Python web framework)
- **Styling**: Custom CSS for professional appearance
- **Data**: Comprehensive activity database with expert citations
- **Forms**: Native Streamlit form components
- **Deployment**: Ready for Streamlit Cloud

## Business Features

- **Lead generation** through quote request forms
- **Social sharing** with embedded discount codes (TAKE40OFF)
- **Professional branding** for Bee Friends Cleaners
- **Mobile-responsive** design
- **Expert testimonials** for credibility

## Deployment Notes

This Streamlit version replicates all the core functionality of the original React/Express application but is optimized for the Streamlit ecosystem and Streamlit Cloud deployment.

The app is designed to be deployed at `https://your-app-name.streamlit.app/` through Streamlit Cloud's free hosting.

---

Built with ❤️ for better time management and cleaner homes!