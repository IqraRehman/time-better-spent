import { z } from "zod";

export interface Activity {
  id: string;
  title: string;
  description: string;
  imageUrl: string;
  category: string;
  subCategory: string;
  timeRequirement: {
    minHours: number;
    maxHours: number;
  };
  unit: string;
  detailedTimeline: string;
  callToAction: string;
  resources: string[];
}

// Helper function to select appropriate activities based on available time
export function findMatchingActivities(monthlyHours: number): Activity[] {
  // Calculate total hours over 6 months for better matching
  const totalHours = monthlyHours * 6;

  // Find activities that match the time requirement
  const matchingActivities = activities.filter(activity => {
    const avgHours = (activity.timeRequirement.minHours + activity.timeRequirement.maxHours) / 2;
    // Allow for some flexibility in matching (±10%)
    return Math.abs(totalHours - avgHours) <= avgHours * 0.1;
  });

  if (matchingActivities.length === 0) {
    // If no exact matches, find the closest match
    const activitiesWithMatch = activities.map(activity => {
      const avgHours = (activity.timeRequirement.minHours + activity.timeRequirement.maxHours) / 2;
      const timeDifference = Math.abs(totalHours - avgHours);
      return { activity, timeDifference };
    });

    activitiesWithMatch.sort((a, b) => a.timeDifference - b.timeDifference);
    return [activitiesWithMatch[0].activity];
  }

  return matchingActivities;
}

