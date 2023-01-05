class Trie {
  originalWord: string | undefined;
  subTries: Map<string, Trie>;

  constructor() {
    this.subTries = new Map<string, Trie>();
  }

  addWord(word: string, originalWord: string): void {
    if (word.length) {
      const firstLetter = word[0];
      const subTrie = this.subTries.get(firstLetter) || new Trie();
      subTrie.addWord(word.slice(1), originalWord);
      this.subTries.set(firstLetter, subTrie);
    } else {
      this.originalWord = originalWord;
    }
  }
}

function findWords(board: string[][], words: string[]): string[] {
  const USED = '';
  const foundWords = new Set<string>();

  const search = (r: number, c: number, trie: Trie) => {
    const char = board[r][c];

    const subTrie = trie.subTries.get(char);
    if (subTrie === undefined) {
      return;
    }
    if (subTrie.originalWord) {
      foundWords.add(subTrie.originalWord);
    }

    board[r][c] = USED;
    if (r > 0 && board[r - 1][c] !== USED) search(r - 1, c, subTrie);
    if (c > 0 && board[r][c - 1] !== USED) search(r, c - 1, subTrie);
    if (r < R - 1 && board[r + 1][c] !== USED) search(r + 1, c, subTrie);
    if (c < C - 1 && board[r][c + 1] !== USED) search(r, c + 1, subTrie);
    board[r][c] = char;
  };

  const trie = new Trie();
  words.forEach((word) => trie.addWord(word, word));

  const R = board.length;
  const C = board[0].length;
  for (let r = 0; r < R; r++) {
    for (let c = 0; c < C; c++) {
      search(r, c, trie);
    }
  }

  return Array.from(foundWords.values());
}
