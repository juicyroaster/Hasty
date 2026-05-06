
# Hasty build system

Hasty is a build system made in python which aims for simplicity. The implementation of the build system is very straight forward and very lightweight.

## Usage

In order to use the library, you have to drop it in the same directory as the build script

```python
  # The build library must be imported
  from hasty import Hasty
  
  # You can use the build system according to your likings. Below is a simple example:

  def test_build():
    h = Hasty()
    cc = "gcc"

    # The build function also accepts a fourth argument. 
    # It is a list of all the dependency Ex: ["module1.o", "module2.o"]
    h.build(cc, "main.c", "-Wextra -o main")

if __name__ == "__main__":
    test_build()
```
    
## Dependncies

In order to use the Build system, you may need any python3 interpreter with subprocesses and os libraries.
