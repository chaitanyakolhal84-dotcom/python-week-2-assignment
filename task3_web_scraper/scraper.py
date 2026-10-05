import csv
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser


# ==========================================
# CONFIGURATION
# ==========================================

BASE_URL = "https://books.toscrape.com/"
START_URL = BASE_URL
OUTPUT_FILE = "books.csv"

MAX_PAGES = 2
REQUEST_DELAY = 2

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; WeIntern-Python-Assignment/1.0)"
}


# ==========================================
# CHECK ROBOTS.TXT
# ==========================================

def check_robots_txt(url):
    try:
        robots_url = urljoin(url, "robots.txt")

        robot_parser = RobotFileParser()
        robot_parser.set_url(robots_url)
        robot_parser.read()

        if robot_parser.can_fetch(
            HEADERS["User-Agent"],
            url
        ):
            print("robots.txt check: Scraping allowed.")
            return True

        print("robots.txt check: Scraping is not allowed.")
        return False

    except Exception as error:
        print(f"Could not check robots.txt: {error}")
        return False


# ==========================================
# SCRAPE ONE PAGE
# ==========================================

def scrape_page(url):

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=10
        )

        response.raise_for_status()

    except requests.exceptions.RequestException as error:
        print(f"Error requesting page: {error}")
        return [], None

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    books = []

    for book in soup.select("article.product_pod"):

        try:

            # ------------------------------
            # TITLE
            # ------------------------------

            title_tag = book.select_one("h3 a")

            if title_tag:
                title = title_tag.get(
                    "title",
                    title_tag.get_text(strip=True)
                )

                book_url = urljoin(
                    url,
                    title_tag.get("href", "")
                )

            else:
                title = "Unknown"
                book_url = ""


            # ------------------------------
            # PRICE
            # ------------------------------

            price_tag = book.select_one(
                ".price_color"
            )

            if price_tag:

                price = price_tag.get_text(
                    strip=True
                )

                # Fix Â£ / Ã‚Â£ encoding problems
                if "Â£" in price:
                    price = price.replace("Â£", "£")

                if "Ã‚Â£" in price:
                    price = price.replace("Ã‚Â£", "£")

                # Convert £ to GBP
                if price.startswith("£"):
                    price = "GBP " + price[1:].strip()

            else:
                price = "N/A"


            # ------------------------------
            # RATING
            # ------------------------------

            rating_tag = book.select_one(
                "p.star-rating"
            )

            if rating_tag:

                rating_classes = rating_tag.get(
                    "class",
                    []
                )

                rating = next(
                    (
                        item
                        for item in rating_classes
                        if item != "star-rating"
                    ),
                    "N/A"
                )

            else:
                rating = "N/A"


            # ------------------------------
            # ADD BOOK
            # ------------------------------

            books.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "URL": book_url
            })


        except Exception as error:

            print(
                f"Error processing a book: {error}"
            )


    # ======================================
    # NEXT PAGE
    # ======================================

    next_button = soup.select_one(
        "li.next a"
    )

    if next_button and next_button.get("href"):

        next_url = urljoin(
            url,
            next_button["href"]
        )

    else:
        next_url = None


    return books, next_url


# ==========================================
# SCRAPE MULTIPLE PAGES
# ==========================================

def scrape_books(max_pages=2):

    all_books = []

    current_url = START_URL
    page_number = 1

    while (
        current_url
        and page_number <= max_pages
    ):

        print()
        print(
            f"Scraping page {page_number}:"
        )
        print(current_url)

        books, next_url = scrape_page(
            current_url
        )

        if books:

            all_books.extend(books)

            print(
                f"Books found on page: {len(books)}"
            )

        else:

            print(
                "No books found on this page."
            )

        current_url = next_url
        page_number += 1

        # Delay before next request
        if (
            current_url
            and page_number <= max_pages
        ):

            print(
                f"Waiting {REQUEST_DELAY} seconds before next request..."
            )

            time.sleep(REQUEST_DELAY)

    return all_books


# ==========================================
# SAVE DATA TO CSV
# ==========================================

def save_to_csv(books):

    if not books:

        print(
            "No data available to save."
        )

        return

    fieldnames = [
        "Title",
        "Price",
        "Rating",
        "URL"
    ]

    try:

        with open(
            OUTPUT_FILE,
            "w",
            newline="",
            encoding="utf-8-sig"
        ) as csv_file:

            writer = csv.DictWriter(
                csv_file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(books)

        print()
        print(
            f"Data successfully saved to: {OUTPUT_FILE}"
        )

        print(
            f"Total books saved: {len(books)}"
        )

    except OSError as error:

        print(
            f"Error writing CSV file: {error}"
        )


# ==========================================
# MAIN
# ==========================================

def main():

    print("=" * 55)
    print("              BOOK WEB SCRAPER")
    print("=" * 55)

    # Check robots.txt
    if not check_robots_txt(START_URL):

        print()
        print(
            "Scraping stopped because robots.txt"
        )
        print(
            "does not allow scraping."
        )

        return

    # Scrape 2 pages
    books = scrape_books(
        max_pages=MAX_PAGES
    )

    # Save CSV
    save_to_csv(books)

    print()
    print(
        "Scraping completed successfully."
    )

    print("=" * 55)


if __name__ == "__main__":
    main()