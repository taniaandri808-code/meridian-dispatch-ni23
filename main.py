import os
import sys
from pathlib import Path

def main():
    """Copy entry.png to the output directory."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    base = os.environ.get("MAKEFUN_BOT_DIR") or str(Path(__file__).resolve().parent)
    src = Path(base) / "entry.png"
    dst = Path(output_dir) / "entry.png"
    dst.parent.mkdir(parents=True, exist_ok=True)
    CHUNK = 65536  # 64 KiB
    with open(src, "rb") as fsrc, open(dst, "wb") as fdst:
        while True:
            chunk = fsrc.read(CHUNK)
            if not chunk:
                break
            fdst.write(chunk)
    src_size = src.stat().st_size
    dst_size = dst.stat().st_size
    if src_size != dst_size:
        print(f"Error: size mismatch source={src_size} destination={dst_size}", file=sys.stderr)
        sys.exit(1)
    print(str(dst))

if __name__ == "__main__":
    main()
