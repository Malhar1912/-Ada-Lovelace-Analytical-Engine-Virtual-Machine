def load_program(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    # Strip comments, blank lines
    program = [line.strip() for line in lines if line.strip() and not line.startswith('#')]
    return program
