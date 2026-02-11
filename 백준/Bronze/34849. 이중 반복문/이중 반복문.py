import sys

def solve():
    try:
        N = int(sys.stdin.readline())
        
        if N * N <= 10 ** 8:
            print("Accepted")
        else:
            print("Time limit exceeded")
            
    except EOFError:
        pass
    
    except ValueError:
        pass

if __name__ == "__main__":
    solve()