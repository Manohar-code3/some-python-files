def generate_assembly_code(intermediate_code):
    assembly_code_data = """.data
x:  .word 0
y:  .word 0
z:  .word 5

adult_msg: .asciiz "You are an adult.\n"
minor_msg: .asciiz "You are a minor.\n"
"""

    assembly_code_text = """.text
.globl _start

_start:
"""

    label_count = 1

    lines = intermediate_code.split('\n')
    for line in lines:
        if 'var' in line or 'let' in line or 'const' in line:
            var_name = line.split()[1][:-1]
            assembly_code_data += f"{var_name}: .word 0\n"

        elif '=' in line and 'IF' not in line and 'PRINT' not in line:
            var_name, value = line.split('=')
            var_name = var_name.strip()
            value = value.strip()
            assembly_code_text += f"    li $t{label_count}, {value}\n"
            assembly_code_text += f"    sw $t{label_count}, {var_name}\n"
            label_count += 1

        elif 'IF' in line:
            condition = line.split('IF ')[1].split(' GOTO')[0].strip()
            label = line.split('GOTO ')[1].strip()
            assembly_code_text += f"    bge $t{label_count - 1}, {condition}, {label}\n"

        elif 'PRINT' in line:
            message = line.split('"')[1]
            assembly_code_text += f"    li $v0, 4\n"
            assembly_code_text += f"    la $a0, {message}_msg\n"
            assembly_code_text += f"    syscall\n"

        elif 'GOTO' in line:
            label = line.split('GOTO ')[1].strip()
            assembly_code_text += f"    j {label}\n"
            assembly_code_text += f"{label}:\n"

    assembly_code_text += """
end_program:
    li $v0, 10
    syscall
"""

    return assembly_code_data + assembly_code_text


# Sample intermediate code as input
intermediate_input = """
var x;
let y;
const z = 5;

var age;
age = 18;

IF age >= 18 GOTO label1
ELSE GOTO label2

label1:
  PRINT "You are an adult."
  GOTO end_if

label2:
  PRINT "You are a minor."
  GOTO end_if

end_if:

let a;
let b;
a = 10;
b = 5;

let sum;
let difference;
let product;
let quotient;
sum = a + b;
difference = a - b;
product = a * b;
quotient = a / b;

PRINT "Sum: " + sum;
PRINT "Difference: " + difference;
PRINT "Product: " + product;
PRINT "Quotient: " + quotient;

let i;
i = 0;

label_for_start:
IF i < 5 GOTO label_for_body
ELSE GOTO label_for_end

label_for_body:
  PRINT "Count (for loop): " + i;
  i = i + 1;
  GOTO label_for_start

label_for_end:

let count;
count = 0;

label_while_start:
IF count < 5 GOTO label_while_body
ELSE GOTO label_while_end

label_while_body:
  PRINT "Count (while loop): " + count;
  count = count + 1;
  GOTO label_while_start

label_while_end:
"""

# Generate assembly code from intermediate input
resulting_assembly_code = generate_assembly_code(intermediate_input)
print(resulting_assembly_code)
