import argparse
from .runner import run_tests
from .utils import write_results
import json
import sys


def main():
    print("------CLI is running------")

    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config/sample-test.json")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    parser.add_argument("--summary", action="store_true", help="Show only PASS/FAIL summary")
    parser.add_argument("--fail-fast", action="store_true", help="Stop on first failure")
    parser.add_argument(
            "--no-exit-on-fail",
            action="store_true",
            help="Do not exit with code 1 if any test fails"
        )

    args = parser.parse_args()

    results = run_tests(args.config)
    write_results(results)

    for r in results:
        print(r)
    
    if args.json:
        print(json.dumps(results, indent=2))
        return

    if args.summary:
        for r in results:
            print(f"{'PASS' if r['passed'] else 'FAIL'} - {r['name']}")
        return

    if not args.no_exit_on_fail:
        if not all(r["passed"] for r in results):
            sys.exit(1)
    else:
        sys.exit(1)  


if __name__ == "__main__":
        main()
