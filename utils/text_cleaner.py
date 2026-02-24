import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

STOPWORDS = set(stopwords.words("english"))


def clean_text(text):
    """
    Basic cleaning:
    - Remove citations like [1], (Smith, 2020)
    - Remove extra spaces
    - Normalize text
    """
    # Remove citation patterns
    text = re.sub(r"\[[0-9]+\]", "", text)
    text = re.sub(r"\([A-Za-z]+,\s?[0-9]{4}\)", "", text)

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def remove_references_section(text):
    """
    Removes references/bibliography section from paper.
    """
    patterns = ["references", "bibliography"]

    lower_text = text.lower()

    for pattern in patterns:
        index = lower_text.find(pattern)
        if index != -1:
            return text[:index]

    return text