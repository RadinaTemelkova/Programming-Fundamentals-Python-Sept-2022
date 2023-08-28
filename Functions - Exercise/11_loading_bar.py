def loading_bar(current_number):
    result_list = []
    percent_signs_count = current_number // 10
    if percent_signs_count == 10:
        final_result = f"100% Complete!\n[%%%%%%%%%%]"
        return final_result
    for index in range(percent_signs_count):
        result_list.append("%")
    dot_signs_count = 10 - (current_number//10)
    for index in range(dot_signs_count):
        result_list.append(".")
    result_list_as_string = "".join(result_list)
    final_result = f"{current_number}% [{result_list_as_string}]\nStill loading..."
    return final_result


number = int(input())
result = loading_bar(number)
print(result)
