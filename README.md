# pedal_boss
This repo contains the code for an application that can be used to organize and manage building of guitar pedals. 
Guitar pedals are used to alter the normal tone of a guitar signal before it is fed into an amplifier. 
Modifying the signal enables tone shaping to create the desired tone of the guitar.
Proprietary pedals have been reversed engineered and various vendors offer PCBs to create clones of original pedals at fraction of cost.
Code in this repo will help a hobbyist to manage pedal BOMs, inventory and overall build process. 

# Why I built this: 
Primarily to study coding concepts including LangChain. To have a simple app that can help me manage my pedal builds and parts inventory

# App features published: 
1. src/get_pdfs/scrpae_donwload_list.py
   
# App features still under construction:
1Extract text from PDFs and run through a LangChain to extract standardized BOMS
2Store the BOM of each pedal 
3Store my inventory of components 
4Simple UI where I select the pedal to build and the app checks inventory 

# Tools I'm using:
1VS Code as IDE and using pipenv to manage environment
2LangChain and GPT3.5 Turbo
3REDIS for DB 

