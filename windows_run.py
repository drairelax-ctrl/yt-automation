"""Local entry point; upload is opt-in and no-topic invocation is a check."""
import argparse
import importlib
from pathlib import Path
import shutil

parser = argparse.ArgumentParser(description='YT Automation: local check by default; --topic generates, --upload explicitly enables publishing.')
parser.add_argument('--topic')
parser.add_argument('--upload', action='store_true')
args = parser.parse_args()
if not args.topic:
    for name in ('config','script_generator','voice_generator','footage_fetcher','visual_builder','video_assembler','uploader'):
        importlib.import_module(name)
        print(name, 'IMPORT OK')
    for name in ('ffmpeg','ffprobe'):
        print(name, shutil.which(name) or 'MISSING')
    for name in ('kokoro-v1.0.onnx','voices-v1.0.bin'):
        print(name, 'OK' if Path(name).exists() else 'MISSING')
    print('Generate later: run.bat --topic "Your topic". Upload additionally requires --upload and OAuth.')
else:
    import main
    if not args.upload:
        main.upload_to_youtube = lambda **kwargs: 'UPLOAD DISABLED: local video retained'
    main.run(args.topic)
