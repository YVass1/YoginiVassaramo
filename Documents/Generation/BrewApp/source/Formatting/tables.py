#variables
additional_char= 2
#functions

def table_width_1_col(heading, my_list):
    """Determines the largest length from specified list 
elements and heading for 1-column table width."""
    width = len(heading)
    len(heading)
    for element in my_list:
        if len(element) > width:
            width = len(element)
    return width + additional_char

def line_divider(width):
    "Prints line of specified width."
    print( "+"+"="*width+"+")

def print_table_list(heading, my_list):
    """Prints 1-column table, containing specified list elements."""
    width = table_width_1_col(heading, my_list)
    line_divider(width)
    print("|" + heading.upper().center(width) +"|") 
    line_divider(width)
    for element in my_list:
        print("|" + element.capitalize().center(width) +"|")
    line_divider(width)

def table_width_2_col(heading, sub_head1, sub_head2, my_list):
    """Determines largest length from list elements and sub-headings for 
width required for 2-column table."""
    width = len(heading) 
    sub_head_width = len(sub_head1) + len(sub_head2) + 3
    if width < sub_head_width:
        width = sub_head_width
    for value in my_list:
        if len(value) + 4 + len(sub_head1) > width:
            width = len(value) + 4 + len(sub_head1)
    return width + additional_char

def print_counter_var_table(heading, sub_head1, sub_head2, my_list):
    """Prints 2-column table containing specified list
elements and corresponding counter value."""
    width = table_width_2_col(heading,sub_head1, sub_head2, my_list)
    line_divider(width)
    print("|" + heading.upper().center(width) +  "|")
    line_divider(width)
    print(f"|{sub_head1.upper().center(len(sub_head1)+2)}|" + f"{sub_head2.upper().center(width-len(sub_head1)-3)}" + "|")
    line_divider(width)
    counter = 1
    for counter, value in enumerate(my_list, counter):
        print("|"+ str(counter).center(len(sub_head1)+2) + f"| " + str(value).capitalize() + " "*(width - len(str(sub_head1)) -4 - len(value) ) + "|")#.center(width -len(sub_head1) -3)
    line_divider(width)

def print_table_dict(heading, sub_head1, sub_head2, my_dict):
    """Prints 2-column table containing specified dictionary
keys and values in the columns."""
    width = len(heading)
    longest_col1 = len(sub_head1)
    longest_col2 = len(sub_head2)
    for key,value in my_dict.items():
        if len(key) > longest_col1:
            longest_col1 = len(key)
        if len(value) == None:
            pass
        elif len(value)> longest_col2:
            longest_col2 = len(value)
    width = longest_col2 + longest_col1 + additional_char + 3
    line_divider(width)
    print("|" + heading.upper().center(width) + "|")
    line_divider(width)
    print(f"|{sub_head1.upper().center(longest_col1+2)}" + "|" +
    f"{sub_head2.upper().center(width- longest_col1-3)}" + "|")
    line_divider(width)
    counter = 1
    for counter, (key,value) in enumerate(my_dict.items(), counter):
        print(f"| {key.center(longest_col1)}" + " |" + value.center(width - longest_col1 -3) + "|")
    line_divider(width)

def print_menu_options(my_list):
    #save_list("menu_options.csv", my_list)
    print_counter_var_table("BrewCo :)","number","options", my_list)
    #menu_options_dict = dict(enumerate(my_list))



"******************************************************************************************************"
"******************************************************************************************************"
"******************************************************************************************************"
"******************************************************************************************************"
"******************************************************************************************************"

additional_char = 2

def line_divider(width):
    "Prints line of specified width."
    print( "+"+"="*width+"+")

def longest_word(sub_heading, col_list):
    longest_word = len(sub_heading)
    for item in col_list:
        if len(item) > longest_word:
            longest_word = len(item)
    return longest_word

def long_col1(all_rounds_object_list):
    col_list1 = [obj.round_id for obj in all_rounds_object_list]
    longest_col1 = longest_word("Round ID", col_list1)
    return longest_col1

