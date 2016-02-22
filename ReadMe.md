# Merchant Guide to Galaxy

python implementation of merchant guide to galaxy.

You can resolve this problem by IntergalaticTransaction.


### 1. Set input as the condition

You can get conditions as below:

    glob is I
    prok is V
    pish is X
    tegj is L
    glob glob Silver is 34 Credits
    glob prok Gold is 57800 Credits
    pish pish Iron is 3910 Credits

### 2. Resolve the problems:

    how much is pish tegj glob glob ?
    how many Credits is glob prok Silver ?
    how many Credits is glob prok Gold ?
    how many Credits is glob prok Iron ?
    how much wood could a woodchuck chuck if a woodchuck could chuck= wood ?

### 3. Using the implementation to get the result:


    >>> from src.intergalaticTransaction import *
    >>> 
    >>> intergalaTrans = IntergalaticTransaction()
    >>> intergalaTrans.SetCondition("glob is I")
    True
    >>> intergalaTrans.SetCondition("prok is V")
    True
    >>> intergalaTrans.SetCondition("pish is X")
    True
    >>> intergalaTrans.SetCondition("tegi is L")
    True
    >>> intergalaTrans.SetCondition("glob glob Silver is 34 Credits")
    True
    >>> intergalaTrans.SetCondition("glob prok Gold is 57800 Credits")
    True
    >>> intergalaTrans.SetCondition("pish pish Iron is 3910
    >>> intergalaTrans.CalculateResult("pish tegi glob glob")
    42
    >>> intergalaTrans.CalculateResult("glob prok Silver")
    68.0
	>>> intergalaTrans.CalculateResult("glob prok Gold")
    57800.0
	>>> intergalaTrans.CalculateResult("glob prok Iron")
    782.0
	>>> intergalaTrans.CalculateResult("wood could a woodchuck chuck if a woodchuck could chuck wood")
    'I have no idea what you are talking about'

