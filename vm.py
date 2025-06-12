class VirtualMachine:
    def __init__(self, program):
        self.registers = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        self.memory = [0] * 256
        self.pc = 0
        self.flags = {'EQ': False}
        self.program = program

    def fetch(self):
        if self.pc >= len(self.program):
            return None
        return self.program[self.pc]

    def step(self):
        instr = self.fetch()
        if instr is None:
            print("End of Program")
            return False

        tokens = instr.split()
        opcode = tokens[0]

        if opcode == "LOAD":
            self.registers[tokens[1]] = int(tokens[2])
        elif opcode == "LOADM":
            addr = int(tokens[2])
            self.registers[tokens[1]] = self.memory[addr]
        elif opcode == "STORE":
            addr = int(tokens[2])
            self.memory[addr] = self.registers[tokens[1]]
        elif opcode == "ADD":
            self.registers[tokens[1]] += self.registers[tokens[2]]
        elif opcode == "SUB":
            self.registers[tokens[1]] -= self.registers[tokens[2]]
        elif opcode == "MUL":
            self.registers[tokens[1]] *= self.registers[tokens[2]]
        elif opcode == "DIV":
            self.registers[tokens[1]] //= self.registers[tokens[2]]
        elif opcode == "CMP":
            self.flags['EQ'] = (self.registers[tokens[1]] == self.registers[tokens[2]])
        elif opcode == "JMP":
            self.pc = int(tokens[1])
            return True
        elif opcode == "JE":
            if self.flags['EQ']:
                self.pc = int(tokens[1])
                return True
        elif opcode == "JNE":
            if not self.flags['EQ']:
                self.pc = int(tokens[1])
                return True
        elif opcode == "HALT":
            print("HALT: Program Terminated")
            return False
        else:
            print(f"Unknown instruction: {instr}")

        self.pc += 1
        return True

    def run(self):
        while self.step():
            self.dump()

    def dump(self):
        print(f"PC: {self.pc} REG: {self.registers} MEM: {self.memory[:10]} FLAGS: {self.flags}")
