import sys
from parser import Parser
from code_writer import CodeWriter

class VMTranslator():
    def __init__(self):
        self.DEBUG = 1
        # Initialization
        self.parser = Parser(self.DEBUG)
        self.code_writer = CodeWriter()

        # The assembly code will be written to Prog.asm
        self.assembly_codes = []

    # def main(self):
    #     # Pathname
    #     absolute_pathname = sys.argv[1].split("/")
    #     relative_pathname = absolute_pathname[1]
    #     relative_pathname_without_extension = relative_pathname.split(".")[0]

    #     name1 = "./" + "/".join(absolute_pathname)
    #     name2 = "./" + "/".join(absolute_pathname[:-1] + [relative_pathname_without_extension])

    #     self.vm_translate()

    def vm_translate(self):
        while self.parser.has_more_lines():
            self.parser.advance()
            command = self.parser.command[0]
            if self.DEBUG:
                print(f"{command = }")
            # Arithmetic commands
            if self.parser.command_type() == "C_ARITHMETIC":
                self.code_writer.write_arithmetic(command)
            # Push/Pop commands
            elif self.parser.command_type() == "C_PUSH" or self.parser.command_type() == "C_POP":
                segment = self.parser.arg1()
                index = self.parser.arg2()
                self.code_writer.write_push_pop(command, segment, index)
            
        self.code_writer.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python3 VMTranslator.py Prog.vm')
        sys.exit(1)
    
    vm_translator = VMTranslator()
    vm_translator()