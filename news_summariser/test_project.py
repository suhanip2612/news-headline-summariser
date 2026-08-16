from project import clean_headline, get_headlines, save_to_file
import os, datetime

def test_clean_headline():
    assert clean_headline("   HIIIII SUHANI     PATEL    HERE") == "HIIIII SUHANI PATEL HERE"

def test_get_headlines():
    headlines = get_headlines()
    assert isinstance(headlines, list)
    assert all(isinstance(h, str) for h in headlines)

def test_save_to_file():
    save_to_file(["Test Headline"]
    filename=f"news_{datetime.date.today()}.txt"
    assert os.path.exosts(filename)
