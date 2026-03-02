"""
Flask server for Sentiment Analyzer web app.
"""

from flask import Flask, render_template, request

from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")


@app.route("/")
def render_index_page():
    """Render the main page."""
    return render_template("index.html")


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """
    Endpoint called by mywebscript.js with query param textToAnalyze.
    Returns a formatted sentence for the UI.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    # Extra: blank input handling (helps UI behave better)
    if text_to_analyze is None or not text_to_analyze.strip():
        return "无效输入！请在文本框输入内容。"

    response = sentiment_analyzer(text_to_analyze)
    label = response.get("label")
    score = response.get("score")

    if label is None:
        return "无效输入！请重试。"

    return "给定的文本已被识别为 {}，得分为 {}.".format(label.split("_")[1], score)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)