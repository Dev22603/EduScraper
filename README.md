# EduScraper

EduScraper is a project that combines the power of Python and ReactJS to streamline the creation of aptitude question papers. It features a web scraper to fetch questions from the IndiaBix website and a React app to generate PDFs of these questions for student practice.

## Features

- **Web Scraper:** Built with Python to scrape aptitude questions from IndiaBix, saving them in JSON and CSV formats.
- **PDF Generator:** A ReactJS app that uses the JSON file to create well-structured PDFs of multiple-choice questions.
- **Modular Design:** The project is designed to be modular, making it easy to extend and integrate new features.

## Future Plans

- **MongoDB Backend:** Plan to integrate a MongoDB backend to store scraped questions and manage them efficiently.

## Setup and Usage

### Prerequisites

- Python 3.x
- Node.js
- npm

### Web Scraper

1. Clone the repository.
2. Navigate to the `webscraper` directory.
3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the scraper script:
    ```bash
    python scraper.py
    ```
5. The questions will be saved in `questions.json` and `questions.csv`.

### React App

1. Navigate to the `react-app` directory.
2. Install the required npm packages:
    ```bash
    npm install
    ```
3. Start the React app:
    ```bash
    npm start
    ```
4. The app will read from `questions.json` and generate a PDF of the questions.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to reach out to me at [devbachani08@gmail.com].

---

*Note: Replace `[your email address]` with your actual email address.*
