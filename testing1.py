
def dna_starts_with(string, prefix):
    return string[0:len(prefix)] == prefix


#neater to push this into a less repetitious form...
assert dna_starts_with("ATC", "A")  #expect true
assert not dna_starts_with("TTC", "A")  #expect false
assert not dna_starts_with("ATC", "TC")  #expect false
assert not dna_starts_with("ATC", "AAAAAAA")  #expect false
assert not dna_starts_with("ATC", "N")  #expect false

#have a list of test inputs and expected results (3D list)

passes = 0
for (seq, prefix, expected) in Tests:
    if ... = expected:

    else:



