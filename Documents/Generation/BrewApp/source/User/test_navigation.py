import unittest
from unittest import mock
import source.User.navigation as nav 


class Test_Navigation_Methods(unittest.TestCase):

    #patching all functions not testing in num_selection
    @mock.patch('builtins.input', return_value = unittest.mock)
    def test_num_selection(self, input1):
        #Arrange
        message = "Enter a number: "
        input1.return_value = "17"
        expected_output = 17
        #Act
        actual_output = nav.num_selection(message)
        #Assert
        self.assertEqual(actual_output, expected_output)
        input1.assert_called_once_with("Enter a number: \n")
    
    
    @mock.patch('builtins.input', return_value = unittest.mock)
    def test_hold(self, input1):
        #Arrange
        input1.return_value = y
        expected_output = "y"
        #Act
        actual_output = hold()
        #Assert
        self.assertEqual(actual_output, expected_output)
        input1.assert_called_once_with("Enter any key to return to main menu: ")


        
    """
    def test_try_again():
        pass

    def test_confirm():
        pass"""

if __name__ == '__main__':
    unittest.main()


