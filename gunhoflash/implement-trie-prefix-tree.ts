class Trie {
  hasValue: boolean;
  subTrie: Map<string, Trie>;

  constructor() {
    this.hasValue = false;
    this.subTrie = new Map<string, Trie>();
  }

  insert(word: string): void {
    if (word.length) {
      const firstLetter = word[0];
      const subTrie = this.subTrie.get(firstLetter) || new Trie();
      subTrie.insert(word.slice(1));
      this.subTrie.set(firstLetter, subTrie);
    } else {
      this.hasValue = true;
    }
  }

  search(word: string): boolean {
    if (word.length) {
      const firstLetter = word[0];
      const subTrie = this.subTrie.get(firstLetter);
      return !!subTrie && subTrie.search(word.slice(1));
    } else {
      return this.hasValue;
    }
  }

  startsWith(prefix: string): boolean {
    if (prefix.length) {
      const firstLetter = prefix[0];
      const subTrie = this.subTrie.get(firstLetter);
      return !!subTrie && subTrie.startsWith(prefix.slice(1));
    } else {
      return this.hasValue || this.subTrie.size > 0;
    }
  }
}
