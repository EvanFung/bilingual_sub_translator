import os
import re
from tqdm import tqdm

class SubtitleProcessor:
    def __init__(self, translator):
        self.translator = translator
        
    def process_srt(self, file_path):
        translated_srt = []
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            if re.match(r'^\d+$', line.strip()):  # Regex to check if line is a subtitle number
                # Add a newline before the subtitle number if it's not the first subtitle
                if translated_srt:
                    translated_srt.append('\n')
                translated_srt.append(line)
            elif '-->' in line:  # Timestamp line
                translated_srt.append(line)
            elif line.strip():  # Text line
                translated_text = translate_text(line.strip(), translator, 'ZH')
                bilingual_text = line.strip() + '\n' + translated_text + '\n'
                translated_srt.append(bilingual_text)

        output_file_path = os.path.splitext(file_path)[0] + '_translated.srt'
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.writelines(translated_srt)
    
    def process_folder(self, folder_path):
        srt_files = [f for f in os.listdir(folder_path) if f.endswith('.srt')]
        for file in tqdm(srt_files, desc="Translating files", unit="file"):
            file_path = os.path.join(folder_path, file)
            self.process_srt(file_path)
