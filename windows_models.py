from pathlib import Path
import urllib.request
base = Path(__file__).resolve().parent
for name in ('kokoro-v1.0.onnx', 'voices-v1.0.bin'):
    target = base / name
    if not target.exists():
        temporary = target.with_suffix(target.suffix + '.download')
        urllib.request.urlretrieve('https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/' + name, temporary)
        temporary.replace(target)
    print(name, 'OK', target.stat().st_size)
