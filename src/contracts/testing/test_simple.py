from contracts.main import parse_contract_string
from contracts.testing.utils import check_contract_single_fail, \
    check_contract_single_ok

good_examples = []
fail_examples = []
def good_example(a, b): good_examples.append((a, b))
def fail_example(a, b): fail_examples.append((a, b))

# dummy
good_example('*', 0)
good_example('*', [1])
good_example('*', None)


# Basic comparisons
good_example('=0', 0)
good_example('==0', 0)
fail_example('=0', 1)
fail_example('==0', 1)
fail_example('=0', [0])
good_example('!=0', 1)
fail_example('!=0', 0)
good_example('>0', 1)
fail_example('>0', 0)
fail_example('>0', -1)
good_example('>=0', 1)
good_example('>=0', 0)
fail_example('>=0', -1)
good_example('<0', -1)
fail_example('<0', 0)
fail_example('<0', +1)
good_example('<=0', -1)
good_example('<=0', 0)
fail_example('<=0', +1)

# wrong types
fail_example('>0', [])
# big letters can only bind to numbers
good_example('N,N>0', 1)
fail_example('N,N>0', 0)
fail_example('N', [])


# AND
fail_example('=0,=1', 0)
good_example('=0,>=0', 0)

# OR
good_example('=0|=1', 0)
good_example('=0|=1', 1)
fail_example('=0|=1', 2)


# TODO: error if N matches something except a number. x,y,z 

good_example('int', 1)
fail_example('int', None)
fail_example('int', 2.0)
good_example('float', 1.1)
fail_example('float', None)
fail_example('float', 2)


good_example('list', [])
fail_example('list', 'ciao')
good_example('list[*]', [])
good_example('list[*]', [1])
good_example('list[*](*)', [1])
good_example('list[*](float)', [1.0])
fail_example('list[*](float)', [1])

good_example('=1', 1)
fail_example('=1', [1])
good_example('list[=1]', [0])
good_example('list[=2]', [0, 1])
fail_example('list[=2]', [0])
good_example('list[1]', [0]) # shortcut
good_example('list[2]', [0, 1])
fail_example('list[2]', [0])
good_example('list(int)', [])
good_example('list(int)', [0, 1])
fail_example('list(int)', [0, 'a'])
fail_example('list(int)', [0, 'a'])
good_example('list(int,>0)', [2, 1])
fail_example('list(int,>0)', [0, 1])
good_example('list(int,=0)', [0, 0])

# with parametric lengths 
good_example('list[N]', [])
good_example('list[N],N>0', [1])
good_example('list[N],N=1', [1])
good_example('list[N],N>0,N<2', [1])
fail_example('list[N],N>0', [])

   
def test_simple_expressions_ok():
    for contract, value in good_examples:
        yield check_contract_single_ok, contract, value

def test_simple_expressions_fail():
    for contract, value in fail_examples:
        yield check_contract_single_fail, contract, value
        
if False:
    for contract, value in (good_examples + fail_examples):
        parsed = parse_contract_string(contract)
        if str(parsed) == contract:
            mark = ' '
        else:
            mark = '~'
            
        print '{0:>20} {1:>20}  {2}'.format(contract, parsed, mark)

