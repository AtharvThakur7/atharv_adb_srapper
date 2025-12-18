from listing_parser import parse_listing_page
from detail_parser import parse_project_detail
from models import Project
import csv


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



def write_projects_to_csv(projects: list[Project], file_name="adb_projects.csv"):
    if not projects:
        return

    with open(file_name, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(projects[0].__dict__.keys())
        for project in projects:
            writer.writerow(project.__dict__.values())


if __name__ == "__main__":
   
    projects = scrape_projects(listing_html, detail_pages)
    write_projects_to_csv(projects)