# /// script
# dependencies = [
#     "httpx",
#     "beautifulsoup4",
# ]
# ///

"""
Download PennDOT Crash Data.

PennDOT shares their Crash data via an ArcGIS Experience. The raw data is available as zip files.

The page is a dynamic javascript page so the HTML with links to the raw data was copied from the browser and pasted below to be parsed and processed. This is easier than trying to parse the javascript or render in a headless browser process.

HTML is copied from https://experience.arcgis.com/experience/51809b06e7b140208a4ed6fbad964990

1. Parse copied HTML and extract URLS
2. Download each zip file, extract, and save into specified folder. Each zip file in a separate folder.
"""

import httpx
import bs4 as beautifulsoup
import zipfile
import os
import argparse
from io import BytesIO

def main():
    parser = argparse.ArgumentParser(description="Download and extract PennDOT crash data")
    parser.add_argument(
        "--output-dir",
        default="data/raw",
        help="Output directory for downloaded files (default: data/raw)"
    )
    args = parser.parse_args()

    copied_html = """
    <div style="font-size:14.5px; font-family:Tahoma; line-height:1.5; text-align:center;"><a href="https://gis.penndot.pa.gov/gishub/crashZip/Statewide/Statewide_2005.zip" target="_blank" style="color:#007934;">2005  Statewide</a><br><p></p><a href="https://gis.penndot.pa.gov/gishub/crashZip/Statewide/Statewide_2006.zip" target="_blank" style="color:#007934;">2006  Statewide</a><br><p></p><a href="https://gis.penndot.pa.gov/gishub/crashZip/Statewide/Statewide_2007.zip" target="_blank" style="color:#007934;">2007  Statewide</a><br><p></p><a href="https://gis.penndot.pa.gov/gishub/crashZip/Statewide/Statewide_2008.zip" target="_blank" style="color:#007934;">2008  Statewide</a><br><p></p><a href="https://gis.penndot.pa.gov/gishub/crashZip/Statewide/Statewide_2009.zip" target="_blank" style="color:#007934;">2009  Statewide</a><br><p></p><a href="https://gis.penndot.pa.gov/gishub/crashZip/Statewide/Statewide_2010.zip" target="_blank" style="color:#007934;">2010  Statewide</a><br><p></p><a href="https://gis.penndot.pa.gov/gishub/crashZip/Statewide/Statewide_2011.zip" target="_blank" style="color:#007934;">2011  Statewide</a><br><p></p><a href="https://gis.penndot.pa.gov/gishub/crashZip/Statewide/Statewide_2012.zip" target="_blank" style="color:#007934;">2012  Statewide</a><br><p></p><a href="https://gis.penndot.pa.gov/gishub/crashZip/Statewide/Statewide_2013.zip" target="_blank" style="color:#007934;">2013  Statewide</a><br><p></p><a href="https://gis.penndot.pa.gov/gishub/crashZip/Statewide/Statewide_2014.zip" target="_blank" style="color:#007934;">2014  Statewide</a><br><p></p><a href="https://gis.penndot.pa.gov/gishub/crashZip/Statewide/Statewide_2015.zip" target="_blank" style="color:#007934;">2015  Statewide</a><br><p></p><a href="https://gis.penndot.pa.gov/gishub/crashZip/Statewide/Statewide_2016.zip" target="_blank" style="color:#007934;">2016  Statewide</a><br><p></p><a href="https://gis.penndot.pa.gov/gishub/crashZip/Statewide/Statewide_2017.zip" target="_blank" style="color:#007934;">2017  Statewide</a><br><p></p><a href="https://gis.penndot.pa.gov/gishub/crashZip/Statewide/Statewide_2018.zip" target="_blank" style="color:#007934;">2018  Statewide</a><br><p></p><a href="https://gis.penndot.pa.gov/gishub/crashZip/Statewide/Statewide_2019.zip" target="_blank" style="color:#007934;">2019  Statewide</a><br><p></p><a href="https://gis.penndot.pa.gov/gishub/crashZip/Statewide/Statewide_2020.zip" target="_blank" style="color:#007934;">2020  Statewide</a><br><p></p><a href="https://gis.penndot.pa.gov/gishub/crashZip/Statewide/Statewide_2021.zip" target="_blank" style="color:#007934;">2021  Statewide</a><br><p></p><a href="https://gis.penndot.pa.gov/gishub/crashZip/Statewide/Statewide_2022.zip" target="_blank" style="color:#007934;">2022  Statewide</a><br><p></p><a href="https://gis.penndot.pa.gov/gishub/crashZip/Statewide/Statewide_2023.zip" target="_blank" style="color:#007934;">2023  Statewide</a><br><p></p><a href="https://gis.penndot.pa.gov/gishub/crashZip/Statewide/Statewide_2024.zip" target="_blank" style="color:#007934;">2024  Statewide</a><br><p></p></div>"""

    # Parse HTML and extract URLs
    soup = beautifulsoup.BeautifulSoup(copied_html, "html.parser")
    urls = [tag['href'] for tag in soup.find_all("a")]

    print(f"Found {len(urls)} URLs to download")

    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)

    # Download and extract each zip file
    for url in urls:
        filename = url.split("/")[-1]
        folder_name = filename.replace(".zip", "")

        print(f"Downloading {filename}...")

        # Download
        response = httpx.get(url)
        response.raise_for_status()

        # Extract to folder with zip name
        with zipfile.ZipFile(BytesIO(response.content)) as zip_ref:
            zip_ref.extractall(f"{args.output_dir}/{folder_name}")

        print(f"Extracted {filename} to {args.output_dir}/{folder_name}")

    print("Download and extraction complete!")

if __name__ == "__main__":
    main()
