from deepl_translator import DeepLTranslator
from sub_processor import SubtitleProcessor

auth_key = "your_deepl_auth_key"
translator = DeepLTranslator(auth_key)

subtitle_processor = SubtitleProcessor(translator)
folder_path = 'path_to_your_folder_with_srt_files'
subtitle_processor.process_folder(folder_path)
