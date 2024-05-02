# LAB 2: Speech recognition with Kaldi toolkit

## Setup


The directory structure should look like this:

```
kaldi
├── egs
    ├── usc
        ├── main.sh
        ├── scripts
            ├── build-lm.sh
            ├── build-lm-util.sh
            ├── compile-lm-util.sh
            ├── clean.sh
            ├── get_deps.sh
            ├── perplexity-util.sh
            ├── prep_lang-util.sh
            ├── part3.sh
            ├── part4-1.sh
            ├── part4-2.sh
            ├── part4-3.sh
            ├── part4-4.sh  
```

## Task implementation

To run all the parts of the exercise, execute the main.sh script from the usc dir. which is our working directory. This will clean the directory from all files except  our scripts, download all the necessary data and the rest of scripts and run all parts of the exercise.
