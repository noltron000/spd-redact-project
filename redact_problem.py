def redact_words(original, redacted):
	'''
	likely one of the slower solutions.
	compare each redacted word to all the original words.
	return a list of words that don't match, called modified.
	---
	best & worst time: O(n*m)
	'''
	modified = []
	for word in original:
		found = False

		for bad_word in redacted:
			if word != bad_word:
				found = True
				break

		if found:
			modified.append(word)

	print(modified)
	return modified
