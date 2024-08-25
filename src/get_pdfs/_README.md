# GET_PDFS
Modules here will scra a site and downlaod the PDFs in this sequence of steps:
## STEP 1
Scrape_download_list: scrapes the pedalpcb.com website and creates a JSON file with pedal PDFs, and reviews. This JSON file will be used later in the application to create the product vector DB as well that will be used for RAG 
## STEP 2
Get_build_pdfs: runs multithreaded and downloads the PDFs from JSON file created in Step 1

