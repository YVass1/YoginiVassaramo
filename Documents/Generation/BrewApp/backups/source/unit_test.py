import source.User.commands as com

def test_add_list_element():
    #Arrange
    test_list = ["John", "Jim", "Jack"]
    test_element = "Julie"
    expected_output = ["John", "Jim", "Jack", "Julie"]
    #Act
    actual_output = com.add_list_element(test_list, test_element)
    #Assert
    assert expected_output == actual_output

def test_remove_list_element():
    #Arrange
    test_list = ["John", "Jim", "Jack"]
    test_element = "Jim"
    expected_output = ["John", "Jack"]
    #Act
    actual_output = com.remove_list_element(test_list,test_element)
    #Assert
    assert expected_output == actual_output

def test_remove_from_dict():
    #Arrange
    test_dict = {"Maria": "Coffee", "John" : "Tea"}
    test_key = "maria"
    expected_output = {"John": "Tea"}
    #Act
    actual_output = com.remove_from_dict(test_dict,test_key)
    #Assert
    assert expected_output == actual_output

def test_add_to_dict():
    #Arrange
    test_dict = {"Maria": "Coffee", "John" : "Tea"}
    test_key = "Yogini"
    test_value = "Water"
    expected_output = {"Maria": "Coffee", "John" : "Tea", "Yogini": "Water"}
    #Act
    actual_output = com.add_to_dict(test_dict,test_key,test_value)
    #Assert
    assert expected_output == actual_output


test_add_list_element()
test_remove_list_element()
test_add_to_dict()
test_remove_from_dict()



