===========================================
***PEIRO91 - 16/01/2022 - V1.0.1 ***
===========================================

This program let you record this events:

	1. left mouse click
	2. right mouse click
	3. paste

After recording, it show an input box, to let user choose how many times he want to repeate all the actions
After input, the program will repeat all the action recorded. Seconds between every action is defined in config file.

To run it, check config file to see Function Commands and then launch main.py.

===========================================
***PEIRO91 - 17/01/2022 - V1.0.2 ***
===========================================
Added cmd window dimension in config file

Added possibility to paste a list of value separated by a separator defined in config file. If number of iterations
is greater then length of lists, the program will print from the first element. Example: copying 1&2&3&4, will paste
1 in the first iteration, 2 in the second, 3 in third, 4 in fourth, 1 in fifth, 2 in sixth and so on.

===========================================
***PEIRO91 - 17/01/2022 - V1.0.3 ***
===========================================
Added possibility to paste using normal CTRL + V. When recording, this will paste the string not splitted. When Automating,
it will print the string splitted. It should be only use when you need to paste a single value.

===========================================
***PEIRO91 - 24/01/2022 - V1.0.4 ***
===========================================
Added possibility to select all with CTRL + A and to Backspace with Backspace button.

===========================================
***PEIRO91 - 01/02/2022 - V1.0.5 ***
===========================================
Added possibility to record Enter button.
