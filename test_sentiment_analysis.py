"""
Unit tests for sentiment_analyzer.
"""

import unittest

from SentimentAnalysis.sentiment_analysis import sentiment_analyzer


class TestSentimentAnalyzer(unittest.TestCase):
    """Unit tests for the sentiment_analyzer function."""

    def test_sentiment_analyzer(self) -> None:
        """Test positive/negative/neutral labels."""
        result_1 = sentiment_analyzer("I love working with Python")
        self.assertEqual(result_1["label"], "SENT_POSITIVE")

        result_2 = sentiment_analyzer("I hate working with Python")
        self.assertEqual(result_2["label"], "SENT_NEGATIVE")

        result_3 = sentiment_analyzer("I am neutral on Python")
        self.assertEqual(result_3["label"], "SENT_NEUTRAL")


if __name__ == "__main__":
    unittest.main()