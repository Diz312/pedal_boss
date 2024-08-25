import os
import json
import requests
from concurrent.futures import ThreadPoolExecutor

def download_pdf(entry):
    # Extract the necessary nodes
    pdf_url = entry.get('URL')
    product_type = entry.get('Type')
    product_name = entry.get('Product Name')
    
    if pdf_url and product_type and product_name:
        # Construct the file name
        file_name = f"{product_type}_{product_name}.pdf"
        file_name = file_name.replace(" ", "_")  # Replace spaces with underscores for the file name
        
        # Download the PDF
        response = requests.get(pdf_url)
        
        if response.status_code == 200:
            # Save the PDF
            with open(file_name, 'wb') as pdf_file:
                pdf_file.write(response.content)
            print(f"Downloaded: {file_name}")
        else:
            print(f"Failed to download {file_name} from {pdf_url}")
    else:
        print("Invalid data in JSON entry.")

def main(json_file):
    # Read the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Download PDFs in parallel
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_pdf, data)

if __name__ == "__main__":
    # Load the environment variables from config.yaml
    yaml_path=os.path.join(os.path.dirname(__file__), 'config.yaml')
    with open(yaml_path) as config_file:
        config = yaml.safe_load(config_file)

    # Set global variables
    # set the relative path to the tmp directory - check config file and make sure the right level is set
    tmp_path = os.path.join(
        os.path.dirname(__file__), 
        os.path.normpath (config['tmp_path'])
    )
    
    # Set global file variables
    prod_file = os.path.join(tmp_path, config['prod_file'])
    
    # Replace 'your_json_file.json' with your actual JSON file name
    json_file = prod_file
    main(json_file)
