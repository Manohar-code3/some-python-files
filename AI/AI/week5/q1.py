import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from tkinter import *

# Sample tourist data (you would typically collect this from various sources)
data = pd.DataFrame({
    'Destination': ['Paris', 'London', 'Rome', 'New York', 'Tokyo'],
    'Description': ['City of Love', 'Historic City', 'Eternal City', 'The Big Apple', 'Vibrant Metropolis'],
})

# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(data['Description'])

# Calculate cosine similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Create a Tkinter GUI for user interaction
def recommend():
    user_input = entry.get()
    if user_input:
        idx = data[data['Destination'].str.lower() == user_input.lower()].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:4]  # Top 3 similar destinations
        recommended_destinations = [data['Destination'][i[0]] for i in sim_scores]
        result_label.config(text=f"Recommended Destinations: {', '.join(recommended_destinations)}")
    else:
        result_label.config(text="Please enter a destination.")

# Create the main GUI window
window = Tk()
window.title("Tourist Recommender")

label = Label(window, text="Enter a destination:")
label.pack(pady=10)

entry = Entry(window)
entry.pack(pady=5)

recommend_button = Button(window, text="Recommend", command=recommend)
recommend_button.pack(pady=5)

result_label = Label(window, text="")
result_label.pack(pady=10)

window.mainloop()
