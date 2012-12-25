def powerSet(elts):
    if len(elts) == 0:
		return [[]]
	else:
		smaller = powerSet(elts[1:])
		elt = [elts[0]]
		withElt = []
		for s in smaller:
			withElt.append(s+elt)
		allofthem = smaller + withElt
		return allofthem