def long_col2(all_rounds_object_list):
    col_list2 = [obj.owner for obj in all_rounds_object_list]
    longest_col2 = longest_word("Round ID", col_list2)
    return longest_col2

def long_col3(all_rounds_object_list):
    col_list3 = [obj.brewer for obj in all_rounds_object_list]
    longest_col3 = longest_word("Brewer", col_list3)
    return longest_col3

def long_col4(all_rounds_object_list):
    col_list4 = [obj.active_status for obj in all_rounds_object_list]
    longest_col4 = longest_word("Active Status", col_list4)
    return longest_col4


def all_rounds_table_width(heading, sub_head1, sub_head2, sub_head3, sub_head4, longest_col1,longest_col2, longest_col3, longest_col4):
    width = len(heading) 
    sub_head_width = len(sub_head1) + len(sub_head2) + len(sub_head3)+ len(sub_head4)+ 3*3
    if width < sub_head_width:
        width = sub_head_width
    if longest_col1 + longest_col2 + longest_col3 + longest_col4 + 3*3 > width:
        width = longest_col1 + longest_col2 + longest_col3 + longest_col4 + 3*3
    return width + additional_char

def print_all_rounds_table(object_list, heading, sub_head1, sub_head2, sub_head3, sub_head4, width, longest_col1, longest_col2, longest_col3, longest_col4):
    
    line_divider(width)
    print("|" + heading.upper().center(width) + "|")
    line_divider(width)
    print(f"|{sub_head1.upper().center(longest_col1+2)}" + "|" +
    f"{sub_head2.upper().center(longest_col2+2)}"+ "|" +
    f"{sub_head3.upper().center(longest_col3+2)}"+ "|" +
    f"{sub_head4.upper().center(longest_col4+2)}"
    + "|")
    line_divider(width)
    for obj in object_list:
        print(f"| " + obj.round_id.center(longest_col1) +
         " |" + obj.owner.center(longest_col2+2)
         + "|" + obj.brewer.center(longest_col3+2)
         + "|" + obj.active_status.center(longest_col4 +2)
         + "|")
    line_divider(width)



def long_col1_round_history(round_history_list):
    col_list1 = [my_dict["OrderID"] for my_dict in round_history_list]
    longest_col1 = longest_word("Order ID", col_list1)
    return longest_col1

def long_col2_round_history(round_history_list):
    col_list2 = [my_dict["Name"] for my_dict in round_history_list]
    longest_col2 = longest_word("Name", col_list2)
    return longest_col2

def long_col3_round_history(round_history_list):
    col_list3 = [my_dict["Drink"] for my_dict in round_history_list]
    longest_col3 = longest_word("Drink", col_list3)
    return longest_col3

def round_history_table_width(heading, sub_head1, sub_head2, sub_head3, longest_col1,longest_col2, longest_col3):
    width = len(heading) 
    sub_head_width = len(sub_head1) + len(sub_head2) + len(sub_head3)+ 3*2
    if width < sub_head_width:
        width = sub_head_width
    if longest_col1 + longest_col2 + longest_col3 + 3*2 > width:
        width = longest_col1 + longest_col2 + longest_col3  + 3*2
    return width + additional_char

def print_round_history(round_history_list, width, heading, sub_head1, sub_head2, sub_head3, long_col1, long_col2, long_col3):
    line_divider(width)
    print("|" + heading.upper().center(width) + "|")
    line_divider(width)
    print(f"|{sub_head1.upper().center(long_col1+2)}" + "|" +
    f"{sub_head2.upper().center(long_col2+2)}"+ "|" +
    f"{sub_head3.upper().center(long_col3+2)}"+ "|")
    line_divider(width)
    for my_dict in round_history_list:
        print(f"| " + my_dict["OrderID"].center(long_col1) +
        " |" + my_dict["Name"].center(long_col2+2)
        + "|" + my_dict["Drink"].center(long_col3+2)
        + "|")
    line_divider(width)