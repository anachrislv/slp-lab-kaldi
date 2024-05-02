# Download important files

pip install gdown

# Download GitHub files

rm -rf slp-labs

# Clone slp-labs
git clone https://github.com/slp-ntua/slp-labs.git

# Copy helpers.py so we can use the run_cmd() function
cp slp-labs/lab1/scripts/helpers.py scripts/

# Copy mfcc.conf and timit_format_data.sh
cp slp-labs/lab2/mfcc.conf ./
cp slp-labs/lab2/timit_format_data.sh scripts/

rm -rf slp-labs

# Download usc.tgz
gdown --fuzzy "https://drive.google.com/file/d/1_mIoioHMeC2HZtIbGs1LcL4kkIF696nB/view?usp=sharing"

tar zxvf usc.tgz

cp -r usc/* ./

# Delete usc.tgz folder (both zipped and unzipped)
rm -r usc/
rm usc.tgz
