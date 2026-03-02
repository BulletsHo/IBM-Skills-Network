"""
Sentiment analysis module using Watson NLP (BERT sentiment).

The main entry point is `sentiment_analyzer(text_to_analyse)`, which returns:
    {"label": <str|None>, "score": <float|None>}
"""

from __future__ import annotations

import json
from typing import Any, Dict, Optional

import requests

_URL = (
    "https://sn-watson-sentiment-bert.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
)
_HEADERS = {
    "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
}


def sentiment_analyzer(text_to_analyse: Optional[str]) -> Dict[str, Any]:
    """
    Analyze sentiment for the given text using Watson NLP.

    Args:
        text_to_analyse: Text to analyze.

    Returns:
        A dict with keys:
          - label: e.g. "SENT_POSITIVE" / "SENT_NEGATIVE" / "SENT_NEUTRAL", or None on error
          - score: sentiment score (float), or None on error
    """
    # Blank / None input -> treat as invalid
    if text_to_analyse is None or not str(text_to_analyse).strip():
        return {"label": None, "score": None}

    payload = {"raw_document": {"text": text_to_analyse}}

    try:
        response = requests.post(_URL, json=payload, headers=_HEADERS, timeout=10)
    except requests.RequestException:
        return {"label": None, "score": None}

    try:
        formatted_response = json.loads(response.text)
    except json.JSONDecodeError:
        return {"label": None, "score": None}

    if response.status_code == 200:
        try:
            label = formatted_response["documentSentiment"]["label"]
            score = formatted_response["documentSentiment"]["score"]
            return {"label": label, "score": score}
        except (KeyError, TypeError):
            return {"label": None, "score": None}

    # Per assignment doc: invalid input may return 500; we map to None
    return {"label": None, "score": None}