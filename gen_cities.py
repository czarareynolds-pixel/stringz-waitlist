#!/usr/bin/env python3
"""
Generate all city landing pages from the Atlanta master template.

Usage:
    python gen_cities.py

Reads waitlist-atlanta/index.html, replaces city-specific content
(title, meta, canonical URL, OG tags, city slug, bg image, venues),
and writes to each waitlist-{slug}/index.html.
"""

import os, re

CITIES = [
    {
        "slug": "bayarea",
        "title": "Bay Area",
        "bg_image": "Stringz_Waitlist_San_Francisco.png",
        "venues": [
            "The Fillmore",
            "Salesforce Tower Terrace",
            "SFMOMA",
            "Lake Chalet",
            "Coin-Op SF",
            "Dolores Park",
        ],
    },
    {
        "slug": "seattle",
        "title": "Seattle",
        "bg_image": "Stringz_Waitlist_Seattle.png",
        "venues": [
            "The Showbox",
            "The Nest Rooftop",
            "Seattle Art Museum",
            "The Walrus & Carpenter",
            "Add-a-Ball",
            "Cal Anderson Park",
        ],
    },
    {
        "slug": "houston",
        "title": "Houston",
        "bg_image": "Stringz_Waitlist_Houston.png",
        "venues": [
            "The Post HTX",
            "Z on 23 Rooftop",
            "MFAH",
            "Brasserie du Parc",
            "Cidercade Houston",
            "Discovery Green",
        ],
    },
    {
        "slug": "dc",
        "title": "Washington DC",
        "bg_image": "Stringz_Waitlist_DC.png",
        "venues": [
            "Decades DC",
            "The Rooftop at the Graham",
            "National Gallery of Art",
            "Dauphine's",
            "Board Room DC",
            "The National Mall",
        ],
    },
    {
        "slug": "charlotte",
        "title": "Charlotte",
        "bg_image": "Stringz_Waitlist_Charlotte.png",
        "venues": [
            "The Broken Spoke",
            "Merchant & Trade",
            "Mint Museum Uptown",
            "Haberdish",
            "Abari Game Bar",
            "Romare Bearden Park",
        ],
    },
    {
        "slug": "chicago",
        "title": "Chicago",
        "bg_image": "Stringz_Waitlist_Chicago.png",
        "venues": [
            "The Promontory",
            "Cindy's Rooftop",
            "Art Institute of Chicago",
            "Beatnik West Town",
            "Headquarters Beercade",
            "Millennium Park",
        ],
    },
    {
        "slug": "newyork",
        "title": "New York",
        "bg_image": "Stringz_Waitlist_NY.png",
        "venues": [
            "House of Yes",
            "Westlight BK",
            "The Met",
            "Lavo NYC",
            "Barcade Brooklyn",
            "Bryant Park",
        ],
    },
    {
        "slug": "miami",
        "title": "Miami",
        "bg_image": "Stringz_Waitlist_Miami.png",
        "venues": [
            "The Wharf Miami",
            "Astra Rooftop",
            "Perez Art Museum",
            "Joia Beach",
            "Arcade Odyssey",
            "Bayfront Park",
        ],
    },
    {
        "slug": "losangeles",
        "title": "Los Angeles",
        "bg_image": "Stringz_Waitlist_LA.png",
        "venues": [
            "The Echo",
            "Perch DTLA",
            "The Broad",
            "Catch LA",
            "EightyTwo",
            "Hollywood Forever Cemetery",
        ],
    },
]

# Atlanta template venues (in order) for replacement
ATL_VENUES = [
    "The Painted Pin",
    "Ponce City Market Roof",
    "The High Museum",
    "Biltmore Ballrooms",
    "Joystick Gamebar",
    "Piedmont Park",
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def generate():
    template_path = os.path.join(BASE_DIR, "waitlist-atlanta", "index.html")
    with open(template_path, "r") as f:
        template = f.read()

    for city in CITIES:
        slug = city["slug"]
        title = city["title"]
        bg_img = city["bg_image"]
        venues = city["venues"]

        page = template

        # Replace <title>
        page = page.replace(
            "Stringz Atlanta — You're Invited",
            f"Stringz {title} — You're Invited",
        )

        # Replace meta description
        page = page.replace(
            "See what's happening in Atlanta.",
            f"See what's happening in {title}.",
        )

        # Replace canonical URL
        page = page.replace(
            "https://stringz.social/waitlist-atlanta",
            f"https://stringz.social/waitlist-{slug}",
        )

        # Replace OG title
        page = page.replace(
            "Stringz Atlanta — You're Invited",
            f"Stringz {title} — You're Invited",
        )

        # Replace background image
        page = page.replace(
            "Stringz_Waitlist_Atlanta.png",
            bg_img,
        )

        # Replace city slug in join link
        page = page.replace(
            "/join?city=atlanta",
            f"/join?city={slug}",
        )

        # Replace venues
        for atl_venue, new_venue in zip(ATL_VENUES, venues):
            page = page.replace(f'"{atl_venue}"', f'"{new_venue}"')

        # Write output
        out_dir = os.path.join(BASE_DIR, f"waitlist-{slug}")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "index.html")
        with open(out_path, "w") as f:
            f.write(page)

        print(f"  ✓ waitlist-{slug}/index.html")

    print(f"\nGenerated {len(CITIES)} city pages from Atlanta template.")


if __name__ == "__main__":
    generate()
