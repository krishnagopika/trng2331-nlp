# 04_ngram_hands_on.py
"""
HANDS-ON: Modify this n-gram generator

TASKS:
1. Try different values of n (2, 3, 4)
2. Use your own text corpus
3. Add smoothing for unseen n-grams
"""

from collections import defaultdict, Counter
import random
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt', quiet=True)

class SimpleNGram:
    """Simplified n-gram model for experimentation"""
    
    def __init__(self, n=2):
        self.n = n
        self.ngrams = defaultdict(Counter)
    
    def train(self, text):
        """Train on text"""
        tokens = word_tokenize(text.lower())
        tokens = ['<START>'] * (self.n - 1) + tokens + ['<END>']
        
        for i in range(len(tokens) - self.n + 1):
            context = tuple(tokens[i:i + self.n - 1])
            next_word = tokens[i + self.n - 1]
            self.ngrams[context][next_word] += 1
    
    def generate(self, max_words=15, seed=None):
        """Generate text"""
        if seed:
            random.seed(seed)
        
        context = list(['<START>'] * (self.n - 1))
        result = []
        
        for _ in range(max_words):
            context_tuple = tuple(context[-(self.n-1):])
            
            if context_tuple not in self.ngrams:
                break
            
            next_words = self.ngrams[context_tuple]
            next_word = random.choices(
                list(next_words.keys()),
                weights=list(next_words.values())
            )[0]
            
            if next_word == '<END>':
                break
            
            result.append(next_word)
            context.append(next_word)
        
        return ' '.join(result)


# TODO: Students modify this part!
def main():
    """
    EXPERIMENT HERE:
    1. Change the corpus
    2. Try n=2, n=3, n=4
    3. Generate multiple examples
    """
    
    # TODO: Try your own text!
    corpus = """
    The quick brown fox jumps over the lazy dog.
    The quick brown dog runs through the lazy fox.
    A lazy cat sleeps on the brown mat.
    The brown cat jumps over the quick dog.
    """ * 5  # Repeat to have more data
    
    # TODO: Experiment with different n values
    n = 2  # Try 2, 3, 4
    
    print(f"Training {n}-gram model...")
    model = SimpleNGram(n=n)
    model.train(corpus)
    
    print(f"\nGenerated sentences (n={n}):")
    print("-" * 50)
    
    for i in range(5):
        generated = model.generate()
        print(f"{i+1}. {generated}")


if __name__ == "__main__":
    main()