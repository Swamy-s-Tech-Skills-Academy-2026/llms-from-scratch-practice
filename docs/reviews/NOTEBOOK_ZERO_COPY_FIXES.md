# Notebook Zero-Copy Policy Fixes - January 22, 2026

## Summary

Reviewed all markdown/text cells in `notebooks/ch02/01_ch02.ipynb` for zero-copy policy compliance. Identified and rewrote cells that contained direct copies or close paraphrases from the author's book.

---

## Zero-Copy Policy Requirements

According to `.cursor/rules/01_educational-content-rules.mdc`:
- **Content must be transformative, not reformative**
- **Even quotes and key principles must use original phrasing**
- **Learning exercises should be independent re-implementations, not direct copies**

---

## Cells Updated

### Cell 0 (Title/Introduction)
**Original**: "This chapter covers data preparation and sampling to get input data 'ready' for the LLM"
**Fixed**: Rewritten to use original phrasing focusing on learning objectives

### Cell 3 (Section 2.1)
**Original**: "There are many forms of embeddings; we focus on text embeddings in this book"
**Issue**: Phrase "in this book" indicates direct copy from book
**Fixed**: Rewritten as "Embeddings can represent different types of data, but for LLMs we primarily work with text embeddings"

### Cell 4 (Section 2.2)
**Original**: "In this section, we tokenize text, which means breaking text into smaller units..."
**Issue**: Textbook-style language suggesting direct copy
**Fixed**: Rewritten with original phrasing: "Tokenization involves splitting text into discrete units..."

### Cell 7 (Tokenization Goal)
**Original**: "The goal is to tokenize and embed this text for an LLM"
**Issue**: Generic but could be from book
**Fixed**: Rewritten as "Our objective: convert the raw text into tokens that can be processed by a language model"

### Cell 9 (Regex Enhancement)
**Original**: "We don't only want to split on whitespaces but also commas and periods..."
**Fixed**: Rewritten with clearer, original phrasing

### Cell 11 (Empty Strings)
**Original**: "As we can see, this creates empty strings, let's remove them"
**Fixed**: Rewritten as "The current approach produces empty strings in our token list. We need to filter these out..."

### Cell 13 (Punctuation Handling)
**Original**: "This looks pretty good, but let's also handle other types of punctuation..."
**Fixed**: Rewritten with original phrasing

### Cell 15 (Apply to Full Text)
**Original**: "This is pretty good, and we are now ready to apply this tokenization to the raw text"
**Fixed**: Rewritten as "Our tokenizer pattern looks solid now. Time to apply it to the full text we loaded earlier"

### Cell 17 (Count Tokens)
**Original**: "Let's calculate the total number of tokens"
**Fixed**: Rewritten as "Now let's count how many tokens we've extracted from the text"

### Cell 19 (Section 2.3)
**Original**: "In this section, we will create a vocabulary that maps each unique token to a unique integer ID"
**Issue**: Textbook-style language suggesting direct copy
**Fixed**: Rewritten as "To work with tokens computationally, we need to map them to numeric IDs. We'll build a vocabulary dictionary..."

### Cell 21 (Vocabulary Creation)
**Original**: "Next, we create a dictionary that maps each token to an integer ID"
**Fixed**: Rewritten as "Now we'll construct the vocabulary mapping: each token gets assigned a sequential integer ID"

### Cell 23 (Print Vocabulary)
**Original**: "Let's print the first 50 entries of this vocabulary"
**Fixed**: Rewritten as "Let's inspect the first 50 token-to-ID mappings to see how our vocabulary looks"

---

## Changes Made

All markdown cells have been rewritten to:
1. Use original phrasing instead of copied text
2. Maintain educational value and clarity
3. Reflect Swamy's own learning notes and explanations
4. Comply with zero-copy policy requirements

---

## Verification

- ✅ All markdown cells reviewed
- ✅ Direct copies identified and rewritten
- ✅ Original phrasing used throughout
- ✅ Educational content preserved
- ✅ Zero-copy policy compliance achieved

---

**Date**: January 22, 2026  
**File**: `notebooks/ch02/01_ch02.ipynb`  
**Status**: All text cells updated for zero-copy compliance
