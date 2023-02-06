from ztdebugger import ic

ic.init(sender="1534643901@qq.com", receiver="zhoutong@intern.langboat.com", key="aydcpdgycdofgffg")
#ic.init()


# @ic.snoop()
def test():
    r = 0
    for i in range(1, 3):
        r += i
    return r


def main():
    b = 1
    ic(b)
    ic(test())
    #a = 1 / 0
    raise ValueError("hello world")
    #assert 0


if __name__ == '__main__':
    main()
