import sys

def printResult(result):

	if result['solution'] is None:
		print('Solution is all real numbers')

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
