

---

# 📄 `README.md`

# 🧮 Ada Lovelace Analytical Engine Virtual Machine (AE-VM)

> A pure Python command-line virtual machine simulating how Ada Lovelace might have programmed Charles Babbage’s Analytical Engine, using modern computational models while honoring historical design.

---

## 📜 Introduction

In 1842, Ada Lovelace wrote what is widely recognized as the world's first computer program: an algorithm for calculating Bernoulli numbers on Charles Babbage's theoretical Analytical Engine. Unfortunately, neither the Analytical Engine nor its full software stack were ever built.

This project aims to pay tribute to Ada Lovelace by building a **Virtual Machine (VM)** that simulates how such an Analytical Engine might have operated, using modern technology principles but maintaining 19th-century computational ideas.

✅ **No GUI**  
✅ **Pure command-line interpreter**  
✅ **Full instruction set simulation**  
✅ **Educational & Historical Project**

---

## 🎯 Project Goals

- Build an educational, low-level CPU emulator.
- Simulate registers, memory, program counter, flags.
- Provide an assembly-like language Ada might have used.
- Demonstrate the basic building blocks of computer architecture.
- Offer a historically inspired learning experience for modern learners.

---

## 🔧 Technologies Used

| Technology | Purpose |
|-------------|---------|
| Python 3.x  | Main programming language |
| No external libraries | Pure standard library only |
| Windows / Linux / macOS | Fully cross-platform |

---

## 🧮 Instruction Set Design

The instruction set reflects operations Ada Lovelace described in her notes while working on Babbage’s machine.

| Instruction | Syntax | Description |
|--------------|--------|-------------|
| `LOAD`  | `LOAD A 10` | Load constant 10 into register A |
| `LOADM` | `LOADM A 100` | Load from memory address 100 into A |
| `STORE` | `STORE A 100` | Store register A into memory[100] |
| `ADD`   | `ADD A B` | A = A + B |
| `SUB`   | `SUB A B` | A = A - B |
| `MUL`   | `MUL A B` | A = A * B |
| `DIV`   | `DIV A B` | A = A / B (integer division) |
| `CMP`   | `CMP A B` | Compare A and B, update flags |
| `JMP`   | `JMP 10` | Jump to instruction 10 |
| `JE`    | `JE 10` | Jump if previous CMP was equal |
| `JNE`   | `JNE 10` | Jump if previous CMP was not equal |
| `HALT`  | `HALT` | Stop program execution |

---

## 🗄 Memory Model

- **Registers:**  
  4 General Purpose Registers: `A`, `B`, `C`, `D`

- **Memory:**  
  256 addresses (`memory[0]` to `memory[255]`)

- **Flags:**  
  - `EQ` (equal flag after comparison)

- **Program Counter (PC):**  
  - Points to current instruction index.

---

## 🏗 Project Structure

```bash
ada-vm/
  ├── main.py         # Main entry point
  ├── vm.py           # Virtual Machine logic
  ├── assembler.py    # Program loader
  └── program.txt     # Sample assembly program
````

---

## 🔌 Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/ada-vm.git
cd ada-vm
```

### 2️⃣ (Optional but recommended) Create virtual environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
# No external dependencies required.
# Pure Python standard library.
```

### 4️⃣ Run the VM

```bash
python main.py
```

---

## 🧑‍💻 Sample Program

File: `program.txt`

```txt
LOAD A 10
LOAD B 5
MUL A B
STORE A 100
LOADM C 100
HALT
```

This program:

* Loads 10 into A
* Loads 5 into B
* Multiplies A \* B (result = 50)
* Stores 50 into memory address 100
* Loads memory\[100] into register C
* Halts execution

---

## 🖥 Example Output

```txt
PC: 1 REG: {'A': 10, 'B': 0, 'C': 0, 'D': 0} MEM: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] FLAGS: {'EQ': False}
PC: 2 REG: {'A': 10, 'B': 5, 'C': 0, 'D': 0} MEM: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] FLAGS: {'EQ': False}
PC: 3 REG: {'A': 50, 'B': 5, 'C': 0, 'D': 0} MEM: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] FLAGS: {'EQ': False}
PC: 4 REG: {'A': 50, 'B': 5, 'C': 0, 'D': 0} MEM: [0, 0, 0, 0, 0, 50, 0, 0, 0, 0] FLAGS: {'EQ': False}
PC: 5 REG: {'A': 50, 'B': 5, 'C': 50, 'D': 0} MEM: [0, 0, 0, 0, 0, 50, 0, 0, 0, 0] FLAGS: {'EQ': False}
HALT: Program Terminated
End of Program
```

---

## 🎓 Educational Value

* CPU Simulation
* Register-based computing
* Instruction decoding
* Memory addressing
* Condition flags
* Program counter control
* No external libraries (pure algorithmic Python)

---

## 🌐 Historical Inspiration

* Ada Lovelace (1815–1852) — First computer programmer.
* Charles Babbage (1791–1871) — Inventor of the Analytical Engine.
* This project imagines how Ada might have written actual machine code if the Analytical Engine had been physically built.

---

## 📈 Roadmap

* [ ] Implement assembler with labels
* [ ] Implement CALL/RET for subroutines
* [ ] Implement stack
* [ ] Advanced branching and loops
* [ ] Debugger mode
* [ ] Step-through execution mode
* [ ] Breakpoint system
* [ ] Unit tests and error handling
* [ ] Export compiled program files
* [ ] Web interface version

---

## 🚀 Advanced Expansion Ideas

* Build a full **Ada Assembly Language (AAL) Compiler**.
* Visualize execution as FSM (Finite State Machine).
* Implement device I/O simulation (printer, punch cards).
* Build full WebAssembly-based online interactive version.
* Create historical educational modules for universities.

---

## 🧮 Why No GUI?

* Stay closer to how Analytical Engine might have been programmed (i.e. no interactive screens)
* Simulate the "mechanical" nature of machine step-by-step operation.
* Command-line driven debugging & execution.
* Focus on core computation models.

---

## 🤝 Contribution Guidelines

We welcome contributions!

* Fork the repository.
* Create a feature branch.
* Commit your changes.
* Submit a Pull Request.
* Write clean code and detailed commit messages.

---

## 🛡 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

* **Malhar Pangarkar** — Tribute to Ada Lovelace
* Twitter / LinkedIn: *add your handles here*

---

## 🧵 Further Reading

* Ada Lovelace, "Notes on the Analytical Engine", 1842
* Charles Babbage, "On the Analytical Engine", 1837
* Martin Campbell-Kelly, "The History of Computing: Birth of the Computer", Oxford

---

## 💎 Closing Remark

> "That brain of mine is something more than merely mortal, as time will show."
> — *Ada Lovelace*

This project is a humble attempt to honor the timeless brilliance of Ada Lovelace and Charles Babbage — to bring their machine to life in the 21st century.

---

# 🔧 Run With One Command (Summary)

```bash
git clone https://github.com/your-username/ada-vm.git
cd ada-vm
python main.py
```

---

⭐ Star the repo if you like the project.
Let’s keep Ada’s legacy alive! 🚀

```




