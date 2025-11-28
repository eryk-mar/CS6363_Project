import json

INPUT_FILE = "csb_corpus_raw.json"
OUTPUT_FILE = "csb_corpus.txt"

with open(INPUT_FILE, "r", encoding="utf-8") as infile, \
     open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:

    for line in infile:
        line = line.strip()
        if not line:
            continue

        try:
            obj = json.loads(line)
        except Exception as e:
            print("JSON error:", e)
            continue

        text = obj.get("text", "").strip()

        if text:
            
            text = text.replace("<br>", " ").replace("<br/>", " ").replace("<br />", " ")
            text = text.replace("&lt;br&gt;", " ")
            text = text.replace("&lt;/br&gt;", " ")
            text = text.replace("<ref>", "").replace("</ref>", "")

            outfile.write(text + "\n")
