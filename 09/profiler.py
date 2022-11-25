import cProfile, pstats, io

class profile_deco:
    def __init__(self, func):
        self.func = func
        self.pr = cProfile.Profile()
            
    def __call__(self, *args, **kwargs):
        
        self.pr.enable()
        result = self.func(*args, **kwargs)
        self.pr.disable()

        self.s = io.StringIO()
        self.ps = pstats.Stats(self.pr, stream=self.s)
        return result

    def print_stat(self):
        self.ps.print_stats()
        print(self.s.getvalue())


@profile_deco
def add(a, b):
    return a + b

@profile_deco
def sub(a, b):
    return a - b

if __name__ == "__main__":
    add(1, 2)
    add(4, 5)
    
    add.print_stat() 

