import unittest
from third_project_withoit_GUI import sort_sequence

class TestSortSequence(unittest.TestCase):

    def test_sort_sequence_invalid_input(self):
        sequence = "5, abc, 8, 1, 6"
        expected_error_message = "Ошибка: could not convert string to float: 'abc'"
        with open("tests.txt", "w") as f:
            sorted_sequence, time_taken = sort_sequence(sequence, "ascending")
            self.assertEqual(sorted_sequence, expected_error_message)
            f.write("Sort Sequence Test:\n")
            f.write(f"Input Sequence: {sequence}\n")
            f.write("Time Taken: " + str(time_taken) + " seconds\n")


    def test_sort_sequence_descending(self):
        sequence = "5, 3, 8, 1, 6"
        expected_sorted_sequence = [8.0, 6.0, 5.0, 3.0, 1.0]
        sorted_sequence, time_taken = sort_sequence(sequence, "descending")
        self.assertEqual(sorted_sequence, expected_sorted_sequence)

if __name__ == '__main__':
    with open("tests.txt", "w") as f:
        runner = unittest.TextTestRunner(stream=f)
        unittest.main(testRunner=runner)
