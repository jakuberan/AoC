def is_valid(nums, options):
    """
    Validates the options
    """
    for n in nums:
        check = 0
        for opt in options:
            if n in opt:
                check = 1
                break
        if check == 0:
            return False
    return True
