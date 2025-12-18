from listing_parser import parse_listing_page
from detail_parser import parse_project_detail
from models import Project
import pandas as pd


def scrape_projects(listing_html: str, detail_pages: dict) -> list[Project]:
    """
    Demonstrates how project data would be collected by:
    - parsing the listing page
    - following project links
    - parsing individual project detail pages
    """
    projects = []

    listing_data = parse_listing_page(listing_html)

    for item in listing_data:
        try:
            detail_html = detail_pages.get(item["project_number"], "")
            detail_data = parse_project_detail(detail_html)

            project = Project(
                **item,
                **detail_data
            )
            projects.append(project)

        except Exception:
            # failure of one project should not stop processing
            continue

    return projects


def save_projects_to_csv(projects: list[Project], file_name: str = "adb_projects.csv"):
    """
    Convert project objects to DataFrame and save as CSV.
    """
    if not projects:
        return

    df = pd.DataFrame([p.__dict__ for p in projects])
    df.to_csv(file_name, index=False)
