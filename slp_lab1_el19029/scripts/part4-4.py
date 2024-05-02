from helpers import run_cmd

print("Running 4.4")

# 4.4.1

# Train monophone GMM-HMM acoustic model
print(run_cmd("bash steps/train_mono.sh data/train data/lang exp/mono"))


# 4.4.2

# Create HCLG graph
for ug_or_bg in ["ug", "bg"]:
    print(run_cmd(f"bash utils/mkgraph.sh data/lang_phones_{ug_or_bg} exp/mono exp/mono_graph_{ug_or_bg}")) # TODO why lang_phones_{} instead of lang?


# 4.4.3

# Use Viterbi algorithm
for ug_or_bg in ["ug", "bg"]:
    for dir in ["dev", "test"]:
        print(run_cmd(f"bash steps/decode.sh exp/mono_graph_{ug_or_bg} data/{dir} exp/mono/decode_{dir}_{ug_or_bg}"))


# 4.4.5

# Align phones using monophone model
print(run_cmd("bash steps/align_si.sh data/train data/lang exp/mono exp/mono_ali"))


# Train triphone model
print(run_cmd("bash steps/train_deltas.sh 2000 10000 data/train data/lang exp/mono_ali exp/tri1"))


# Create HCLG graph like before
for ug_or_bg in ["ug", "bg"]:
    print(run_cmd(f"bash utils/mkgraph.sh data/lang_phones_{ug_or_bg} exp/tri1 exp/tri1_graph_{ug_or_bg}"))


# Use Viterbi algorithm like before
for ug_or_bg in ["ug", "bg"]:
    for dir in ["dev", "test"]:
        print(run_cmd(f"bash steps/decode.sh exp/tri1_graph_{ug_or_bg} data/{dir} exp/tri1/decode_{dir}_{ug_or_bg}"))


print("4.4 complete")
