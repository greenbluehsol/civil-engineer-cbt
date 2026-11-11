import os
import json
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\sol\기사문제 답지 만들기"
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DIR = os.path.join(DATA_DIR, "sessions_raw")
EXP_DIR = os.path.join(DATA_DIR, "explanations")
PUB_DIR = os.path.join(BASE_DIR, "public")
PUB_DATA_DIR = os.path.join(PUB_DIR, "data")
PUB_PDF_DIR = os.path.join(PUB_DIR, "pdfs")

os.makedirs(PUB_DATA_DIR, exist_ok=True)
os.makedirs(PUB_PDF_DIR, exist_ok=True)

# Copy PDFs to public/pdfs if not already there
for fname in os.listdir(os.path.join(DATA_DIR, "pdfs")):
    src = os.path.join(DATA_DIR, "pdfs", fname)
    dst = os.path.join(PUB_PDF_DIR, fname)
    if not os.path.exists(dst):
        shutil.copy2(src, dst)

with open(os.path.join(DATA_DIR, "sessions.json"), "r", encoding="utf-8") as f:
    sessions = json.load(f)

bundle = {}
total_q = 0
explained_q = 0

for s in sessions:
    sid = s["id"]
    raw_path = os.path.join(RAW_DIR, f"{sid}.json")
    exp_path = os.path.join(EXP_DIR, f"{sid}.json")
    
    with open(raw_path, "r", encoding="utf-8") as f:
        raw_obj = json.load(f)
        
    if os.path.exists(exp_path):
        try:
            with open(exp_path, "r", encoding="utf-8") as f:
                exp_obj = json.load(f)
            # Map by qnum
            exp_map = {q["qnum"]: q for q in exp_obj.get("questions", [])}
            for q in raw_obj["questions"]:
                eq = exp_map.get(q["qnum"], {})
                if eq.get("explanation"):
                    q["explanation"] = eq["explanation"]
                    explained_q += 1
                if eq.get("topic"):
                    q["topic"] = eq["topic"]
                if eq.get("choices") and any(eq["choices"]):
                    q["choices"] = eq["choices"]
        except Exception as e:
            print(f"Warning reading {exp_path}: {e}")
            
    total_q += len(raw_obj["questions"])
    bundle[sid] = raw_obj

json_str = json.dumps(bundle, ensure_ascii=False, indent=2)
with open(os.path.join(PUB_DATA_DIR, "exams.json"), "w", encoding="utf-8") as f:
    f.write(json_str)

with open(os.path.join(PUB_DATA_DIR, "exams_bundle.js"), "w", encoding="utf-8") as f:
    f.write("window.EXAMS_DATA = " + json_str + ";\n")

print(f"Built bundle: {len(bundle)} sessions, {explained_q}/{total_q} questions with explanations.")
