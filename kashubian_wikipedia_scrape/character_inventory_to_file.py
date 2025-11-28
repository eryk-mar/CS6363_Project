
import sys
from collections import Counter

if len(sys.argv) < 3:
    print("Usage: python3 character_inventory_to_file.py <input_corpus.txt> <output_file.txt>")
    sys.exit(1)

input_path = sys.argv[1]
output_path = sys.argv[2]

with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()


counts = Counter(text)

sorted_chars = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

with open(output_path, "w", encoding="utf-8") as out:
    out.write("CHARACTER INVENTORY (sorted by frequency)\n")
    out.write("=========================================\n\n")

    for ch, n in sorted_chars:
        if ch == "\n":
            display = "\\n"
        elif ch == "\t":
            display = "\\t"
        elif ch == " ":
            display = "[space]"
        else:
            display = ch

        out.write(f"{display}: {n}\n")

    out.write(f"\nTotal unique characters: {len(sorted_chars)}\n")

print(f"Character inventory written to: {output_path}")
