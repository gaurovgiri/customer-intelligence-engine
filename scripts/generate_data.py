"""Generate synthetic customer booking and sentiment data for experimentation."""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)
random.seed(42)
n = 200

services = ["Massage","Facial","Wellness Package","Body Scrub","Manicure","Hot Stone Therapy","Aromatherapy","Deep Tissue"]

positive = [
    "Loved every minute!", "Absolutely fantastic — will book again.",
    "My therapist was exceptional.", "Best massage I've ever had.",
    "Highly recommend to everyone.", "Left feeling completely renewed.",
    "Such a relaxing experience.", "Worth every cent — flawless service.",
    "Incredible attention to detail.", "The staff made me feel so welcome.",
    "Perfect from start to finish.", "Going to make this a monthly ritual.",
    "Transformed my whole week.", "Exactly what I needed.", "Five stars, no question.",
    "Exceeded all my expectations.", "Professional and deeply relaxing.",
    "I floated out of there.", "Genuinely the best in the city.",
    "Booked again before I even left."
]
neutral = [
    "It was okay, nothing special.", "Decent service, a bit pricey.",
    "Average — met expectations.", "Fine but not remarkable.",
    "Would consider coming back.", "Good enough for the price.",
    "Neither great nor bad.", "Pretty standard experience.",
    "I've had better, I've had worse.", "Reasonable, but room to improve.",
    "Not bad, just not memorable.", "Satisfactory overall.",
    "Could improve the ambience.", "Middle of the road service."
]
negative = [
    "Too expensive for what you get.", "Waited 20 mins past my booking time.",
    "Therapist seemed distracted.", "Not as described — disappointing.",
    "Would not recommend at this price.", "Below my expectations.",
    "The room was too cold.", "Felt rushed throughout.",
    "Poor communication from staff.", "Won't be returning.",
    "Quality has dropped since my last visit.", "Overpriced for average work.",
    "Very underwhelming experience.", "Wouldn't recommend to a friend.",
    "Left more stressed than when I arrived."
]

start = datetime(2023, 1, 1)

def assign_segment(freq, spend, days_since):
    """Assign customer segment based on booking frequency, spend, and recency."""
    if freq >= 8 and spend >= 250:
        return "High-value"
    elif freq >= 5 and days_since <= 90:
        return "Loyal"
    elif freq <= 2 or days_since >= 270:
        return "Churned"
    else:
        return "At-risk"

def assign_review(seg):
    """Sample review text and sentiment according to customer segment."""
    if seg == "High-value":
        return random.choice(positive), "Positive"
    elif seg == "Loyal":
        return random.choice(positive if random.random() < 0.7 else neutral), ("Positive" if random.random() < 0.7 else "Neutral")
    elif seg == "At-risk":
        pool = neutral + negative
        r = random.choice(pool)
        return r, ("Neutral" if r in neutral else "Negative")
    else:  # Churned
        return random.choice(negative), "Negative"

rows = []
ref_date = datetime(2024, 3, 31)

for i in range(n):
    freq = np.random.randint(1, 13)
    spend = round(np.random.uniform(35, 520), 2)
    svc = random.choice(services)
    days_ago = int(np.random.randint(5, 400))
    last_activity = (ref_date - timedelta(days=days_ago)).strftime("%Y-%m-%d")
    seg = assign_segment(freq, spend, days_ago)
    review, sent = assign_review(seg)

    # inject ~5% nulls
    if random.random() < 0.05:
        freq = None
    if random.random() < 0.05:
        spend = None
    if random.random() < 0.05:
        review = None
        sent = None

    rows.append({
        "Customer_ID": 1001 + i,
        "Booking_Frequency": freq,
        "Avg_Spending": spend,
        "Preferred_Service": svc,
        "Last_Activity": last_activity,
        "Review_Text": review,
        "Sentiment": sent,
        "Segment": seg
    })

df = pd.DataFrame(rows)
df.to_csv("data/raw/customer_data.csv", index=False)
print(df.head(10).to_string())
print(f"\nShape: {df.shape}")
print(f"\nSegment distribution:\n{df['Segment'].value_counts()}")
print(f"\nSentiment distribution:\n{df['Sentiment'].value_counts()}")
print(f"\nNulls:\n{df.isnull().sum()}")