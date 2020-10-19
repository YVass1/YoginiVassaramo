#importing neccessary libraries/functions/methods

import unittest
from unittest import mock
import source.User.commands as com
import source.User.navigation as nav
import source.Formatting.tables as tab

class Test_Commands_Methods(unittest.TestCase):

    def test_add_list_element(self):
        #Arrange
        test_list = ["John", "Jim", "Jack"]
        test_element = "Julie"
        expected_output = ["John", "Jim", "Jack", "Julie"]
        #Act
        actual_output = com.add_list_element(test_list, test_element)
        #Assert
        self.assertEqual(expected_output, actual_output)

    def test_remove_list_element(self):
        #Arrange
        test_list = ["John", "Jim", "Jack"]
        test_element = "Jim"
        expected_output = ["John", "Jack"]
        #Act
        actual_output = com.remove_list_element(test_list,test_element)
        #Assert
        self.assertEqual(expected_output, actual_output)

    def test_remove_from_dict(self):
        #Arrange
        test_dict = {"Maria": "Coffee", "John" : "Tea"}
        test_key = "maria"
        expected_output = {"John": "Tea"}
        #Act
        actual_output = com.remove_from_dict(test_dict,test_key)
        #Assert
        self.assertEqual(expected_output, actual_output)

    def test_add_to_dict(self):
        #Arrange
        test_dict = {"Maria": "Coffee", "John" : "Tea"}
        test_key = "Yogini"
        test_value = "Water"
        expected_output = {"Maria": "Coffee", "John" : "Tea", "Yogini": "Water"}
        #Act
        actual_output = com.add_to_dict(test_dict,test_key,test_value)
        #Assert
        self.assertEqual(expected_output, actual_output)

    #stub person id --> use that for extracting from list
    @mock.patch('source.User.commands.num_selection', return_value = unittest.mock)
    #stub drink_is  --> use that fro extracting from list
    @mock.patch('builtins.input', return_value = unittest.mock)
    #stub confirmation functions too
    @mock.patch('source.User.commands.confirm', return_value = 2)
    #need to stub print table
    @mock.patch('source.Formatting.tables.print_counter_var_table', return_value = None)
    def test_user_add_pref(self, mock_print_menu, confirm1 ,input2 ,input1):
        #Arrange
        my_drinks = ["Tea", "Coffee","Water"]
        my_person = ["James", "Ava", "Teracotta"]
        my_dict = {"Perry": "Fanta"}
        expected_output = {"Perry": "Fanta", "Teracotta": "Tea"}
        input1.return_value = 3
        input2.side_effect = "1"
        #Act
        actual_output = com.user_add_pref(my_person, my_drinks, my_dict)
        #Assert
        self.assertEqual(actual_output, expected_output)
        self.assertEqual(mock_print_menu.call_count, 2)
        self.assertEqual(confirm1.call_count, 1)
        self.assertEqual(input1.call_count, 1)
        self.assertEqual(input2.call_count, 1)

    
    @mock.patch('builtins.input', return_value = unittest.mock)
    #stub confirmation functions too
    @mock.patch('source.User.commands.confirm', return_value = 2)
    #need to stub print table
    @mock.patch('source.Formatting.tables.print_table_dict', return_value = None)
    def test_user_remove_pref(self, mock_print_menu, confirm1 ,input1):
        #Arrange
        my_dict = {"Perry": "Fanta", "Teracotta": "Tea"}
        expected_output = {"Teracotta": "Tea"}
        input1.return_value = "Perry"
        #Act
        actual_output = com.user_remove_pref(my_dict)
        #Assert
        self.assertEqual(actual_output, expected_output)   
        self.assertEqual(mock_print_menu.call_count, 1)
        self.assertEqual(confirm1.call_count, 1)
        self.assertEqual(input1.call_count, 1)
        

if __name__ == '__main__':
    unittest.main()






