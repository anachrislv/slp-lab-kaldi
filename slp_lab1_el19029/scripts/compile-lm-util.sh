. ./path.sh
. ./cmd.sh

compile-lm $1 -t=yes /dev/stdout | grep -v unk | gzip -c > $2
