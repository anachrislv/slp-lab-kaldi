from helpers import run_cmd

print("Running 4.1")

# 4.1.1

# Get path.sh and cmd.sh from wsj
run_cmd("cp ../wsj/s5/{path.sh,cmd.sh} ./")

# path.sh: Set KALDI_ROOT
with open("tmp", "w") as outfile, open("path.sh") as used_path:
    for i, line in enumerate(used_path.readlines()):
        if "export KALDI_ROOT" in line:
            line = "export KALDI_ROOT=`pwd`/../..\n"
        print(line, file=outfile, end="")

run_cmd("mv tmp path.sh")

# cmd.sh: Change train_cmd, decode_cmd and cuda_cmd to run.pl
with open("tmp", "w") as outfile, open("cmd.sh") as cmd_scr:
    for i, line in enumerate(cmd_scr.readlines()):
        if "export train_cmd" in line:
            line = "export train_cmd=run.pl\n"
        elif "export decode_cmd" in line:
            line = "export decode_cmd=run.pl\n"
        elif "export cuda_cmd" in line:
            line = "export cuda_cmd=run.pl\n"
        print(line, file=outfile, end="")

run_cmd("mv tmp cmd.sh")

# 4.1.2

# Create softlinks
run_cmd("ln -sf ../wsj/s5/{steps,utils} ./")

# 4.1.3

# Create local directory
run_cmd("mkdir -p local")

# Create link of score.sh to score_kaldi.sh 
run_cmd("ln -sfr steps/score_kaldi.sh local/score.sh")

# 4.1.4

# Create conf folder
run_cmd("mkdir -p conf")

# Move mfcc.conf
run_cmd("mv mfcc.conf conf/")

# 4.1.5

# Create data/lang, data/local/dict, data/local/lm_tmp, data/local/nist_lm
run_cmd("mkdir -p data/lang data/local/dict data/local/lm_tmp data/local/nist_lm")

print("4.1 complete")
