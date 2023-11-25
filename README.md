Requirements
Python 3.x
deepl Python package
tqdm Python package
Installation
Before running the script, you need to install the required packages. You can do this using pip:
pip install deepl tqdm

Setting Up Your DeepL API Key
To use this script, you will need a DeepL API key.

Once you have your API key, replace your_deepl_auth_key in the script with your actual DeepL API key.

Usage
Place the script in a directory of your choice.

Ensure that your .srt files are in a single folder (the script will process all .srt files within this folder).

Open the script and set the folder_path variable to the path of the folder containing your SRT files.

Run the script:

bash
Copy code
python srt_translator.py
The script will process each file and output the translated subtitles in the same folder with _translated appended to the file name.