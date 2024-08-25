import requests
from bs4 import BeautifulSoup
from xml.etree import ElementTree as ET
import re
import os
import json
import yaml

def fetch_product_urls(sitemap_url):
    product_urls = set()
    response = requests.get(sitemap_url)
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
   
    # REad the XML and create an XML Element Tree for parsing
    tree = ET.ElementTree(ET.fromstring(response.content))
    root = tree.getroot()
    
    # Extract URLs containing the word 'product'
    product_urls = []
    for url in root.findall('ns:url', namespace):
        loc = url.find('ns:loc', namespace).text
        if 'product' in loc.lower():
            product_urls.append(loc)
    
    return product_urls

def prepare_download_list(product_urls):
    final_results = []
    pattern = r'\s*\b\W+\b\s*'

    for url in product_urls:
        product_name = ""
        crumbs = set()
        pdf_links = set()
        download_path = []
        
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find references to download PDFs on the current product URL page
            pdf_elements = soup.find_all('a', href=re.compile(r'\.pdf$'))
            
            # Check all the PDFs and only proceed if there is actual Build Documentation on the page. Otherwise go to next URL 
            for link in pdf_elements:
                if "Download Build Documentation" in link.get_text().strip():
                    pdf_links.add(link['href'])
                else:
                    print(link, " doesn't have a Build Documentation PDF")

            # IF there is Build documentation then for each build doc find the bread crumbs and to the  list of download paths
            if pdf_links:
                 # Find the navigation class 'woocommerce-breadcrumb breadcrumbs'
                nav = soup.find('nav', class_='woocommerce-breadcrumb breadcrumbs')
                if not nav:
                    print(pdf_links, " doesn't have breadcrumbs")
                    continue # Skip this product if no breadcrumbs found
                
                # Extract all 'a' tags within this navigation structure
                crumbs = nav.find_all('a')

                for crumb in crumbs:
                    text = crumb.get_text(strip=True)
                    
                    # Replace the matched pattern with an empty space
                    modified_text = [token.upper() for token in re.split(pattern, text) if token]

                    # Add breadcrumbs to create a path
                    download_path.extend(modified_text)

                # Find the header element that contains the name of product
                product_name = soup.find('h1', class_='product-title product_title entry-title').get_text().strip()
                
                # If there is no product name skip to next URL 
                if not product_name: 
                    print(pdf_links," doesn't have Product Title")
                    continue # Skip this product if no Product Title found

                # Create a path from crumbs while dropping the first crumb as its the HOME crumb and prepare the product_name.
                # product_name will be used as the actual PDF file name later on when downloading.                 
                product_name=re.sub(r'[^a-zA-Z0-9]', '', product_name)    
            
                # Add the build files (including FileName, BreadCrumbs and link to the list of files to download)
                for link in pdf_links:  
                    final_results.append({
                        'Product Name': product_name,
                        'Type': download_path[-1],
                        'URL': link
                    })
                print (link, "added to download list")
            
            else:
                continue # Skip this product if no build doco found
                    
        except requests.RequestException as e:
            print(f"Failed to process {url}: {str(e)}")
    
    # Return the final results as a list of dictionaries, which is a JSON-serializable structure
    with open(download_file, "w") as json_file:
        json.dump(final_results, json_file, indent=4)

if __name__ == "__main__":
    
    #Load the environment variables from config.yaml
    with open('config.yaml') as config_file:
        config = yaml.safe_load(config_file)

    # Set global variables
    sitemap_url = config['sitemap_url']
    download_file = config['download_file']
    download_file = os.path.abspath(download_file)
    
    #get a list of all "product" URLs from the sitemap
    product_urls = fetch_product_urls(sitemap_url)
    
    #create the list of files to download
    prepare_download_list(product_urls)