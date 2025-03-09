import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression  # Zmieniamy na model klasyfikacji
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

# Wczytanie danych
df = pd.read_csv(r'C:\Users\Piotr Staszak\RepoKwiatek\RepoKwiatek\PANDAS 09_03_25\bug_reports.csv')

print(df)

# Tworzenie kolumny tekstowej do analizy
df['Text'] = df['Summary'] + " " + df['Description']

# Konwersja tekstu na wektory za pomocą TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
x = vectorizer.fit_transform(df['Text'])  # x to cechy (wektory TF-IDF)

# Etykiety do klasyfikacji
y = df["Category"]

# Zakodowanie etykiet (jeśli są tekstowe)
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)  # Kodowanie etykiet na liczby

# Podział na zbiór treningowy i testowy
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Trenowanie modelu klasyfikacji (LogisticRegression zamiast LinearRegression)
model = LogisticRegression(max_iter=1000)  # Dodajemy max_iter, żeby model miał wystarczająco dużo iteracji
model.fit(x_train, y_train)

# Predykcja na zbiorze testowym
y_pred = model.predict(x_test)

# Ocena modelu
#print(classification_report(y_test, y_pred))  # Ocena wyników

# sprawdzenie nowego bledu
new_bug = ["A random issue with login."]
new_bug_vectorized = vectorizer.transform(new_bug)
prediction_category = model.predict(new_bug_vectorized)

print(prediction_category[0])