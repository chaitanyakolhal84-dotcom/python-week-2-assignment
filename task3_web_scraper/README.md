\# Task 3 - Web Scraper



\## Project Description



This project is a Python web scraper developed as part of the WeIntern Python Development Week 2 assignment.



The scraper collects book information from the public website:



https://books.toscrape.com/



The scraped information is saved into a CSV file named `books.csv`.



\## Objective



The objective of this project is to:



\* Send HTTP requests to a public website

\* Extract structured data using BeautifulSoup

\* Scrape data from multiple pages

\* Handle pagination

\* Handle request and missing-field errors

\* Add a delay between requests

\* Check robots.txt before scraping

\* Save the collected data into a CSV file



\## Target Website



Website:



https://books.toscrape.com/



Books to Scrape is a public website suitable for practicing web scraping.



\## Technologies Used



\* Python

\* Requests

\* BeautifulSoup

\* CSV module

\* Time module

\* urllib.robotparser



\## Fields Scraped



The scraper collects the following four fields for each book:



| Field  | Description             |

| ------ | ----------------------- |

| Title  | Name of the book        |

| Price  | Price of the book       |

| Rating | Star rating of the book |

| URL    | Direct URL of the book  |



\## Pagination Logic



The scraper starts from the main page and identifies the `Next` page link.



The scraper is configured to collect data from 2 pages.



Each page contains 20 books.



Therefore, the final CSV contains:



\* Page 1: 20 books

\* Page 2: 20 books

\* Total: 40 books



The scraper automatically creates the URL for the next page using the `Next` button found on the current page.



\## Request Delay



A 2-second delay is added between page requests.



This helps avoid sending requests continuously to the website.



\## Robots.txt Handling



Before scraping starts, the program checks the website's `robots.txt` file.



The scraper proceeds only when scraping is allowed.



\## Error Handling



The program handles:



\* HTTP request errors

\* Connection errors

\* Missing title

\* Missing price

\* Missing rating

\* Missing book URL

\* CSV writing errors



If a field is missing, the scraper uses suitable fallback values such as `Unknown`, `N/A`, or an empty URL.



\## CSV Output



The scraped data is saved in:



`books.csv`



The CSV contains the following columns:



```text

Title, Price, Rating, URL

```



Example:



```text

A Light in the Attic,GBP 51.77,Three,https://books.toscrape.com/catalogue/a-light-in-the-attic\_1000/index.html

Tipping the Velvet,GBP 53.74,One,https://books.toscrape.com/catalogue/tipping-the-velvet\_999/index.html

Soumission,GBP 50.10,One,https://books.toscrape.com/catalogue/soumission\_998/index.html

```



\## Project Structure



```text

task3\_web\_scraper/

│

├── scraper.py

├── books.csv

└── README.md

```



\## Installation



Install the required Python libraries using:



```powershell

python -m pip install requests beautifulsoup4

```



\## How to Run



Open PowerShell and navigate to the project folder:



```powershell

cd C:\\python-week2-assignment\\task3\_web\_scraper

```



Run the scraper:



```powershell

python scraper.py

```



\## Expected Output



The program displays:



```text

robots.txt check: Scraping allowed.



Scraping page 1:

https://books.toscrape.com/

Books found on page: 20



Waiting 2 seconds before next request...



Scraping page 2:

https://books.toscrape.com/catalogue/page-2.html

Books found on page: 20



Data successfully saved to: books.csv

Total books saved: 40



Scraping completed successfully.

```



\## Testing



The scraper was tested successfully.



Test results:



\* robots.txt check: Passed

\* Page 1 scraping: Passed

\* Page 2 scraping: Passed

\* Pagination: Passed

\* Book fields extraction: Passed

\* Request delay: Passed

\* CSV generation: Passed

\* Total records: 40

\* CSV fields: 4



\## Output File Verification



The generated `books.csv` was checked successfully.



The output contains:



\* 40 book records

\* Title

\* Price

\* Rating

\* URL



\## Conclusion



The web scraper successfully collects book information from two pages of the Books to Scrape website and stores the results in a structured CSV file.



The project demonstrates HTTP requests, HTML parsing, pagination, error handling, robots.txt checking, request delay, and CSV file handling using Python.



\## Author



Chaitanya Kolhal



