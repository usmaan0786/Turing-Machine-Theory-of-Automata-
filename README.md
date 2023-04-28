# Turing-Machine-Theory-of-Automata-

language {𝑎n𝑏2n𝑐3n | where n belongs to Natural numbers}

Descriptive Definition:
b’s followed by a’s and c’s followed by a’s then b’s are twice times of a’s and number of c’s are thrice times of a’s.

Words:
{abbccc,  aabbbbccccccc, aaabbbbbbccccccccc, aaaabbbbbbbbcccccccccccc, aaaaabbbbbbbbbbccccccccccccccc, aaaaaabbbbbbbbbbbbcccccccccccccccccc, aaaaaaabbbbbbbbbbbbbbccccccccccccccccccccc, aaaaaaaabbbbbbbbbbbbbbbbcccccccccccccccccccccccc,...}


Report:

In this Turing Machine I made the Logic that in every go the first starting a is replaced with X then two b’s replaced with Y and then three starting c’s replaced with Z. This happens again and again till all a’s , b’s and c’s will not converted into X , Y and Z. 

e.g : 

consider the String aabbbbcccccc when it is going to the right it replaces the string in this format XaYYbbZZZccc after replacing third c it moves towards Left and move until it finds X. Now he finds X and again moving towards right the string becomes (B XXYYYYZZZZZZ B)  now it is again moving towards left in search of X and if he finds it he checks for a if there is no a it means all b’s and c’s are converted into Y and Z Now my tape is moving towards right direction and when It finds B it goes to the HALT state.
