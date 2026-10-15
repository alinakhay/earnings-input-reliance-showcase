"""Inspect three recorded benchmark comparisons using only Python's standard library."""
from pathlib import Path
import argparse, json

def load_cases():
    return json.loads((Path(__file__).resolve().parent/'examples/recorded_cases.json').read_text())

def main():
    data=load_cases()
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', choices=[case['id'] for case in data['cases']])
    args=parser.parse_args()
    print('Recorded comparisons; no live inference or observed stock-return labels.\n')
    for case in data['cases']:
        if args.case and args.case!=case['id']:
            continue
        delta=100*(case['changed_score']-case['baseline_score'])
        print(case['title'])
        print(f"  Baseline: {100*case['baseline_score']:.2f}%")
        print(f"  Changed:  {100*case['changed_score']:.2f}%")
        print(f"  Change:   {delta:+.2f} percentage points\n")
    print(data['score_meaning'])

if __name__=='__main__':
    main()
