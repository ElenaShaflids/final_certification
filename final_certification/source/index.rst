This script implements a graphical program using the Tkinter library for sorting a sequence of numbers with the ability to choose the sorting order (ascending or descending).
The program consists of an input field for entering the sequence, a dropdown list for selecting the sorting order, a result text field, and a button to initiate the sorting process.

Logic:
 1. The user inputs a sequence of numbers separated by commas.
 2. The user selects one of the sorting options.
 3. After clicking the "Start" button, the sequence is sorted based on the selected option, and the sorted sequence is displayed in the result text field.
 4. The time taken for sorting is also displayed.

Functions:
 - sort_sequence(): This function retrieves the input sequence, sorts it based on the selected option, and displays the sorted sequence along with the time taken for sorting. It handles possible exceptions such as invalid input format.

Widgets:
 - Entry: Field for entering the sequence of numbers.
 - Combobox: Dropdown list for selecting the sorting order.
 - Button: Initiates the sorting process.
 - Label: Displays instructional text and the result of the sorting process.
 - Text: Displays the sorted sequence.