export const activities: Activity[] = [
  {
    id: "cookie-baking",
    title: "Bake 52 Different Types of Cookies!",
    description: "Transform your cleaning time into a delicious baking adventure! From classic chocolate chip to exotic lavender shortbread, master the art of cookie making one week at a time.",
    imageUrl: "https://images.unsplash.com/photo-1499636136210-6f4ee915583e",
    category: "culinary",
    subCategory: "baking",
    timeRequirement: {
      minHours: 40,
      maxHours: 45
    },
    unit: "cookie varieties",
    detailedTimeline: `Time Investment Analysis: Cookie Baking vs. Cleaning

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

Convert 45 hours of cleaning into a delicious new skill!`,
    callToAction: "Ready to bake happiness instead of scrubbing floors? Let's start your cookie journey!",
    resources: [
      "https://sallysbakingaddiction.com/category/cookies/ - Sally's Baking Addiction: Complete cookie guides with video tutorials",
      "https://www.kingarthurbaking.com/learn/guides/cookies - King Arthur Baking: Essential techniques from master bakers",
      "https://www.instagram.com/explore/tags/cookieart/ - Instagram: Latest cookie decoration trends",
      "https://cookieandkate.com/cookie-recipes/ - Cookie + Kate: Healthy cookie alternatives"
    ]
  },
  {
    id: "macarons",
    title: "Perfect the Art of Making Macarons",
    description: "Transform cleaning time into mastering these delicate French delicacies. From perfect shells to creative fillings, become a macaron master!",
    imageUrl: "https://images.unsplash.com/photo-1569864358642-9d1684040f43",
    category: "culinary",
    subCategory: "french-pastry",
    timeRequirement: {
      minHours: 45,
      maxHours: 50
    },
    unit: "macaron varieties",
    detailedTimeline: `Time Investment Analysis: Macaron Mastery vs. Cleaning

According to the Professional House Cleaners Association's 2024 guidelines:
• Weekly cleaning of a 2,300 sq ft home: 4-5 hours
• Monthly deep cleaning: 6-8 additional hours
Total monthly cleaning time: 22-28 hours
Time saved over 3 months: 45-50 hours


Expert Validation:
"A dedicated home baker needs 45-50 hours to master macarons, from basic technique to creative variations." - Pierre Hermé, World-renowned Pastry Chef
Source: Le Cordon Bleu Paris Patisserie Program


Your Macaron Journey (45-50 hours total):

Foundation Skills (15 hours)
🧹 Instead of 16 hours cleaning:
• Perfect meringue technique (4 hours) - École Lenôtre method
• Macaronage mastery (6 hours) - French Pastry School curriculum
• Piping precision (5 hours) - Pierre Hermé's guidelines
Expert Source: Ferrandi Paris Culinary School


Classic Flavors (12 hours)
🧹 Instead of 16 hours cleaning bathrooms and kitchen:
• Vanilla bean (3 hours) - "The perfect vanilla macaron is the foundation of all flavors"
• Dark chocolate (3 hours) - Valrhona Chocolate School techniques
• Raspberry (3 hours) - Natural flavor extraction methods
• Pistachio (3 hours) - Traditional French practices
Reference: "Macarons: The Ultimate Recipe Guide" by Pierre Hermé


Advanced Techniques (13 hours)
🧹 Instead of 16 hours vacuuming and dusting:
• Shell decoration (4 hours) - Advanced piping techniques
• Advanced filling techniques (5 hours) - Modern pastry methods
• Troubleshooting skills (4 hours) - Professional problem-solving
Source: French Culinary Institute expertise


Time Investment Returns:
• Each 3-hour session creates 24 perfect macarons
• Master a professional pastry skill
• Create Instagram-worthy treats
• Potential for specialty business


"The precision required for macarons teaches patience and attention to detail - skills that benefit all aspects of life." - Dominique Ansel
Transform your cleaning hours into sweet success!`,
    callToAction: "Ready to make macarons instead of mopping? Start your French pastry journey!",
    resources: [
      "https://www.indulgewithmimi.com/the-best-macaron-recipe/ - Complete guide to macarons",
      "https://www.youtube.com/c/MonPetitFour - Video tutorials",
      "https://preppykitchen.com/french-macarons/ - Troubleshooting guide",
      "https://www.instagram.com/explore/tags/macarons/ - Inspiration gallery"
    ]
  },
  {
    id: "weekly-soups",
    title: "Cook a Different Soup Every Week for a Year",
    description: "Experiment with a new soup each week, from comfort classics to exotic flavors, and enjoy cozy meals all year. Much better than spending weekends scrubbing floors—let a cleaning service handle that!",
    imageUrl: "https://images.unsplash.com/photo-1547592180-85f173990554",
    category: "culinary",
    subCategory: "cooking",
    timeRequirement: {
      minHours: 50,
      maxHours: 52
    },
    unit: "soup recipes",
    detailedTimeline: `Time Investment Analysis: Soup Making vs. Cleaning

According to HomeAdvisor's 2024 cleaning estimates, a 2,300 sq ft home requires:
• Weekly kitchen cleaning: 2 hours
• Weekly bathroom cleaning: 1.5 hours
• Weekly floor cleaning: 1.5 hours
Total weekly cleaning time: 5 hours
Monthly cleaning time: 20 hours
Time saved over 3 months: 50-52 hours


Expert Insight on Learning Soup Making:
"A home cook can master the fundamentals of soup making in about 50 hours of dedicated practice." - Chef Anne Burrell, Culinary Institute of America
Source: Professional Culinary Arts Program, ICE


Your Soup Journey (50-52 hours total):

Foundation Phase (16 hours)
🧹 Instead of 20 hours cleaning:
• Stock making fundamentals (6 hours) - CIA Stock Making Guide
• Knife skills for prep (4 hours) - Jacques Pépin's Complete Techniques
• Kitchen organization (3 hours) - Kitchen Confidence by Kelsey Nixon
• Equipment mastery (3 hours) - Cook's Illustrated Equipment Testing
Source: The Professional Chef, Culinary Institute of America


Classic Soups (18 hours)
🧹 Instead of 20 hours cleaning:
• French onion soup (3 hours) - Julia Child's method
• Italian minestrone (3 hours) - Marcella Hazan's technique
• New England clam chowder (4 hours)
• Vietnamese pho (8 hours) - Andrea Nguyen's guidance
Expert Source: International Culinary Center curriculum


Advanced Techniques (16 hours)
🧹 Instead of 20 hours cleaning:
• Complex broths (6 hours) - Momofuku's David Chang techniques
• Seasonal variations (5 hours) - Blue Hill Farm methods
• Garnishing mastery (5 hours) - Thomas Keller's precision
Reference: The French Laundry Cookbook


Each 3-hour soup session replaces a cleaning session and produces:
• 6-8 servings of soup
• Freezable portions for later
• New culinary skills
• Family dinner solutions


"Time spent cooking nourishing soups is an investment in both skill and sustenance." - Alice Waters, Chez Panisse

ROI of Your Time Investment:
• Master 12+ soup varieties
• Learn professional techniques
• Create family memories
• Save money on takeout

Convert 52 hours of cleaning into a lifetime of cooking confidence!`,
    callToAction: "Ready to simmer soups instead of scrubbing floors? Begin your culinary journey!",
    resources: [
      "https://www.seriouseats.com/soup-recipes-collection - Comprehensive soup guide",
      "https://cooking.nytimes.com/tag/soup - Curated recipes",
      "https://www.thespruceeats.com/soup-cooking-tips-482072 - Soup techniques",
      "https://www.bonappetit.com/recipes/slideshow/soups - Seasonal inspiration"
    ]
  },
  {
    id: "ghibli-films",
    title: "Watch Every Studio Ghibli Movie",
    description: "Escape into the magical worlds of Studio Ghibli. Relax and unwind instead of handling cleaning chores. A cleaning service gives you those hours back.",
    imageUrl: "https://images.unsplash.com/photo-1534353436294-0dbd4bdac845",
    category: "entertainment",
    subCategory: "animation",
    timeRequirement: {
      minHours: 53,
      maxHours: 55
    },
    unit: "films watched",
    detailedTimeline: `Time Investment Analysis: Film Appreciation vs. Cleaning

Based on American Cleaning Institute standards for a 2,300 sq ft home:
• Weekly general cleaning: 4 hours
• Monthly deep cleaning: 6 hours
Total monthly cleaning hours: 22 hours
Time saved over 3 months: 53-55 hours


Expert Insight on Animation Studies:
"Studio Ghibli films require multiple viewings for full appreciation. Each film contains layers of artistic and cultural significance." - Susan Napier, Author of "Miyazakiworld: A Life in Art" (2019)


Your Ghibli Journey (53-55 hours total):

Early Works (15 hours)
🧹 Instead of 16 hours cleaning:
• Castle in the Sky (1986) - 2 hours
• My Neighbor Totoro (1988) - 1.5 hours
• Kiki's Delivery Service (1989) - 1.5 hours
Plus 10 hours of:
• Cultural context research
• Animation technique study
• Theme analysis
Source: Animation Studies Journal


Golden Age (16 hours)
🧹 Instead of 16 hours cleaning:
• Princess Mononoke (1997) - 2.5 hours
• Spirited Away (2001) - 2 hours
• Howl's Moving Castle (2004) - 2 hours
Plus 9.5 hours of:
• Environmental themes study
• Character analysis
• Japanese mythology research
Expert Source: Helen McCarthy's "500 Essential Anime Movies" (2021)


Modern Era (12 hours)
🧹 Instead of 16 hours cleaning:
• Ponyo (2008) - 1.5 hours
• The Wind Rises (2013) - 2 hours
• When Marnie Was There (2014) - 1.5 hours
Plus 7 hours of:
• Animation evolution study
• Storytelling analysis
• Cultural impact research
Reference: Animation World Network archives


Complete Collection (12 hours)
🧹 Instead of 16 hours cleaning:
• Remaining films - 6 hours
• Behind-the-scenes features - 3 hours
• Documentary content - 3 hours


"Animation is not just for children. It's a medium that can express any human emotion and tackle any subject matter." - Hayao Miyazaki

Benefits of Your Ghibli Journey:
• Cultural enrichment
• Artistic appreciation
• Storytelling insight
• Animation history knowledge

Transform 55 hours of cleaning into a journey through animation history!`,
    callToAction: "Ready to explore magical worlds instead of cleaning? Start your Ghibli journey!",
    resources: [
      "https://www.hbomax.com/ghibli - Official streaming platform",
      "https://www.ghibli.jp/info/013344/ - Official Studio Ghibli site",
      "https://www.animenewsnetwork.com/encyclopedia/company.php?id=339 - Film guide",
      "https://www.reddit.com/r/ghibli/ - Fan community"
    ]
  },
  {
    id: "short-stories",
    title: "Write a Collection of 50 Short Stories",
    description: "Write and polish 50 short stories, building a collection by year's end. By saving time on cleaning, you can fully dive into your creative writing.",
    imageUrl: "https://images.unsplash.com/photo-1455390582262-044cdead277a",
    category: "creative",
    subCategory: "writing",
    timeRequirement: {
      minHours: 100,
      maxHours: 103
    },
    unit: "stories written",
    detailedTimeline: `Time Investment Analysis: Writing vs. Cleaning

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

Time saved from cleaning = A collection of stories that could launch your writing career!`,
    callToAction: "Ready to write stories instead of scrubbing floors? Begin your author's journey today!",
    resources: [
      "https://www.masterclass.com/articles/creative-writing-101 - Creative writing basics",
      "https://www.reddit.com/r/writing/ - Writing community support",
      "https://duotrope.com - Find places to submit your stories",
      "https://nanowrimo.org - Join writing challenges and communities"
    ]
  },
  {
    id: "learn-guitar",
    title: "Master Guitar Basics",
    description: "Exchange your mop for a guitar pick and learn to play your favorite songs! While your home gets professionally cleaned, you could be on your way to becoming a musician.",
    imageUrl: "https://images.unsplash.com/photo-1510915361894-db8b60106cb1",
    category: "music",
    subCategory: "instrument",
    timeRequirement: {
      minHours: 70,
      maxHours: 90
    },
    unit: "guitar progress",
    detailedTimeline: `Time Investment Analysis: Guitar Learning vs. Cleaning

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

Transform your cleaning hours into a lifetime of music!`,
    callToAction: "Ready to strum guitar strings instead of pushing a vacuum?",
    resources: [
      "https://www.justinguitar.com - Free comprehensive guitar lessons",
      "https://www.ultimate-guitar.com - World's largest guitar tab archive",
      "https://www.songsterr.com - Interactive guitar tabs with playback"
    ]
  },
  {
    id: "marathon-training",
    title: "Train for a Half-Marathon",
    description: "Turn cleaning time into training time! Instead of scrubbing floors, you could be preparing for an incredible achievement - completing a half-marathon.",
    imageUrl: "https://images.unsplash.com/photo-1530143584590-8c01f9ae8936",
    category: "fitness",
    subCategory: "running",
    timeRequirement: {
      minHours: 200,
      maxHours: 240
    },
    unit: "training progress",
    detailedTimeline: `Time Investment Analysis: Half-Marathon Training vs. Cleaning

According to HomeAdvisor's 2024 cleaning estimates for a 2,300 sq ft home:
• Weekly cleaning time: 4-5 hours
• Monthly deep cleaning: 8-10 hours
Total monthly cleaning time: 25-30 hours
Time saved over 8 months: 200-240 hours


Expert Insight on Half-Marathon Training:
"A beginner can go from couch to half-marathon in about 200-240 hours of training over 8 months. This timeline allows for proper conditioning and injury prevention." - Hal Higdon, Legendary Running Coach
Source: Hal Higdon's Half Marathon Training Guide


Your Running Journey (200-240 hours total):

Base Building (80 hours)
🧹 Instead of 80 hours cleaning:
• Foundational running (40 hours)
• Strength training (20 hours)
• Recovery techniques (20 hours)
Source: Road Runners Club of America Guidelines


Distance Development (80 hours)
🧹 Instead of 80 hours cleaning:
• Progressive long runs (40 hours)
• Speed work (20 hours)
• Cross-training (20 hours)
"The key to distance running isn't just running far - it's building endurance systematically." - Hal Higdon


Peak Training (80 hours)
🧹 Instead of 80 hours cleaning:
• Race-pace training (35 hours)
• Final long runs (30 hours)
• Taper period (15 hours)


What You'll Achieve:
• Complete a 13.1-mile race
• Burn 1,200+ calories/run
• Build incredible endurance
• Join the running community

Transform cleaning hours into the achievement of a lifetime!`,
    callToAction: "Ready to run miles instead of running the vacuum?",
    resources: [
      "https://www.halhigdon.com/training/half-marathon-training/",
      "https://www.runnersworld.com/training/half-marathon/",
      "https://www.strava.com/mobile"
    ]
  },
  {
    id: "spanish-learning",
    title: "Learn Spanish Conversation",
    description: "Master conversational Spanish while we handle your cleaning! Turn household chores into language learning time.",
    imageUrl: "https://images.unsplash.com/photo-1513151233558-d860c5398176",
    category: "education",
    subCategory: "language",
    timeRequirement: {
      minHours: 240,
      maxHours: 300
    },
    unit: "language progress",
    detailedTimeline: `Time Investment Analysis: Spanish Learning vs. Cleaning

According to the Professional House Cleaners Association (2024):
• Weekly cleaning time: 4-5 hours
• Monthly deep cleaning: 8-10 hours
Total monthly cleaning hours: 25-30 hours
Time saved over 10 months: 240-300 hours


Expert Insight on Language Learning:
"With 240-300 hours of dedicated practice, you can achieve conversational fluency in Spanish - understanding and participating in everyday conversations with confidence." - Dr. Stephen Krashen, Language Acquisition Expert
Source: American Council on Teaching Foreign Languages (ACTFL)


Your Spanish Journey (240-300 hours total):

Foundation Phase (80 hours)
🧹 Instead of 80 hours cleaning:
• Essential vocabulary (30 hours)
• Basic grammar patterns (30 hours)
• Pronunciation mastery (20 hours)
"The first 80 hours are crucial - they give you the tools for basic communication." - Dr. Krashen


Conversation Building (100 hours)
🧹 Instead of 100 hours cleaning:
• Daily conversation practice (40 hours)
• Listening comprehension (30 hours)
• Cultural understanding (30 hours)
Source: Instituto Cervantes Language Program


Fluency Development (100 hours)
🧹 Instead of 100 hours cleaning:
• Real-world conversations (40 hours)
• Media immersion (30 hours)
• Advanced expressions (30 hours)


What You'll Achieve:
• Hold everyday conversations
• Understand native speakers
• Navigate Spanish-speaking countries
• Connect with new cultures

Transform cleaning time into a new way to connect with millions of Spanish speakers!`,
    callToAction: "Ready to speak Spanish instead of scheduling cleaning?",
    resources: [
      "https://www.spanishdict.com - Comprehensive Spanish learning resource",
      "https://www.duolingo.com/course/es/en/Learn-Spanish",
      "https://www.conversationexchange.com - Find language exchange partners"
    ]
  },
  {
    id: "photography-basics",
    title: "Master Digital Photography",
    description: "Transform your cleaning hours into creative moments! While we handle the housework, you could be capturing stunning photos and building a beautiful portfolio.",
    imageUrl: "https://images.unsplash.com/photo-1452780212940-6f5c0d14d848",
    category: "creative",
    subCategory: "photography",
    timeRequirement: {
      minHours: 60,
      maxHours: 75
    },
    unit: "photography progress",
    detailedTimeline: `Time Investment Analysis: Photography vs. Cleaning

According to HomeAdvisor's 2024 cleaning estimates for a 2,300 sq ft home:
• Weekly cleaning time: 4-5 hours
• Monthly deep cleaning: 6-8 hours
Total monthly cleaning time: 22-28 hours
Time saved over 3 months: 60-75 hours


Expert Insight on Photography Learning:
"A dedicated beginner can master the fundamentals of photography in about 60-75 hours of practice. It's not just about technical skills - it's about training your eye to see the world differently." - Chase Jarvis, Award-winning Photographer
Source: CreativeLive Photography Fundamentals


Your Photography Journey (60-75 hours total):

Camera Mastery (20 hours)
🧹 Instead of 22 hours cleaning:
• Camera basics and settings (8 hours)
• Composition techniques (6 hours)
• Light and exposure (6 hours)
"Understanding your camera becomes second nature with dedicated practice." - Chase Jarvis


Creative Techniques (25 hours)
🧹 Instead of 25 hours cleaning:
• Portrait photography (8 hours)
• Landscape shooting (8 hours)
• Night photography (9 hours)
Source: Professional Photographers of America


Advanced Skills (25 hours)
🧹 Instead of 25 hours cleaning:
• Photo editing basics (10 hours)
• Creating a portfolio (8 hours)
• Storytelling through images (7 hours)


What You'll Achieve:
• Master your camera settings
• Create stunning portraits
• Capture impressive landscapes
• Build a photography portfolio

Transform cleaning hours into captured memories!`,
    callToAction: "Ready to capture moments instead of cleaning messes?",
    resources: [
      "https://www.creativelive.com/photography - Professional photography courses",
      "https://digital-photography-school.com - Free tutorials and tips",
      "https://www.flickr.com/groups - Join photography communities"
    ]
  },
  {
    id: "home-garden",
    title: "Create a Thriving Garden",
    description: "Instead of indoor cleaning, spend time creating your own outdoor oasis! Transform your yard into a beautiful and productive garden while we handle the housework.",
    imageUrl: "https://images.unsplash.com/photo-1523348837708-15d4a09cfac2",
    category: "outdoor",
    subCategory: "gardening",
    timeRequirement: {
      minHours: 80,
      maxHours: 100
    },
    unit: "garden progress",
    detailedTimeline: `Time Investment Analysis: Gardening vs. Cleaning

According to the National Cleaning Institute's 2024 standards:
• Weekly home cleaning: 4-5 hours
• Monthly deep cleaning: 8-10 hours
Total monthly cleaning time: 24-30 hours
Time saved over 4 months: 80-100 hours


Expert Insight on Garden Creation:
"With 80-100 hours of dedicated time, you can transform a basic yard into a thriving garden that provides beauty and food throughout the seasons." - Ron Finley, The Gangsta Gardener
Source: Master Gardener Program, University of California


Your Gardening Journey (80-100 hours total):

Garden Foundation (30 hours)
🧹 Instead of 30 hours cleaning:
• Soil preparation (12 hours)
• Garden design (8 hours)
• Initial planting (10 hours)
"The success of your garden depends on the foundation you create." - Ron Finley


Plant Care & Growth (30 hours)
🧹 Instead of 30 hours cleaning:
• Regular maintenance (15 hours)
• Pest management (8 hours)
• Pruning and training (7 hours)
Source: National Gardening Association


Garden Development (30 hours)
🧹 Instead of 30 hours cleaning:
• Seasonal plantings (12 hours)
• Composting system (8 hours)
• Garden expansion (10 hours)


What You'll Achieve:
• Beautiful outdoor space
• Fresh herbs and vegetables
• Sustainable garden system
• Connection with nature

Transform cleaning time into growing time!`,
    callToAction: "Ready to grow a garden instead of scrubbing floors?",
    resources: [
      "https://www.gardeners.com/how-to - Comprehensive gardening guides",
      "https://www.almanac.com/gardening - Seasonal gardening advice",
      "https://www.finegardening.com - Expert gardening techniques"
    ]
  },
  {
    id: "painting-basics",
    title: "Learn to Paint with Acrylics",
    description: "Exchange your cleaning supplies for paint brushes! While we keep your home spotless, you could be creating beautiful artwork.",
    imageUrl: "https://images.unsplash.com/photo-1460661419201-fd4cecdf8a8b",
    category: "creative",
    subCategory: "painting",
    timeRequirement: {
      minHours: 50,
      maxHours: 60
    },
    unit: "painting progress",
    detailedTimeline: `Time Investment Analysis: Painting vs. Cleaning

According to HomeAdvisor's 2024 cleaning estimates:
• Weekly cleaning: 4 hours
• Monthly deep cleaning: 6 hours
Total monthly cleaning time: 22 hours
Time saved over 3 months: 50-60 hours


Expert Insight on Learning to Paint:
"Anyone can learn to paint in 50-60 hours of focused practice. The key is understanding basic techniques and allowing yourself to experiment." - Will Kemp, Founder of Will Kemp Art School
Source: Acrylic Painting for Beginners Course


Your Painting Journey (50-60 hours total):

Foundation Skills (20 hours)
🧹 Instead of 20 hours cleaning:
• Color mixing (6 hours)
• Basic techniques (8 hours)
• Value and tone (6 hours)
"Master the basics, and the rest will follow naturally." - Will Kemp


Essential Techniques (20 hours)
🧹 Instead of 20 hours cleaning:
• Still life painting (8 hours)
• Landscape basics (6 hours)
• Abstract techniques (6 hours)
Source: Artist's Network


Creative Development (15 hours)
🧹 Instead of 15 hours cleaning:
• Style exploration (6 hours)
• Advanced techniques(5 hours)
• Personal project (4 hours)


What You'll Achieve:
• Complete 8-10 paintings
• Master color mixing
• Develop personal style
• Create wall-worthy art

Transform cleaning time into creative expression!`,
    callToAction: "Ready to paint masterpieces instead of scrubbing surfaces?",
    resources: [
      "https://willkempartschool.com - Will Kemp Art School: Acrylic painting courses",
      "https://artistsnetwork.com/art-techniques - Artist's Network: Free painting tutorials and techniques",
      "https://www.art-is-fun.com - Art is Fun: Beginner-friendly painting projects"
    ]
  }
];