class P36:
    def __init__(self, text):
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        self._text = text         
        self._word_counts = {}     

    def count_words(self):
        try:
            words = self._text.split()
            self._word_counts.clear()

            for word in words:
                word = word.lower()
                self._word_counts[word] = self._word_counts.get(word, 0) + 1

            return self._word_counts

        except Exception as e:
            return f"Unexpected Error: {e}"
