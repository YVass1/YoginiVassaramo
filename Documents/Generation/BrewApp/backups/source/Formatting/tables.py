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
    print_counter_var_table("BrewCo Options Menu :)","number","options", my_list)
    #menu_options_dict = dict(enumerate(my_list))
