class WordDictionary {
  hasValue: boolean;
  subDictionary: Map<string, WordDictionary>;

  constructor() {
    this.hasValue = false;
    this.subDictionary = new Map<string, WordDictionary>();
  }

  addWord(word: string): void {
    if (word.length) {
      const firstLetter = word[0];
      const subDictionary = this.subDictionary.get(firstLetter) || new WordDictionary();
      subDictionary.addWord(word.slice(1));
      this.subDictionary.set(firstLetter, subDictionary);
    } else {
      this.hasValue = true;
    }
  }

  search(word: string): boolean {
    if (word.length) {
      const firstLetter = word[0];
      if (firstLetter === '.') {
        return Array.from(this.subDictionary).some(([, subDictionary]) => subDictionary.search(word.slice(1)));
      } else {
        return !!this.subDictionary.get(firstLetter)?.search(word.slice(1));
      }
    } else {
      return this.hasValue;
    }
  }
}
