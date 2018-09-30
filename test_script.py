import chances

r = chances.Randomizer(100, 10)

nums = r.ambience()
print('Ambience passed')
nums = r.halton()
print('Halton passed')
nums = r.korobov_matrix()
print('Korobov passed')
nums = r.latin_improved()
print('Latin improved passed')
nums = r.latin_matrix()
print('Latin passed')
nums = r.latin_sudoku()
print('Latin sudoku passed')
nums = r.quantum()
print('Quantum passed')
nums = r.sobol()
print('Sobol passed')
nums = r.uniform_crypto()
print('Crypto passed')
nums = r.uniform_mersenne()
print('Mersenne passed')

# chances.oned(nums)
# print('1d plot passed')
# chances.twod(nums)
# print('2d plot part 1/2 passed')
# chances.twod(nums, nums)
# print('2d plot part 2/2 passed')
