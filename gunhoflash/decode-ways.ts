function isDecodable(s: string): boolean {
  if (s[0] === '0') return false;
  const num = parseInt(s);
  return 0 < num && num < 27;
}

function numDecodings(s: string): number {
  // there is one way to decode empty string
  let answerPrev = 1;

  // there is one(or zero) way to decode last character only
  let answerNow = isDecodable(s.substring(s.length - 1)) ? 1 : 0;

  let i = s.length - 1;
  while (i--) {
    const answerPrevPrev = answerPrev;
    answerPrev = answerNow;
    answerNow = (
      // decode 1 character
      isDecodable(s.substring(i, i + 1)) ? answerPrev : 0
    ) + (
      // decode 2 characters
      isDecodable(s.substring(i, i + 2)) ? answerPrevPrev : 0
    );
  }

  return answerNow;
}
