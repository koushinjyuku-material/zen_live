"""XeLaTeX で問題・解答を再生成する。Python 3 と TeX Live が必要。"""
from pathlib import Path
import shutil
import subprocess
import re

lesson = Path(__file__).resolve().parent
source = lesson / "source"
scratch = lesson.parents[1] / "tmp" / "pdfs" / "thermodynamics_v3"
output = lesson / "output" / "pdf"
scratch.mkdir(parents=True, exist_ok=True)
output.mkdir(parents=True, exist_ok=True)

for stem, filename in [("problems", "熱力学_問題.pdf"), ("answers", "熱力学_解答.pdf")]:
    command = ["xelatex", "-interaction=nonstopmode", "-halt-on-error", f"-output-directory={scratch}", f"{stem}.tex"]
    with (scratch / f"{stem}-build.txt").open("w") as log:
        for _ in range(2):
            subprocess.run(command, cwd=source, stdout=log, stderr=subprocess.STDOUT, check=True)
    log_text = (scratch / f"{stem}.log").read_text()
    if "Overfull" in log_text or "Missing character" in log_text:
        raise RuntimeError(f"{stem}: 組版のはみ出し・欠落を確認してください。")
    info = subprocess.check_output(["pdfinfo", str(scratch / f"{stem}.pdf")], text=True)
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    expected_pages = {"problems": 9, "answers": 14}[stem]
    if pages != expected_pages:
        raise RuntimeError(f"{stem}: {pages}ページです。意図しない改ページを確認してください。")
    shutil.copy2(scratch / f"{stem}.pdf", output / filename)
    print(output / filename)
