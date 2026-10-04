from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)


def calculate_similarity(text1, text2):
    documents = [text1, text2]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return round(similarity[0][0] * 100, 2)


def get_result(percentage):
    if percentage >= 80:
        return "Highly Similar"
    elif percentage >= 50:
        return "Moderately Similar"
    elif percentage >= 20:
        return "Slightly Similar"
    else:
        return "Mostly Different"


@app.route("/", methods=["GET", "POST"])
def index():
    text1 = ""
    text2 = ""
    similarity = None
    result = None

    if request.method == "POST":
        text1 = request.form.get("text1", "").strip()
        text2 = request.form.get("text2", "").strip()

        if text1 and text2:
            similarity = calculate_similarity(text1, text2)
            result = get_result(similarity)

    return render_template(
        "index.html",
        text1=text1,
        text2=text2,
        similarity=similarity,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)
