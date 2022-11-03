function hash(str: string): string {
  return str.split('').sort().join('');
}

function groupAnagrams(strs: string[]): string[][] {
  const map = new Map<string, string[]>();

  for (const str of strs) {
    const h = hash(str);
    if (!map.has(h)) {
      map.set(h, []);
    }
    map.get(h)!.push(str);
  }

  return Array.from(map.values());
}
