from helpers import run_cmd
import os
import re

#Part 3 - prep part

#Create the directories
run_cmd("mkdir -p data")
run_cmd("mkdir -p data/{dev,test,train}")

#Create a dictionary from all the transcriptions
with open("transcriptions.txt") as infile:
    lines = infile.read().splitlines()
    transcriptions = dict([line.split("\t") for line in lines])

#Create a dictionary for all mappings
with open("lexicon.txt") as infile:
    lines = infile.read().splitlines()

    lines = [line.lower() for line in lines]

    #For multiple voicings keep one
    lines = [re.sub("\(\d\)", "", line) for line in lines]

    lexicon = dict([line.split("\t") for line in lines])

dirs = [
    ("train", "training.txt"),
    ("dev", "validation.txt"),
    ("test", "testing.txt"),
]

for (dir, file_name) in dirs:
    run_cmd(f"cp filesets/{file_name} data/{dir}/uttids")

    # Create "uttids"
    with open(f"data/{dir}/uttids") as f_uttids:
        uttids = f_uttids.read().splitlines()

        # Create "utt2spk"
        with open(f"data/{dir}/utt2spk", "w") as f_utt2spk:
            speakers = [uttid.split("_")[0] for uttid in uttids]
            for uttid, speaker in zip(uttids, speakers):
                print(f"{uttid} {speaker}", file=f_utt2spk)

        # Create "wav.scp"
        with open(f"data/{dir}/wav.scp", "w") as f_wav:
            for uttid in uttids:
                wavpath = os.path.realpath(f"wav/{uttid}.wav")
                print(f"{uttid} {wavpath}", file=f_wav)

        # Create text files
        with open(f"data/{dir}/text_orig", "w") as f_text_orig, open(f"data/{dir}/text", "w") as f_text:
            for uttid in uttids:
                sentence_id = uttid.split("_")[1]
                sentence = transcriptions[sentence_id]

                print(f"{uttid} {sentence}", file=f_text_orig)

                sentence = sentence.lower()

                sentence = re.sub("-", " ", sentence)
                sentence = re.sub("[^a-zA-Z' ]", "", sentence)
                phonemes = [lexicon[word] for word in sentence.split()]
                print(f"{uttid} sil{''.join(phonemes)} sil", file=f_text)

print("prep is complete")
