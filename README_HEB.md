# Tacotron2 Hebrew

## Based on [tacotron2/issues/321#issuecomment-603894212](https://github.com/NVIDIA/tacotron2/issues/321#issuecomment-603894212)


## Presquires

[Node](https://nodejs.org/en) | [Python](https://python.org)

## Modifications

Add [data/clean.py](data/clean.py) for clean numbers and symbols from text
Change [text/symbols.py](text/symbols.py) symbols to Latin.
Change [hparams.py][hparams.py] text cleaners to basic.


## Setup

1. Clone the repo

```console
git clone https://github.com/thewh1teagle/tacotron2.git
git submodule init; git submodule update
```

2. Get dataset from [saspeech_gold_standard_v1.0.tar.gz](https://openslr.org/134/)
3. Extract it
4. Put `metadata.csv` inside `data` folder
5. Execute the cleaner

```console
python clean.py
python transliteration.py
python latin_abs_path.py
python check.py
python split_data.py
```

# Install dependencies

[Torch](https://pytorch.org/get-started/locally/)


# Train

```console
python train.py --output_directory=data/outdir --log_directory=data/logdir --training-files data/train_data --validation-files data/validation_data
```