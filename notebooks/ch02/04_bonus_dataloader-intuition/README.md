# Bonus: Dataloader Intuition with Simple Numbers

**Purpose**: Understanding the sliding-window dataloader before applying it to real text.

## Why I'm Doing This

When I first saw the `GPTDatasetV1` class, it wasn't obvious to me how the sliding-window logic worked — especially how `input_ids` and `target_ids` relate to each other. Replacing text with small integers makes the mechanics visible.

## What's in This Folder

### `dataloader-intuition.ipynb`

I use `number-data.txt` (simple integer sequences) instead of real text to trace:
- How the stride and window size determine the number of samples
- Why `target_ids` is just `input_ids` shifted by one position
- How batch size, shuffle, and sequence length interact

**My takeaway**: The dataloader is teaching the model to predict the next token. Every sample is just a window of token IDs where the label is the same window shifted right by one. Once I saw this with numbers, the text version made complete sense.

## Source Attribution

Concepts derived from *Build a Large Language Model From Scratch* (Raschka), Chapter 2 bonus material.  
Implementation is my own reconstruction — not a copy of the source-material notebook.
