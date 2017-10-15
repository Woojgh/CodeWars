'''This function will reverse or rotate the number based on conditions'''


def rr(string, sz):
	thing = ''
	groups = [string[_:_+ sz] for _ in range(0,len(string), sz)]
	if len(groups[-1]) < sz:
		groups.pop()
	for _ in groups:
		num = 0
		for i in list(_):
			num = num + int(i)
		if num % 2 == 0:
			_ = _[::-1]
		else:
			_ += _[0]
			_ = _[1:]
		thing = thing + _
	return thing