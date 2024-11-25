import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

# Завантаження необхідних ресурсів
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Читання тексту з файлу
with open('original_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Токенізація по словам
tokens = word_tokenize(text)
print(f"Токени: {tokens}")

# Лемматизація та стеммінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]
stemmed_words = [stemmer.stem(word) for word in tokens]

print(f"\nЛемматизовані слова: {lemmatized_words}")
print(f"\nСтемінг слів: {stemmed_words}")

# Видалення стоп-слів
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in tokens if word.lower() not in stop_words]

print(f"\nСлова без стоп-слів: {filtered_words}")

# Видалення пунктуації
cleaned_words = [word for word in filtered_words if word not in string.punctuation]

print(f"\nСлова без пунктуації: {cleaned_words}")

# Запис обробленого тексту у інший файл
processed_text = ' '.join(cleaned_words)
with open('obroblen_text.txt', 'w', encoding='utf-8') as file:
    file.write(processed_text)

print("Обробка завершена. Оброблений текст записано у 'obroblen_text.txt'.")