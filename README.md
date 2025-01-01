
# AI Scraper Project

Welcome to the AI Scraper project repository! This project uses Python, Selenium, BeautifulSoup, and the Ollama language model to scrape, parse, and extract information from web pages.

## Project Overview

The AI Scraper is designed to handle complex web scraping tasks including captcha solving, HTML parsing, and structured data extraction using advanced AI techniques.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/umutkayash/AI-Scraper.git
   cd AI-Scraper
   ```

2. **Set Up a Virtual Environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

- You will need to set environment variables for the Selenium WebDriver URL. You can do this by creating a `.env` file in the project root with the following content:
  ```
  WEBDRIVER_URL="your_webdriver_url_here"
  ```

## Usage

To run the scraper:
1. **Activate your virtual environment if not already activated:**
   ```bash
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

2. **Run the Scraper:**
   ```bash
   python main.py
   ```
   Replace `main.py` with the script you wish to run.

## How It Works

The AI Scraper performs the following steps:
- Connects to a web page using Selenium.
- Handles any captchas using configured settings.
- Extracts HTML content and parses it using BeautifulSoup.
- Segments the HTML content if necessary.
- Uses the Ollama model to extract specific information based on user-defined criteria.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
