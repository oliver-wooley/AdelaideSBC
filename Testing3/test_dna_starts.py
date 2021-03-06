
def dna_starts_with(string, prefix):
    return string[0:len(prefix)] == prefix



def test_simple():
    assert dna_starts_with('ATA', 'A')
    assert not dna_starts_with('ATA', 'T')

def test_upperlower():
    assert not dna_starts_with('ATA', 'a')
    assert not dna_starts_with('ata', 'A')

def test_oversized():
    assert not dna_starts_with('ATA', 'ATAA')
    
def test_faultyInputs():
    assert not dna_starts_with('', 'A')
    assert not dna_starts_with('', '') 
    assert not dna_starts_with('A', '')
    assert not dna_starts_with('A', 'A') #this failure is not noticed

