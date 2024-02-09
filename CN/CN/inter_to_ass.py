class Compiler:
    def __init__(self):
        self.data_section = []
        self.text_section = []

    def add_data(self, var_name, var_value=None):
        self.data_section.append(f"{var_name}: .word {var_value if var_value is not None else 0}")

    def add_instruction(self, instruction):
        self.text_section.append(instruction)

    def compile_to_assembly(self):
        data = "\n".join(self.data_section)
        text = "\n".join(self.text_section)
        assembly_code = f""".data
{data}

.text
.globl _start

_start:
{text}
"""
        return assembly_code


# Sample intermediate code
intermediate_code = [
    "x = undefined",
    "y = undefined",
    "z = 5",
    "age = 18",
    "if age >= 18 goto L1",
    "    console.log('You are a minor')",
    "goto L2",
    "L1:",
    "    console.log('You are an adult')",
    "L2:",
    "a = 10",
    "b = 5",
    "sum = a + b",
    "difference = a - b",
    "product = a * b",
    "quotient = a / b",
    "i = 0",
    "L3:",
    "if i >= 5 goto L4",
    "    console.log('Count (for loop): ' + i)",
    "    i = i + 1",
    "goto L3",
    "L4:",
    "count = 0",
    "L5:",
    "if count >= 5 goto L6",
    "    console.log('Count (while loop): ' + count)",
    "    count = count + 1",
    "goto L5",
    "L6:"
]

compiler = Compiler()

for line in intermediate_code:
    parts = line.split()
    if len(parts) >= 3 and parts[1] == '=':
        var_name = parts[0]
        var_value = parts[2] if parts[2] != 'undefined' else None
        compiler.add_data(var_name, var_value)
    elif len(parts) >= 4 and parts[0] == 'if':
        condition = parts[1] + ' ' + parts[2] + ' ' + parts[3]
        goto = parts[-1]
        instruction = f"    bge $t0, {condition}, {goto}"
        compiler.add_instruction(instruction)
    elif len(parts) >= 2 and parts[0] == 'goto':
        label = parts[1]
        instruction = f"    j {label}"
        compiler.add_instruction(instruction)
    elif len(parts) >= 1 and parts[0][-1] == ':':
        label = parts[0][:-1]
        compiler.add_instruction(f"{label}:")

assembly_output = compiler.compile_to_assembly()
print("THIS IS THE TARGET CODE: ")
print(assembly_output)
