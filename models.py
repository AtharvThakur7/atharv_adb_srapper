from dataclasses import dataclass

@dataclass
class Project:
    # Listing page fields
    project_number: str
    project_title: str
    project_url: str
    country: str
    sector: str
    status: str
    approval_year: str

    # Detail page fields (optional / may be missing)
    project_type: str = ""
    funding_amount: str = ""
    impact: str = ""
    outcome: str = ""
    outputs: str = ""
    executing_agencies: str = ""
