import re
import itertools

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxgc'

# 2.1
# re

symbols = re.findall(r"(?<=[A-Z])[a-z](?=[A-Z])", line)

print(''.join(symbols))

# loop

new_line_loop = ''
for i, letter in enumerate(line):
    if letter.islower() and line[i - 1].isupper() and line[i + 1].isupper():
        new_line_loop += letter
print(new_line_loop)

# 2.2
# re

symbols_2 = re.findall(r"(?<=[A-Z][a-z]{2})[A-Z](?=[A-Z]{2}[a-z])", line)
print(''.join(symbols_2))

# loop

new_line_loop2 = ''
for i, letter in enumerate(line):
    if letter.isupper() and line[i - 1].islower() and line[i - 2].islower() and line[i - 3].isupper() and line[
        i + 1].isupper() and line[i + 2].isupper() and line[i + 3].islower():
        new_line_loop2 += letter
print(new_line_loop2)

# 2.3

generator = itertools.cycle('12345')

for letter in line:
    loop_counter = next(generator)
    new_file = open(f'file_{loop_counter}', 'a')
    new_file.write(letter)
    new_file.close()
