from helpers import run_cmd

print("Running 4.3")

# 4.3

for dir in ["train", "dev", "test"]:
    print(run_cmd(f"bash steps/make_mfcc.sh data/{dir}"))

for dir in ["train", "dev", "test"]:
    print(run_cmd(f"bash steps/compute_cmvn_stats.sh data/{dir}"))

print("4.3 complete")
