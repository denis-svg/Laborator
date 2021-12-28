def parser_pattern(pattern):
    pattern += "0"
    out = []
    i = 0
    while i < len(pattern) - 1:
        if pattern[i + 1] == "*":
            out.append(pattern[i] + pattern[i + 1])
            i += 2
            continue
        else:
            out.append(pattern[i])
            i += 1
    return out


def last_char_index(char, string, number):
    if char == "":
        return len(string)
    i = len(string) - 1
    count = 0
    while i > -1:
        if string[i] == char:
            count += 1
            if count == number:
                return i
        i -= 1
    return -1


def match(string, pattern):
    parsed = parser_pattern(pattern)
    formed_str = ""
    i, j = 0, 0
    while i < len(string) and j < len(parsed):
        if len(parsed[j]) == 2:
            if parsed[j][0] == ".":
                k = j + 1
                stop = ""
                while k < len(parsed):
                    if len(parsed[k]) == 1:
                        stop = parsed[k]
                        break
                    k += 1
                count = 0
                it = len(parsed) - 1
                while it > k - 1:
                    if stop == parsed[it]:
                        count += 1
                    it -= 1
                break_index = last_char_index(stop, string, count)
                while i < len(string) and i < break_index != -1:
                    formed_str += string[i]
                    i += 1
                j = k
                continue
            elif parsed[j][0] == string[i]:
                k = j + 1
                while k < len(parsed):
                    if parsed[k] != parsed[j][0]:
                        break
                    k += 1
                t1 = k - (j + 1)
                k2 = i
                while k2 < len(string):
                    if string[k2] != string[i]:
                        break
                    k2 += 1
                t2 = k2 - i

                t3 = t2 - t1
                while t3 > 0:
                    formed_str += string[i]
                    i += 1
                    t3 -= 1
                if t3 < 0:
                    j += 1
                else:
                    j += t3 + 1
                continue
            else:
                j += 1
                continue
        if string[i] == parsed[j] or parsed[j] == ".":
            formed_str += string[i]
            j += 1
            i += 1
            continue
        else:
            break
    if formed_str == string and i == len(string):
        while j < len(parsed):
            if len(parsed[j]) == 1:
                break
            j += 1
    if j == len(parsed) and i == len(string) and formed_str == string:
        return True
    return False


print(match("abbcccd", ".*"))

