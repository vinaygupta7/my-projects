class First(object):
    def __init__(self):
        super(First, self).__init__()
        print ("First")


class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        print ("Second")

class Third(Second,First):
    def __init__(self):
        super(Third, self).__init__()
        print ("Third")


Third()