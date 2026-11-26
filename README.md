# News Headline Summariser
#### Video Demo:  <URL HERE>
#### Description:

### What it is
News Headline Summariser is a command-line Python application that fetches live news headlines from an RSS feed, cleans the text, prints a numbered list of stories directly to the terminal, and archives the cleaned headlines into a date-stamped text file (`news_<date>.txt`). I chose this project because checking multiple news websites every day is time-consuming and cluttered with ads. This tool is built for anyone—students, developers, or daily readers—who wants a fast, distraction-free snapshot of current events right from their terminal while automatically keeping a daily log of headlines.

---

### Files

* **`project.py`**: Contains the core logic of the application, utilizing `feedparser` to parse the RSS XML data and Python's built-in `datetime` module to generate date-stamped filenames.
  * `main()`: Orchestrates the program flow by calling the functions to fetch, clean, display, and save the headlines.
  * `get_headlines()`: Connects to the configured RSS feed URL using `feedparser` and extracts the raw entry titles into a list.
  * `clean_headline()`: Takes a raw headline string and strips leading and trailing whitespace.
  * `display()`: Iterates through the cleaned headlines and prints them to the console as a cleanly numbered list (`1. ...`, `2. ...`).
  * `save_to_file()`: Writes the un-numbered headlines, one per line, into a `news_<date>.txt` file for archival.

* **`test_project.py`**: Uses `pytest` to verify the core functionality across three unit tests: one checking `clean_headline()` with messy whitespace strings, one verifying `save_to_file()` creates a file properly, and one testing `get_headlines()` to ensure it returns a populated list. The `get_headlines()` test requires an active internet connection to reach the live RSS feed, which means the test suite will fail if run offline or if the external feed experiences downtime.

* **`requirements.txt`**: Lists the external dependencies needed to run and test the project—specifically `feedparser` for handling RSS feeds and `pytest` for running the test suite.

---

### Design choices

* **Modular Functions**: Instead of writing everything inside a single `main()` block, I separated fetching, cleaning, displaying, and file-writing into distinct helper functions. This kept each step isolated and made debugging much easier when separating network issues from formatting bugs.
* **File Writing Mode (`"w"`)**: I chose `"w"` (write) mode rather than `"a"` (append) mode in `save_to_file()`. If the program is run multiple times on the same day, `"w"` mode overwrites the existing `news_<date>.txt` file with the latest snapshot of headlines rather than duplicating stories that were already saved earlier in the day.
* **RSS Feed Debugging**: Early in development, my initial RSS feed URL returned an empty list with no error message. By running a quick diagnostic check on the raw output of `get_headlines()`, I realized `feedparser` fails silently on dead or invalid feeds—returning an empty entries list instead of raising an exception. Switching to a verified, active RSS feed URL immediately resolved the issue and populated the list.
* **Text Cleaning**: Using `.strip()` in `clean_headline()` ensures clean spacing by removing leading and trailing whitespace from each headline. In the future, I would expand this function using regular expressions or `html.unescape()` to clean up encoded HTML entities (like `&amp;` or `&#39;`).

---

### Limitations and next steps

Because the program relies on a live RSS URL, running it offline results in an empty headline list and an empty output file without warning the user. In the next version, I would add an empty-list check in `main()` to alert the user when no stories can be retrieved, include exact timestamps inside the saved file so multiple runs per day can be tracked, and allow users to pass custom RSS feed URLs as command-line arguments.
