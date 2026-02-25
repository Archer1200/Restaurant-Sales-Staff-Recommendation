# Restaurant-Sales-Staff-Recommendation
---
**Folder Structure**
```
Restaurant-Sales-Staff-Recommendation/
│
├── Intership project/
│   ├── RSFASR.ipynb
│   ├── restaurant_sales.csv
│   ├── test.py
│
├── .github/workflows/
├── README.md
```
1.**Clone the Repository**
```
git clone https://github.com/your-username/Restaurant-Sales-Staff-Recommendation.git
cd Restaurant-Sales-Staff-Recommendation
```

2.**Create Virtual Environment (Optional but Recommended)**
```
python -m venv venv
venv\Scripts\activate   # Windows
```
3.**Install Dependencies**
```
pip install streamlit pandas numpy scikit-learn
```
4.**Run the Application**
```
streamlit run "Intership project/test.py"
```
**The app will open in your browser.**

**How It Works**
```
1.Upload historical restaurant sales data.**
2.Data preprocessing:
  -Convert Date into DayOfWeek
  -Encode Weather
  -Convert Holiday (Yes/No → 1/0)
3.Train Random Forest model.
4.Predict future sales.
5.Calculate required staff.
6.Download staff planning CSV file.
```
** Future Improvements**
```
  -Add real weather API integration
  -Add holiday calendar integration
  -Deploy on Streamlit Cloud
  -Add interactive charts
  -Improve UI/UX design
```

**License**
```
This project is for educational and internship purposes.
```
  
---


