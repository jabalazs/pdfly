# pdfly

Simple script for extracting pages from or merging PDF files.

# Dependencies
* Python 3
* pikepdf

# Installation

```
git clone https://github.com/jabalazs/pdfly
cd pdfly
pip install -r requirements.txt
```

# Usage Examples

## Extracting pages

To extract the first 3 pages of `document1.pdf` and save them as `out.pdf` we
can execute:

```
python pdfly.py extract document1.pdf out.pdf 1 3
```

## Merging PDF files

To merge `document1.pdf`, `document2.pdf` and `document3.pdf` into `merged.pdf`
we can execute:

```
python pdfly.py merge document1.pdf document2.pdf document3.pdf -o merged.pdf
```
