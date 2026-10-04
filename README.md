# Text Similarity System

A web-based Natural Language Processing application that compares two text documents and calculates their similarity using TF-IDF vectorization and cosine similarity.

## Features

* Compare two text documents
* Calculate similarity percentage
* Uses TF-IDF text representation
* Uses cosine similarity for comparison
* Displays an easy-to-understand similarity status
* Visual similarity progress bar
* Simple and responsive web interface

## Technologies Used

* Python
* Flask
* Scikit-learn
* HTML5
* CSS3
* TF-IDF
* Cosine Similarity

## Project Structure

```text
Text-Similarity-System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## Installation

Open a terminal inside the project folder and run:

```bash
pip install -r requirements.txt
```

## Running the Application

Run the following command:

```bash
python app.py
```

The application will start at:

```text
http://127.0.0.1:5000
```

Open the address in a web browser.

## How It Works

1. The user enters two different texts.
2. The application receives both texts through Flask.
3. TF-IDF converts the text documents into numerical vectors.
4. Cosine similarity compares the two vectors.
5. The similarity score is converted into a percentage.
6. The system displays the percentage and similarity category.

## Similarity Categories

| Similarity | Category           |
| ---------- | ------------------ |
| 80% – 100% | Highly Similar     |
| 50% – 79%  | Moderately Similar |
| 20% – 49%  | Slightly Similar   |
| 0% – 19%   | Mostly Different   |

## Example

### Text 1

```text
Natural language processing helps computers understand human language.
```

### Text 2

```text
Natural language processing allows computers to understand human language.
```

### Example Result

```text
Similarity: 80%
Status: Highly Similar
```

The exact percentage depends on the words present in the input texts.

## Applications

Text similarity can be used in:

* Plagiarism detection
* Document comparison
* Duplicate content detection
* Search engines
* Information retrieval
* Question-answering systems
* Recommendation systems
* Document classification

## Purpose

This project demonstrates how Natural Language Processing and machine learning techniques can be used to measure the similarity between two textual documents.

## Note

The similarity score is based mainly on the words and their importance in the two documents. It should be treated as a basic text-similarity measure rather than a complete plagiarism-detection system.

## Author

B.E. CSE Student
