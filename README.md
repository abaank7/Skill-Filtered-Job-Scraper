# 🕸️ TimesJobs Python Scraper

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-00599C?style=flat-square)
![Requests](https://img.shields.io/badge/Requests-2CA5E0?style=flat-square)

A Python automation script that continuously scrapes job listings for "Python" roles from TimesJobs.com. It allows users to input specific skills they are unfamiliar with and filters out job postings requiring those skills, saving the relevant matches directly to local text files.

---

## ✨ Features

* **Automated Data Extraction:** Fetches live job postings using the `requests` library and parses the HTML using `BeautifulSoup`.
* **Dynamic Skill Filtering:** Prompts the user to enter unfamiliar skills and actively filters out job listings that mandate them.
* **Recency Filter:** Only extracts jobs that were published recently (marked as posted a "few" days ago).
* **Automated File Generation:** Saves matching job details (Company Name, Required Skills, and Application Link) into individual `.txt` files.
* **Continuous Monitoring:** Runs in an infinite loop, fetching new data every 10 minutes to keep you updated on the latest postings.

---

## 🛠️ Prerequisites

Before running the script, ensure you have Python installed on your system. You will also need to install the following external Python libraries:

* `requests`
* `beautifulsoup4`
* `lxml`

---

## 🚀 Setup & Installation

### 1. Clone the Repository
Download the script to your local machine:
```bash
git clone [https://github.com/yourusername/timesjobs-scraper.git](https://github.com/yourusername/timesjobs-scraper.git)
cd timesjobs-scraper
```
### 2. Install Dependencies
Install the required libraries using pip:
```bash
pip install requests beautifulsoup4 lxml
```

### 3. Create the Output Directory
The script writes job postings to a folder named "posts". You must create this folder in the same directory as the script before running it.
```bash
mkdir posts
```

### 4. Run the Script
Execute the Python file:
```bash
python main.py
```

