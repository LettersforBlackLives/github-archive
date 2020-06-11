## Letters for Black Lives Github Archival

Instead of hosting everything on Medium, we're trying to also have the letters available through a more permanent medium like Github. This project aims to archive the content of different letters & translations of Medium links into a markdown format, where it will be hosted on a Github Pages site.

The script `converter.py` will populate the directory with markdown links. It is a wrapper to call the Node.js tool https://github.com/SkillFlowHQ/medium-to-markdown#readme with the links to the letters.

The Jupyter notebook can also be used to inspect data and commands.
To run it, Python 3 and Node.js are required. 
1. Run `pip install pandas` in this directory. 
2. Go inside the ` medium-to-markdown` directory and run `npm install`.
3. Run `python converter.py`


