from vm import VirtualMachine
from assembler import load_program

def main():
    program = load_program('program.txt')
    vm = VirtualMachine(program)
    vm.run()

if __name__ == '__main__':
    main()
