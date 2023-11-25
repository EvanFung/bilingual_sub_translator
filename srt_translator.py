import os
import re
import deepl
from tqdm import tqdm

def translate_text_bulk(texts, auth_key, target_language='ZH'):
    # Initialize the DeepL Translator
    translator = deepl.Translator(auth_key)

    # Translate all texts in one API call
    results = translator.translate_text(texts, target_lang=target_language)
    return [result.text for result in results]

def process_srt(file_path, auth_key):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Extract text lines for translation
    texts_to_translate = [line.strip() for line in lines if line.strip() and '-->' not in line and not re.match(r'^\d+$', line.strip())]

    # Translate all texts
    translations = translate_text_bulk(texts_to_translate, auth_key)

    # Map translations back to the SRT format
    translated_srt = []
    translation_index = 0
    for line in lines:
        if line.strip() and '-->' not in line and not re.match(r'^\d+$', line.strip()):
            bilingual_text = line.rstrip() + '\n' + translations[translation_index] + '\n'
            translated_srt.append(bilingual_text)
            translation_index += 1
        else:
            translated_srt.append(line)

    # Write the translated subtitles
    output_file_path = os.path.splitext(file_path)[0] + '_translated.srt'
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.writelines(translated_srt)

def process_folder(folder_path, auth_key):
    srt_files = [f for f in os.listdir(folder_path) if f.endswith('.srt')]
    for file in tqdm(srt_files, desc="Translating files", unit="file"):
        file_path = os.path.join(folder_path, file)
        process_srt(file_path, auth_key)

# Example usage
auth_key = ""  # Replace with your DeepL API key
folder_path = './srt_files'
process_folder(folder_path, auth_key)
