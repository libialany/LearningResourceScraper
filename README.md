# English Learning Resources Scraper

A web scraper that aggregates resources for learning English.


## Overview
This tool automatically collects and organizes various English learning resources from across the web, making it easier for language learners to find quality learning materials.

## Features
- Scrapes multiple resource types:
  - Online courses (free and paid)
  - Language exchange platforms
  - Educational podcasts
  - Learning apps
  - YouTube channels
  - Articles and tutorials

## Installation
1. Ensure you have Python 3.7+ and Poetry installed
2. Clone the repository:
```bash
git clone https://github.com/yourusername/english-learning-scraper.git
cd english-learning-scraper
```
3. Install dependencies:
```bash
poetry install
```

## Usage
1. Activate the virtual environment:
```bash
poetry shell
```

2. Run the scraper:
```bash
scrapy crawl news
```

## Data Storage
The scraped data is stored in MySQL database. For database configuration and setup, please refer to the [database setup guide](docs/database-setup.md).

## Scheduling
To run the scraper on a schedule, you can use cron jobs or scheduling libraries. For more information, check our [scheduling guide](docs/scheduling.md).

## Warning

This is version is not completed. i have to fix this trouble. If the text is in cursive, the text will not be saved.

![completed](./imgs/error.png)

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
[Add your license here]

## Resources
- [Scheduling Scrapy spiders](https://stackoverflow.com/questions/44228851/scrapy-on-a-schedule)
- [Saving data to MySQL with Scrapy](https://scrapeops.io/python-scrapy-playbook/scrapy-save-data-mysql/)