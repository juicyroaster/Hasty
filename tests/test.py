from hasty import Hasty 

def test_build():
    h = Hasty()
    cc = "gcc"

    h.build(cc, "main.c", "-Wextra -o main") 


if __name__ == "__main__":
    test_build()
