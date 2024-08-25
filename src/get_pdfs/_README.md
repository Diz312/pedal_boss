# GET_PDFS
Modules here will scrape the pedalpcb.copk site and create to create a JSON file. This JSON file will be used to create vector embedding representing all the products the site has to offer and will also be used as the directory of PDF files to be donwloaded. 

## STEP 1
Scrape_download_list: scrapes the pedalpcb.com website and creates a JSON file with pedal PDFs.
## STEP 2
Get_build_pdfs: runs multithreaded and downloads the PDFs from JSON file created in Step 1
