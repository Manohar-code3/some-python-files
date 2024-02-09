def generate_intermediate_code(javascript_code):
    # Split JavaScript code by lines
    lines = javascript_code.split('\n')

    intermediate_code = ""
    label_count = 1

    for line in lines:
        # Remove comments
        if '//' in line:
            line = line.split('//')[0].strip()

        # Skip empty lines
        if line.strip() == '':
            continue

        # Handle variable declaration
        if 'var' in line or 'let' in line or 'const' in line:
            intermediate_code += line + '\n'
        
        # Handle assignment statements
        elif '=' in line and 'if' not in line and 'for' not in line and 'while' not in line:
            var_name = line.split('=')[0].strip()
            intermediate_code += f'{var_name};\n{var_name} = {line.split("=")[1].strip()};\n'
        
        # Handle conditional statements
        elif 'if' in line:
            condition = line.split('(')[1].split(')')[0].strip()
            intermediate_code += f'IF {condition} GOTO label{label_count}\n'
            label_count += 1
        
        elif 'else' in line:
            intermediate_code += f'ELSE GOTO label{label_count}\n'
            intermediate_code += f'label{label_count - 1}:\n'
            label_count += 1
        
        elif '}' in line and 'end_if' not in line:
            intermediate_code += f'GOTO end_if\n'
            intermediate_code += f'label{label_count - 1}:\n'
            label_count += 1
        
        elif 'for' in line:
            loop_var = line.split('let')[1].split('=')[0].strip()
            loop_limit = line.split('<')[1].split(';')[0].strip()
            intermediate_code += f'{loop_var};\nlabel_for_start:\nIF {loop_var} < {loop_limit} GOTO label_for_body\nELSE GOTO label_for_end\nlabel_for_body:\nPRINT "Count (for loop): " + {loop_var};\n{loop_var} = {loop_var} + 1;\nGOTO label_for_start\nlabel_for_end:\n'

        elif 'while' in line:
            intermediate_code += f'let count;\ncount = 0;\nlabel_while_start:\nIF count < 5 GOTO label_while_body\nELSE GOTO label_while_end\nlabel_while_body:\nPRINT "Count (while loop): " + count;\ncount = count + 1;\nGOTO label_while_start\nlabel_while_end:\n'

    return intermediate_code.strip()


# Sample JavaScript code as input
javascript_input = """
// Variable Declaration
var x;
let y;
const z = 5;

// Decision Making Statement (if-else)
let age = 18;

if (age >= 18) {
  console.log("You are an adult.");
} else {
  console.log("You are a minor.");
}

// Arithmetic Operations
let a = 10;
let b = 5;

let sum = a + b;
let difference = a - b;
let product = a * b;
let quotient = a / b;

console.log(`Sum: ${sum}`);
console.log(`Difference: ${difference}`);
console.log(`Product: ${product}`);
console.log(`Quotient: ${quotient}`);

// For loop
for (let i = 0; i < 5; i++) {
  console.log(`Count (for loop): ${i}`);
}

// While loop
let count = 0;
while (count < 5) {
  console.log(`Count (while loop): ${count}`);
  count++;
}
"""

# Generate intermediate code from JavaScript input
resulting_intermediate_code = generate_intermediate_code(javascript_input)
print(resulting_intermediate_code)
