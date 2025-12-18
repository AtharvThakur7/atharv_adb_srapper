from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://www.adb.org"



def parse_listing_page(html: str) -> list[dict]:
    """
    Parse ADB projects listing page HTML and extract summary project data.
    """
    soup = BeautifulSoup(html, "html.parser")
    projects = []

    for item in soup.select("div.item.linked"):
        title_tag = item.select_one("div.item-title a")
        summary = item.select_one("div.item-summary")

        if not title_tag or not summary:
            continue  # skip incomplete entries

        parts = [p.strip() for p in summary.get_text().split(";")]

        # Status (second span inside item-meta)
        status_spans = item.select("div.item-meta span")
        status = status_spans[1].text.strip() if len(status_spans) > 1 else ""

        # Approval year
        year_tag = item.select_one("div.item-meta time")
        approval_year = year_tag.text.strip() if year_tag else ""

        projects.append({
            "project_number": parts[0] if len(parts) > 0 else "",
            "project_title": title_tag.text.strip(),
            "project_url": urljoin(BASE_URL, title_tag["href"]),
            "country": parts[1] if len(parts) > 1 else "",
            "sector": parts[2] if len(parts) > 2 else "",
            "status": status,
            "approval_year": approval_year,
        })

    return projects
