from bs4 import BeautifulSoup

def parse_project_detail(html: str) -> dict:
    """
    Parse ADB project detail page HTML (Project Data Sheet section).
    """
    soup = BeautifulSoup(html, "html.parser")
    data = {}

    # iterate through ALL PDS sections
    for pds in soup.select("dl.pds"):
        for dt, dd in zip(pds.find_all("dt"), pds.find_all("dd")):
            label = dt.text.strip()
            value = dd.get_text(" ", strip=True)

            field_map = {
                "Source of Funding / Amount": "funding_amount",
                "Impact": "impact",
                "Outcome": "outcome",
                "Outputs": "outputs",
                "Executing Agencies": "executing_agencies",
            }

            if label in field_map and value:
                data[field_map[label]] = value

    return data
