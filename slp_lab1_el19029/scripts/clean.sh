WORK_DIR=$(pwd | rev | cut -d "/" -f1 | rev)

mkdir -p ../tmp
cp -r main.sh scripts/ ../tmp/

rm -r *

cp -r ../tmp/* ../"$WORK_DIR"

rm -r ../tmp
