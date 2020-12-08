import sys

def checkExpression(expression):
	reg = re.compile('[0-9X\s\^\-\+\*\=\.\/]+$')
	const = re.search('(?<=[^X])\^', expression)
	const2 = re.search('\^(?![0-9])', expression)
	const3 = re.search('(?<=\d)\s(?=\d)', expression)

	if not reg.match(expression):
		print('Wrong characters in expression.')
		return False
	if const is not None or const2 is not None or const3 is not None:
		print('Eh buddy the Polynome is not well formatted.')
		return False
	return True

def printResult(result):

	if result['solution'] is None:
		print('The Solution has only real numbers')

	elif result['solution'] == False:
		print('There is no answer to this expression')

	else:
		if result['discriminant'] is None and result['degree'] == 1:
			print('Polynomial degree: 1')
			print('The solution is:\n{}'.format(result['solution1']))
		elif result['discriminant'] == 0 and result['degree'] == 2:
			print('Polynomial degree: 2')
			print('Discriminant is null, the solutions is:\n{}'.format(result['solution1']))
		elif result['discriminant'] < 0 and result['degree'] == 2:
			print('Polynomial degree: 2')
			print('Discriminant is strictly negative, the two solutions are:\n{}\n{}'.format(result['solution1'], result['solution2']))
		else:
			print('Polynomial degree: 2')
			print('Discriminant is strictly positive, the two solutions are:\n{}\n{}'.format(result['solution1'], result['solution2']))

