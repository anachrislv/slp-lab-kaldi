from helpers import run_cmd
from util import l

print("Running 4.2")

# 4.2.1

# silence_phones.txt && optional_silence.txt
with open("data/local/dict/silence_phones.txt", "w") as outfile:
    print("sil", file=outfile)

# nonsilence_phones.txt
with open("data/local/dict/optional_silence.txt", "w") as outfile:
    print("sil", file=outfile)

phones = set() # To exclude duplicates

# Create file of sorted phones
with open("lexicon.txt") as infile, open("data/local/dict/nonsilence_phones.txt", "w") as outfile:
    for line in infile.readlines():
        line_phones = line.split("\t")[1].strip().split()
        for phone in line_phones:
            phones.add(phone)

    # Discard silence phone
    phones.discard("sil")

    # Sort remaining phones
    phones = sorted(list(phones))

    # Print in each line
    for i, phone in enumerate(phones):
        print(phone, file=outfile)

# Map every phone to itself in lexicon.txt
with open("data/local/dict/lexicon.txt", "w") as outfile:
    sorted_phones = sorted((phones + ["sil"]))
    for i, phone in enumerate(sorted_phones):
        print(f"{phone} {phone}", file=outfile)

# Create lm_train.text
for dir in ["dev", "test", "train"]:
    with open(f"data/local/dict/lm_{dir}.text", "w") as outfile, open(f"data/{dir}/text") as infile:
        for line in infile.readlines():
            # First token is the uttid, the rest is the sentence
            uttid, *sentence = line.split()

            # Add <s> and </s>
            full_line = [uttid] + ["<s>"] + sentence + ["</s>"]
            print(" ".join(full_line), file=outfile)

run_cmd("touch data/local/dict/extra_questions.txt")

run_cmd("cp ../../tools/irstlm/scripts/build-lm.sh scripts/")

# 4.2.2

# Create intermediate unigram and bigram language models
for n in [1, 2]:
    ug_bg = "ug" if n == 1 else "bg"
    run_cmd(f"rm -f data/local/lm_tmp/lm_phone_{ug_bg}.ilm.gz") 
    print(run_cmd(f"bash scripts/build-lm-util.sh data/local/dict/lm_train.text {n} data/local/lm_tmp/lm_phone_{ug_bg}.ilm.gz"))

# 4.2.3

# Compile language model in ARPA format
for n in [1, 2]:
    ug_bg = "ug" if n == 1 else "bg"
    print(run_cmd(f"bash scripts/compile-lm-util.sh data/local/lm_tmp/lm_phone_{ug_bg}.ilm.gz data/local/nist_lm/lm_phone_{ug_bg}.arpa.gz"))

# 4.2.4

# Create FST
print(run_cmd(f"bash scripts/prep_lang-util.sh data/local/dict data/local/lm_tmp data/lang"))

# 4.2.5

# Sort wav.scp, text, utt2spk files
for dir in ["data/dev", "data/test", "data/train"]:
    for file_name in ["wav.scp", "text", "utt2spk"]:
        run_cmd(f"sort {dir}/{file_name} > {dir}/{file_name}~")
        run_cmd(f"mv {dir}/{file_name}~ {dir}/{file_name}")

# 4.2.6

# Run utt2spk_to_spk2utt.pl
for dir in ["data/dev", "data/test", "data/train"]:
    run_cmd(f"perl utils/utt2spk_to_spk2utt.pl {dir}/utt2spk > {dir}/spk2utt")

# question 1
for dir in ["dev", "test"]:
    for ug_bg in ["ug", "bg"]:
        print(run_cmd(f"bash scripts/perplexity-util.sh data/local/lm_tmp/lm_phone_{ug_bg}.ilm.gz data/local/dict/lm_{dir}"))

for dir in ["dev", "test"]:
    for x in ["ug", "bg"]:
        with open(f"perplex-{dir}-{x}", "w") as outfile:
            perplexity_string = ""
            perplexity_string += f"Perplexity for {dir} {x}: "
            for k, v in l[f"{dir}_{x}"].items():
                perplexity_string += f"{k}={v} "
            print(perplexity_string, file=outfile)

# 4.2.7

# Create grammar FST
print(run_cmd("bash scripts/timit_format_data.sh"))

print("4.2 complete")
