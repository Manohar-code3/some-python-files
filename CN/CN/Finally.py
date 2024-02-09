import ply.lex as lex
import json
from pyjsparser import parse


tokens = (
    'KEYWORD',
    'IDENTIFIER',
    'STRING_LITERAL',
    'NUMBER',
    'BOOLEAN_LITERAL',
    'NULL',
    'UNDEFINED',
    'SPECIAL_LITERAL',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'COMMA',
    'DOT',
    'ASSIGN',
    'EQUAL',
    'NOT_EQUAL',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'MODULO',
    'FUNCTION',
    'RETURN',
    'CONSTANT',
    'DELIMITER',
    'OPERATOR',
)

t_ignore = ' \t'
t_KEYWORD = r'(var|let|const|if|while|for|function|return)(?=\W|$)'
t_IDENTIFIER = r'(console.log)|(\w+(?=\W|$))'
t_STRING_LITERAL = r'(\'[^\']*\'|\"[^\"]*\")'
t_SPECIAL_LITERAL = r'(null|undefined)(?=\W|$)'
t_NUMBER = r'\d+'
t_BOOLEAN_LITERAL = r'(?:true|false)'
t_NULL = r'null'
t_UNDEFINED = r'undefined'

# literals = '()[]{}:;,.=+-=*/%'

# New token definitions
def t_CONSTANT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_DELIMITER(t):
    r'[{}();,\[\]\.]'
    return t

def t_OPERATOR(t):
    r'[+-=<>*!|/]'
    return t

def t_ignore_COMMENT(t):
    r'//.*|/\*(.|\n)*?\*/'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.lexer.lexpos = t.lexpos + len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}, position {t.lexpos}")
    t.lexer.skip(1)

lexer = lex.lex()
# Test input code
input_code = """// Variable Declaration
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

console.log('Sum: ',sum);
console.log('Difference: ',difference);
console.log('Product:',product);
console.log('Quotient:', quotient);

// For loop
for (let i = 0; i < 5; i++) {
  console.log('Count (for loop):', i);
}

// While loop
let count = 0;
while (count < 5) {
  console.log('Count (while loop): ' + count);
  count++;
}

"""

# Give the lexer the input code
lexer.input(input_code)

# Tokenize and print the lexer output
print("Lexer Output:")
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)

# Parse the input code
ast = parse(input_code)

# Convert the AST to a JSON string for printing (Syntax Analysis)
ast_json_syntax = json.dumps(ast, indent=2)
print("\nAST after Syntax Analysis:")
print(ast_json_syntax)
class SymbolTable:
    def _init_(self):
        self.symbols = {}
        self.scopes = [{}]

    def push_scope(self):
        self.scopes.append({})

    def pop_scope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()

    def add_symbol(self, name, value, type, lineno):
        self.scopes[-1][name] = {'value': value, 'type': type, 'lineno': lineno}

    def get_symbol(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

    def update_symbol(self, name, value):
        for scope in reversed(self.scopes):
            if name in scope:
                scope[name]['value'] = value
                return True
        return False


# ... (your existing symbol table class and example usage of the symbol table)

# Initialize the symbol table
symbol_table = SymbolTable()
current_scope = 'global'

# Function to handle variable declarations
def handle_variable_declaration(node):
    global current_scope
    declaration_type = node['kind']

    for decl in node['declarations']:
        var_name = decl['id']['name']
        lineno = decl['id'].get('loc', {}).get('start', {}).get('line', -1)

        # Check if there is an initialization value
        if 'init' in decl and decl['init']:
            if decl['init']['type'] == 'Literal':
                var_value = decl['init']['value']
            elif decl['init']['type'] == 'Identifier':
                # Handle the case where the variable is initialized with another variable
                var_value = symbol_table.get_symbol(decl['init']['name'])['value']
            elif decl['init']['type'] == 'BinaryExpression':
                # Evaluate binary expressions during initialization
                var_value = evaluate_binary_expression(decl['init'])
            else:
                # Handle other types of initialization as needed
                var_value = None
        else:
            var_value = None

        symbol_table.add_symbol(var_name, var_value, declaration_type, lineno)

def evaluate_binary_expression(node):
    operator = node['operator']
    left_operand = node['left']
    right_operand = node['right']

    if operator == '+':
        return evaluate_expression(left_operand) + evaluate_expression(right_operand)
    elif operator == '-':
        return evaluate_expression(left_operand) - evaluate_expression(right_operand)
    elif operator == '*':
        return evaluate_expression(left_operand) * evaluate_expression(right_operand)
    elif operator == '/':
        return evaluate_expression(left_operand) / evaluate_expression(right_operand)
    # Add other binary operators as needed

def evaluate_expression(node):
    if node['type'] == 'Literal':
        return node['value']
    elif node['type'] == 'Identifier':
        return symbol_table.get_symbol(node['name'])['value']
    elif node['type'] == 'BinaryExpression':
        return evaluate_binary_expression(node)

# Rest of your code...


# Function to perform semantic analysis
def semantic_analysis(ast):
    global current_scope

    for node in ast['body']:
        if node['type'] == 'ExpressionStatement' and node['expression']['type'] == 'CallExpression':
            # Example of a console.log statement
            callee = node['expression']['callee']
            if callee['type'] == 'MemberExpression' and callee['object']['name'] == 'console' and callee['property']['name'] == 'log':
                arguments = node['expression']['arguments']
                for arg in arguments:
                    if arg['type'] == 'Literal':
                        print(f"Found log statement with value: {arg['value']}")

        elif node['type'] == 'VariableDeclaration':
            handle_variable_declaration(node)
        elif node['type'] == 'FunctionDeclaration':
            symbol_table.add_symbol(node['id']['name'], None, 'function', node.get('loc', {}).get('start', {}).get('line', -1))
            symbol_table.push_scope()
            for param in node['params']:
                symbol_table.add_symbol(param['name'], None, 'param', param.get('loc', {}).get('start', {}).get('line', -1))
            semantic_analysis(node['body'])
            symbol_table.pop_scope()
        # Add handling for other node types as needed

# Run semantic analysis on the AST
semantic_analysis(ast)

# Print the symbol table
print("\nSymbol Table:")
for scope_index, scope in enumerate(symbol_table.scopes):
    print(f"Scope {scope_index + 1}:")
    for symbol_name, symbol_info in scope.items():
        if 'value' in symbol_info:
            print(f"  {symbol_name}: {symbol_info['value']} (Type: {symbol_info['type']}, Line No: {symbol_info['lineno']})")
        else:
            print(f"  {symbol_name}: (Type: {symbol_info['type']}, Line No: {symbol_info['lineno']})")



# Convert the updated AST to a JSON string for printing (Semantic Analysis)
ast_json_semantic = json.dumps(ast, indent=2)
print("\nAST after Semantic Analysis:")
print(ast_json_semantic)

# ... (your existing symbol table class and example usage of the symbol table)

class Compiler:
    def _init_(self):
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
print(assembly_output)