import os
import subprocess

class Hasty:
    def __init__(self):
        self.compiled_list = set()

    def was_compiled(self, filepath):
        return filepath in self.compiled_list

    def sh(self, cmd):
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError:
            print(f"\n[ERROR] Command failed:\n{cmd}")
            exit(1)
        print(f"[SUCCESS] {cmd}.")

    def build(self, compiler, file, flags="", output="", deps=None):
        deps = deps or []

        if output and self.was_compiled(output):
            return False

        needs_rebuild = not output or not os.path.exists(output)
        
        if not needs_rebuild and output:
            out_time = os.path.getmtime(output)
            if os.path.getmtime(file) > out_time:
                needs_rebuild = True
            else:
                for d in deps:
                    if (os.path.exists(d) and os.path.getmtime(d) > out_time) or self.was_compiled(d):
                        needs_rebuild = True
                        break

        if needs_rebuild:
            cmd = f"{compiler} {file} {flags}"
            self.sh(cmd)
            if output:
                self.compiled_list.add(output)
            return True
            
        return False

if __name__ == "__main__":
    print("To use this build system, import this in a python source file. Read more at github.com/juicyroaster/hasty.")
