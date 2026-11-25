import os
import sys

ENTRY = "Laundry v2.1: Socks now disappear in pairs so you can stop keeping the survivor around for closure."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verify: read the file back and require an exact match, no trailing newline.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("ERROR: entry.txt does not match ENTRY exactly", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
