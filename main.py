def test():
    try:
        return "abc"
    except:
        return "aaa"
    finally:
        return "CCC"


print(test())
