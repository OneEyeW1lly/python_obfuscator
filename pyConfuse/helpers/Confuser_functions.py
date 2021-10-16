import os, base64, random, re
from helpers.variable_name_generator import VariableNameGenerator

#FILE = "./test.py"
#RECURSIONS = 5

class Confuser():
    def __init__(self, B64_NAME_RANGE_HIGH=50, B64_NAME_RANGE_LOW=10, XOR_HIGHER=20, XOR_LOWER=10):
        self.WATERMARK = '# ========== Obfuscated by pyConfuser ========== #\n'
        self.BASE64_NAME_RANGE_LOWER = B64_NAME_RANGE_LOW
        self.BASE64_NAME_RANGE_HIGHER = B64_NAME_RANGE_HIGH
        self.file = None
        self.code = None
        self.name_generator = VariableNameGenerator()

    def read_file(self, file):
        with open(file, 'r') as fp:
            return fp.read()


    def write_file(self, file, data):
        with open(file, 'w') as fp:
            fp.write(data)


    def b64(self, data):
        return base64.b64encode(data.encode('utf-8')).decode('utf-8')


    def b32(self, data):
        return base64.b32encode(data.encode('utf-8')).decode('utf-8')


    def b16(self, data):
        return base64.b16encode(data.encode('utf-8')).decode('utf-8')


    def base64_encode(self, data):
        return self.b16(self.b32(self.b64(data)))


    def XOR(self, data, key):
        string_ = ""
        for i in data:
            string_ += chr(ord(i) ^ int(key))

        return string_


    def new_file_name(self, file, ext):
        f_t, f_h = os.path.split(file)
        filename, fileext = os.path.splitext(f_h)
        return os.path.join(f_t, filename + ext + fileext)


    def string_encryption(self, data, xor_key=10):
        key_val = xor_key
        key_name = "rand_num"
        b64_name = "_" + self.name_generator.random_string(
            2, random.randint(self.BASE64_NAME_RANGE_LOWER, self.BASE64_NAME_RANGE_HIGHER))
        code = f'import base64 as {b64_name};\n{key_name}={key_val}\n' + data  #.replace('\'', '\"')
        strings = re.findall(r"[\'\"]([^\'\"]*)[\'\"]", code)
        print("Strings:")
        for i in range(len(strings)):
            encypted_string = self.XOR(strings[i], key_val)
            print("\t" + "\"" + strings[i] + "\"")
            code = re.sub(
                r'[\'\"](?<=[^.])(\b{}\b)[\"\']'.format(strings[i]),
                f"''.join([str(chr(int(ord(i))^int({key_name}))) for i in {b64_name}.b16decode('{self.b16(encypted_string)}').decode('u'+'tf'+'-'+'8')])",
                code)

        print()
        return code


    def variable_renamer(self, code):
        # add \n so regex picks it up
        code = "\n" + code
        variable_names = re.findall(r"(\w+)(?=( |)=( |))", code)
        print("Variable Names:")
        for i in range(len(variable_names)):
            obfuscated_name = self.name_generator.get_random(i + 12)
            print("\t" + "\"" + variable_names[i][0] + "\"")
            code = re.sub(r"(?<=[^.])(\b{}\b)".format(variable_names[i][0]), obfuscated_name, code)

        print()
        return code

    def function_renamer(self, code):
        pass

    def base64_encryption(self, data, RECURSIONS):
        for i in range(RECURSIONS):
            b64_name = self.name_generator.random_string(10)
            code = f'import base64 as {b64_name};exec({b64_name}.b64decode({b64_name}.b32decode({b64_name}.b16decode(\'\'\'{self.base64_encode(data)}\'\'\'))))'
            data = code

        return data

    def use_random_obfuscation(self, FILE, xor_key):
        print("Starting Obfuscation\n")
        code = ""
        new_file = self.new_file_name(FILE, '-StringEncrypt')
        f_buff = self.read_file(FILE)
        code = self.string_encryption(f_buff, int(xor_key))
        #code = self.variable_renamer(code)
        self.write_file(new_file, self.WATERMARK + code)
        print("DONE!")

    def use_variable_obfuscation(self, FILE):
        print("Starting Obfuscation\n")
        code = ""
        new_file = self.new_file_name(FILE, '-VarRename')
        f_buff = self.read_file(FILE)
        #code = self.string_encryption(f_buff)
        code = self.variable_renamer(f_buff)
        self.write_file(new_file, self.WATERMARK + code)
        print("DONE!")

    def use_base64_encyption(self, FILE, RECURSIONS):
        print("Starting Obfuscation\n")
        code = ""
        new_file = self.new_file_name(FILE, '-base64')
        f_buff = self.read_file(FILE)
        code = self.base64_encryption(f_buff, RECURSIONS)
        self.write_file(self.new_file_name(FILE), self.WATERMARK + code)
        print("DONE!")

    def use_all_encryption(self, FILE, RECURSIONS, xor_key):
        print("Starting Obfuscation\n")
        code = ""
        new_file = self.new_file_name(FILE, '-confused')
        f_buff = self.read_file(FILE)

        code = self.string_encryption(f_buff, xor_key)
        code = self.variable_renamer(code)
        code = self.base64_encryption(code, RECURSIONS)

        self.write_file(new_file, self.WATERMARK + code)
        print("DONE!")

'''
if __name__ == '__main__':
    c = Confuser()
    c.use_all_encryption("./pyConfuser.py", 5)
'''
