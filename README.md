# pedal_boss
This repo contains the code for an application that can be used to organize and manage building of guitar pedals. 
Guitar pedals are used to alter the normal tone of a guitar signal before it is fed into an amplifier 
Modifying the signal enables tone shaping to create the desired tone of the guitar
Proprietary pedal design have been reversed engineered and various vendors offer PCBs to create clones of original pedals at fraction of cost

Why I built this: 
Primarily to study coding concepts including LangChain
Simple inventory management so I know what pedals I can build or when I have to order additional components 


App features: 
Scrape the PedalPCB site for all build PDFs

----BELOW FEATURES ARE WIP------------
Extract text from PDFs and run through a LangChain to extract standardized BOMS
Store the BOM of each pedal 
Store my inventory of components 
Simple UI where I select the pedal to build and the app checks inventory 

Tools used: 
VS Code as IDE and using pipenv to manage environment
LangChain and GPT3.5 Turbo
REDIS for DB 

