# 📉 Customer Churn Analysis – Telco Dataset

This project analyzes customer churn behavior using IBM’s Telco dataset. The goal is to uncover key factors behind customer churn and propose actionable strategies to help telecom companies retain customers.

---

## 🎯 Objective

To identify patterns in customer attrition and provide data-backed business recommendations that can reduce churn and improve customer loyalty.

---

## 📊 Key Insights

| Metric | Segment | Churn Rate | Insight |
|--------|---------|------------|---------|
| **Contract Type** | Month-to-month | 42.7% | Short-term users are highly likely to churn |
| | One-year | 11.3% | Longer commitment reduces churn |
| | Two-year | 2.8% | Most loyal customers |
| **Tenure** | 0–6 months | 53.3% | New users churn the most |
| | 48–72 months | 9.5% | Long-term users are highly retained |
| **Monthly Charges** | Churned: ₹74.44 | Retained: ₹61.31 | Higher charges linked to higher churn |
| **Payment Method** | Electronic Check: 45.3% | Credit Card/Bank Transfer: ~15% | Manual billing correlates with higher churn |

---

## 🧠 Business Recommendations

1. **Promote Long-Term Contracts**  
   Offer discounts or perks to encourage one-year or two-year plans.

2. **Improve Onboarding for New Customers**  
   Launch welcome journeys, NPS surveys, and early engagement campaigns.

3. **Incentivize AutoPay**  
   Provide cashback or discounts for enrolling in AutoPay to reduce churn linked to manual billing.

4. **Launch Loyalty Programs for High-Value Customers**  
   Tier-based rewards and anniversary credits to retain higher-paying users.

5. **Bundle Add-On Services**  
   Promote OnlineSecurity and TechSupport via trials or bundles to increase retention.

6. **Expand OTT Bundles & Entertainment Offers**  
   Users with streaming services show lower churn rates.

---

## 📈 Visualizations

| Insight | Chart |
|--------|-------|
| Churn by Contract Type | ![Contract Type](images/churn_by_contract.png) |
| Monthly Charges Distribution | *(add when available)* |
| Churn by Tenure Group | *(add when available)* |

---

## 🧪 Tools & Technologies

- Python (Pandas, NumPy, Seaborn, Matplotlib)
- Jupyter Notebook
- Excel (for preliminary views)
- [IBM Telco Churn Dataset on Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

---
## 📁 Repository Structure
customer-churn-analysis/
├── notebooks/ churn-analysis.ipynb
├── images/ # Visualizations and graphs
├── data/telco_customer_churn.csv CSV dataset
├── README.md # Project summary and insights
├── requirements.txt # List of Python libraries

---

## 📂 Dataset Description

- **Churn**: Whether the customer left in the last month
- **Services**: Internet, phone, security, streaming, etc.
- **Account Info**: Contract type, payment method, billing type, charges

This dataset is ideal for practicing **classification models**, **EDA**, and **customer retention strategies**.

---

## ⚖ License

This project is open-source under the [MIT License](LICENSE). Dataset credit to IBM and [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn).


---

## 🙌 Let’s Connect

If you have suggestions, feedback, or would like to collaborate — feel free to reach out via [LinkedIn](https://www.linkedin.com/in/harshitraman/)) or open an issue on this repo.

