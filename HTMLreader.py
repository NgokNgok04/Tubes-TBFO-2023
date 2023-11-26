def get_raw_list(file_html):
    raw_list = []

    with open(file_html, 'r', encoding='utf-8') as file:
        html_content = file.read()
        words = html_content.split()

        for word in words:
            raw_list.append(word.lower())

    return raw_list


def get_remainding_input(file_html) :
    
    input_list = get_raw_list(file_html)
    print(input_list , "\n\n\n")


    # Inisialisasi daftar untuk menyimpan hasil
    result_list = []
    validation = ['method="', 'type="']

    att = ["class", "id", "style", "rel", "href", "src", "alt", "type",
                   "action", "method", "get", "post", "text", "password", "email",
                   "number", "checkbox", "submit", "reset", "button"]

    isTutup = False
    isComment = False
    isInAtt = False
    is_need_validation = False

    # Iterasi setiap elemen dalam input_list
    currstr = ""
    for element in input_list:
        for char in element : 
            # if currstr in att : isatt = True
            
            if char == '>':
                if  isTutup : 
                    currstr += char
                    result_list.append(currstr)
                    currstr = ""
                    isTutup = False
                elif isComment: 
                    currstr += char
                    result_list.append("&%")
                    currstr = ""
                    isComment = False
                else :
                    result_list.append(currstr)
                    currstr = ""
                    result_list.append(char)
                # isatt = False
            elif char == '"': 
                currstr += char
                if currstr in validation :
                    result_list.append(currstr)
                    currstr = ""
                    is_need_validation = True
                    isInAtt = True
                elif currstr[:-2] in att : 
                    result_list.append(currstr)
                    isInAtt = True
                elif isInAtt : 
                    if (result_list[-1])[:-2] in att : 
                        if is_need_validation : 
                            result_list.append(currstr)
                        else :
                            result_list.append('%"')

                    else : 
                        result_list.append(currstr)
                    currstr = ""
                    isInAtt = False 
                    is_need_validation = False
            elif not isComment and currstr + char == '<!--':
                currstr = "<!--" + char
                isComment = True
                isTutup = False
                # isatt = False
            elif not isTutup and len(currstr) > 1 and currstr[-1] == "/" and currstr[-2] == "<":
                result_list.append(currstr[:-2])
                currstr = "</" + char
                isTutup = True
                # isatt = False
            else : 
                currstr += char; 
        
        
        if  not(isTutup) and not(isComment) and not isInAtt and not is_need_validation:    
            result_list.append(currstr)
            currstr = ""

    # Hapus string kosong dari result_list
    result_list = [element.strip() for element in result_list if element.strip()]

    print(result_list)
    return result_list
