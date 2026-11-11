import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

for sid in ['2020_3', '2020_12']:
    path = f"c:/sol/기사문제 답지 만들기/data/explanations/{sid}.json"
    try:
        with open(path, 'r', encoding='utf-8') as f:
            d = json.load(f)
    except FileNotFoundError:
        print(f"{sid}.json not found yet.")
        continue

    print(f"=== Verifying {sid}.json ===")
    print(f"Total questions: {len(d['questions'])}")
    assert len(d['questions']) == 40
    for q in d['questions']:
        assert q['topic'].strip(), f"Q{q['qnum']} empty topic"
        assert q['explanation'].strip(), f"Q{q['qnum']} empty explanation"
        for i, c in enumerate(q['choices']):
            assert c.strip(), f"Q{q['qnum']} empty choice {i+1}"
    print(f"PASS: {sid}.json is valid and complete!\n")
