import os
import subprocess
from pathlib import Path

root_dir = Path('.')
output_in_same_folder = True

output_base = Path('./tetelek_pdf')

def convert_md_to_pdf(md_path: Path):
    relative_path = md_path.relative_to(root_dir)
    pdf_path = output_base / relative_path.with_suffix('.pdf')
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        subprocess.run([
            "pandoc",
            str(md_path),
            "-o", str(pdf_path),
            "--pdf-engine=tectonic"
        ], check=True)
        print(f"PDF kész: {pdf_path}")
    except subprocess.CalledProcessError as e:
        print(f"Hiba: {e} - {pdf_path}")

for md_file in root_dir.rglob("*.md"):
    convert_md_to_pdf(md_file)