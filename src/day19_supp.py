def get_messages(num, rules_raw, rules_fin):
    """
    Get valid messages for given rule number
    """
    if num in rules_fin.keys():
        return rules_fin[num]
    else:
        rules_fin[num] = []
        for p in rules_raw[num].split("|"):
            message = [""]
            for n in p.split():
                m_new = get_messages(int(n), rules_raw, rules_fin)
                message = [m + new for m in message for new in m_new]
            for m in message:
                rules_fin[num].append(m)
    return rules_fin[num]


def validate8(msg, l1, l2, lens, valids):
    """
    Validates messages for 8
    """
    if msg[l1 : (l1 + lens["8"])] in valids["8"]:
        if l2 - l1 == lens["8"]:
            return False
        elif validate8(msg, l1 + lens["8"], l2, lens, valids):
            return True
        elif validate11(msg, l1 + lens["8"], l2, lens, valids):
            return True
        else:
            return False
    else:
        return validate11(msg, l1, l2, lens, valids)


def validate11(msg, l1, l2, lens, valids):
    """
    Validates messages for 11
    """
    if msg[l1:l2] == "":
        return True
    else:
        if (
            msg[l1 : (l1 + lens["42"])] in valids["42"]
            and msg[(l2 - lens["31"]) : l2] in valids["31"]
        ):
            return validate11(msg, l1 + lens["42"], l2 - lens["31"], lens, valids)
        return False
