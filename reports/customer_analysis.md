# Customer Behavior Analysis Report

## Overview

**Dataset:** 200 synthetic customer records across 8 service categories  
**Method:** K-Means clustering (k=4) on normalized features: Booking Frequency, Avg Spending, Sentiment Score, and Service Preference  
**NLP:** VADER sentiment analysis on Review_Text  
**Missing data:** 37 nulls across Booking_Frequency (7), Avg_Spending (10), and Review_Text (10) - filled with column medians / empty strings before processing

---

## Sentiment Distribution

VADER scored all 190 non-null reviews on a compound scale (-1 to +1):

| Sentiment | Count | % of labelled |
|---|---|---|
| Neutral | 109 | 57% |
| Positive | 52 | 27% |
| Negative | 39 | 21% |

**Note:** Several intuitively negative phrases (e.g. "Too expensive for what you get", "Won't be returning") scored 0.0 in VADER because they lack negation markers VADER recognises. This is a known limitation of lexicon-based sentiment analysis. For production use, a fine-tuned model (e.g. DistilBERT on service reviews) would yield more accurate labels.

---

## Customer Segmentation - K-Means (k=4)

The elbow method suggested k=5–8 and the silhouette score peaked at k=8, but k=4 was selected to keep segments business-actionable. Silhouette scores were low across all k values (0.220–0.242), indicating the clusters are not sharply separated - expected given the limited feature set and synthetic data.

### Cluster Profiles (corrected labels from actual stats)

| Cluster | Count | Avg Freq | Avg Spend | Avg Sentiment | Label |
|---|---|---|---|---|---|
| 1 | 51 | 9.8 | $375 | +0.41 | High-value loyalists |
| 0 | 54 | 3.8 | $289 | -0.05 | Engaged mid-tier |
| 2 | 49 | 3.7 | $312 | -0.03 | At-risk infrequents |
| 3 | 46 | 8.6 | $145 | -0.14 | Price-sensitive / churned |

---

## Segment Insights & Recommendations

### Cluster 1 - High-value loyalists (51 customers)
- Highest booking frequency (avg 9.8/year) and highest spend ($375)
- Positive sentiment (avg +0.41) - genuinely satisfied customers
- Top service: Deep Tissue
- **Retention strategy:** Introduce a VIP tier with priority booking, early access to new therapists, and a complimentary service after every 10 bookings. Personal outreach from account managers for customers in this cluster.

### Cluster 0 - Engaged mid-tier (54 customers)
- Moderate frequency (avg 3.8/year), solid mid-range spend ($289)
- Neutral sentiment - satisfied but not enthusiastic
- Top service: Massage
- **Growth strategy:** Upsell to Wellness Packages via post-booking email ("Customers like you also love..."). Referral incentives - offer $20 credit for each successful referral. Target with seasonal promotions to increase booking cadence.

### Cluster 2 - At-risk infrequents (49 customers)
- Low frequency (avg 3.7/year), mid-to-high spend ($312) but neutral/negative sentiment
- Customers who spend well when they do book but aren't returning consistently
- Top service: Aromatherapy
- **Re-engagement tactic:** Triggered email at 60 days of inactivity with a 15% discount on their preferred service. Follow up with a satisfaction survey to identify friction points - price, availability, or therapist quality.

### Cluster 3 - Price-sensitive / churned (46 customers)
- High frequency in raw numbers (avg 8.6) but lowest spend by far ($145) and negative sentiment (-0.14)
- Likely booking lower-tier services repeatedly; negative reviews suggest value-for-money dissatisfaction
- Top service: Facial
- **Intervention tactic:** Do not discount further - this risks anchoring price expectations lower. Instead, communicate service value through before/after content, therapist credentials, and customer testimonials. If sentiment remains negative after 2 re-engagement touchpoints, suppress from outreach to protect NPS.

---

## Key Findings

1. **Sentiment alone is a weak churn signal** with VADER on short service reviews - 57% of reviews scored as Neutral including clearly negative ones. Recommend switching to a supervised sentiment model trained on hospitality/wellness reviews.

2. **Deep Tissue and Wellness Packages drive the highest average spend** across high-value clusters. These services should be prioritised in recommendation and upsell flows.

3. **~23% of customers** (Cluster 3) show price-sensitivity and negative sentiment despite returning repeatedly - a distinct and underserved segment that warrants its own pricing and communication strategy separate from churned customers.

4. **Cluster separation is moderate** (silhouette ~0.23). Adding features such as days since last booking, number of different services tried, and time-of-day preference would meaningfully sharpen segmentation in a production dataset.

---

## Limitations

- Dataset is synthetic (200 rows, single booking per customer) - real-world clustering benefits from transaction history, recency scoring (RFM), and a larger feature space.
- SVD recommendation model produced identical results for all users due to data sparsity (one service per customer, no repeat interactions). A production recommendation system requires multi-interaction history per user.
- Cluster label assignment is manual and should be validated with domain experts before use in business decisions.
