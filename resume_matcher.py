import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Download necessary NLTK data (run once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

def preprocess_text(text):
    """
    Preprocess the input text by:
    - Converting to lowercase
    - Removing punctuation
    - Tokenizing into words
    - Removing stopwords
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize into words
    words = word_tokenize(text)
    
    # Get English stopwords
    stop_words = set(stopwords.words('english'))
    
    # Remove stopwords
    filtered_words = [word for word in words if word not in stop_words]
    
    return filtered_words

def extract_keywords(text):
    """
    Extract keywords from the text by preprocessing and returning unique words.
    For simplicity, all preprocessed words are considered keywords.
    """
    preprocessed = preprocess_text(text)
    # Return unique keywords
    return set(preprocessed)

def calculate_match_score(resume_keywords, job_keywords):
    """
    Calculate the match score based on common keywords.
    Score is the percentage of job keywords present in resume.
    """
    if not job_keywords:
        return 0.0
    
    matched = resume_keywords.intersection(job_keywords)
    score = (len(matched) / len(job_keywords)) * 100
    return score, matched, job_keywords - matched

def main():
    # Sample inputs (in a real application, these could be read from files or user input)
    resume_text = """
    I am a software engineer with experience in Python, Java, and web development.
    I have worked on machine learning projects and data analysis.
    Skills include programming, problem-solving, and teamwork.
    """
    git
    job_description_text = """
    We are looking for a software engineer proficient in Python, Java, and C++.
    Experience in machine learning and data science is required.
    Strong programming skills and ability to work in a team are essential.
    """
    
    # Extract keywords
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_description_text)
    
    # Calculate match score
    score, matched, missing = calculate_match_score(resume_keywords, job_keywords)
    
    # Display results
    print("Matched Keywords:", list(matched))
    print("Missing Keywords:", list(missing))
    print(f"Final Match Score: {score:.2f}%")

if __name__ == "__main__":
    main()