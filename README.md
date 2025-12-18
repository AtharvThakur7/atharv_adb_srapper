# ADB Projects Scraping

projects website:
https://www.adb.org/projects

## The goal is not to perform live web scraping, but to design and implement the parsing logic required to:

Extract project data from the main projects listing page

Follow links to individual project detail pages

Parse additional project details from those pages

Combine listing-level and detail-level data into a structured dataset

This approach mirrors how a real data engineering scraping pipeline would be structured.

## Project Files

listing_parser.py – Parses the projects listing page

detail_parser.py – Parses individual project detail pages

scraper.py – Demonstrates how listing and detail parsing work together

models.py – Defines the structured Project data model
