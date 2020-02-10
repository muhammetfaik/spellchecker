import jamspell

corrector = jamspell.TSpellCorrector()
corrector.LoadLangModel('en.bin')

print(corrector.FixFragment('I am the begt spell cherken!'))
# u'I am the best spell checker!'

print(corrector.GetCandidates(['i', 'am', 'the', 'begt', 'spell', 'cherken'], 3))
# (u'best', u'beat', u'belt', u'bet', u'bent', ... )

print(corrector.GetCandidates(['i', 'am', 'the', 'begt', 'spell', 'cherken'], 5))
# (u'checker', u'chicken', u'checked', u'wherein', u'coherent', ...)
corrector.TrainLangModel('sherlockholmes.txt','alphabet_en.txt','en.bin')
corrector.FixFragmentNormalized('sherlockholmes.txt')
corrector.GetCandidatesRaw()
corrector.SetMaxCandiatesToCheck()
corrector.SetPenalty()