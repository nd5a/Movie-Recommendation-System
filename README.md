# Movie-Recommendation-System![code](https://github.com/nd5a/Movie-Recommendation-System/assets/128470872/076b09cc-2b09-4ccf-97df-cb51016a1d6b)

---

# 🎬 Movie Recommendation System  

## 📌 Overview  
This project is a **Movie Recommendation System** built using **Python and machine learning**. The system uses **content-based filtering** and **cosine similarity** to suggest similar movies based on user input.  

## 📂 Project Files  
```
Movie-Recommendation-System/
│── movie_recommendation_system.ipynb   # Jupyter Notebook with the recommendation logic
│── dataset/                            # Raw movie dataset (if applicable)
│── artifacts/                          # Preprocessed files (pickled data)
│   ├── movie_list.pkl                  # List of movies in pickle format
│   ├── similarity.pkl                   # Precomputed similarity matrix
│── requirements.txt                     # Dependencies
│── README.md                            # Project documentation
│── .gitignore                           # Ignore unnecessary files
```

## 🛠️ Installation & Setup  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/your-username/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### **2️⃣ Install Dependencies**  
Ensure you have **Python 3.8+** installed. Then, install required libraries:  
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the Jupyter Notebook**  
Start Jupyter Notebook in your terminal:  
```sh
jupyter notebook
```
Then open `movie_recommendation_system.ipynb` and **run all cells**.  

## 🧠 How It Works  
1️⃣ **Data Processing**: The system reads movie data from a CSV file.  
2️⃣ **Feature Engineering**: Text descriptions are vectorized using **TF-IDF**.  
3️⃣ **Similarity Computation**: A **cosine similarity matrix** is built for recommendations.  
4️⃣ **Movie Recommendation**: When a user selects a movie, the system finds and returns **top 5 similar movies**.  

## 🏗️ Technologies Used  
- **Python** 🐍  
- **Pandas** 📊  
- **Scikit-learn** 🤖  
- **Jupyter Notebook** 📒  
- **TMDB API** 🌍 (for fetching movie posters)  

## 💡 Future Improvements  
🔹 Add **collaborative filtering** (based on user ratings)  
🔹 Implement a **hybrid recommendation system**  
🔹 Deploy the model as a **web app using Streamlit**  

## 🤝 Contributing  
Want to improve this project? Feel free to **fork & submit a PR**!  

---
