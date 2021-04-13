# -*- coding: utf-8 -*-
import re
with open('Mockingjay.txt') as m:
    count = 0
    text = m.read()
    pattern = re.compile(r'\bm\w{8}y', re.I)
    matches = pattern.finditer(text)
    for match in matches:
            count += 1
            print(match)
            #print(match.span)
    # for line in m:
    #     line = line.strip()
    #     pattern = re.compile(r'\b[mM]\w{8}[yY]')
    #     # x = re.match(pattern, line)
    #     matches = pattern.finditer(line)
    #     #matches = pattern.findall(line)
    #     # x = re.search(r'\b[mM]\w{8}[yY]\b', line)
    #     for match in matches:
    #         count += 1
    #         print(match)
    #         #print(match.span)
    #     #if x != None and x != []:
    #         #count += 1
    #         # y = x.span()
            
    #         # print(line[y[0]:y[1]])
    #         # print(x.span())
    #         # print(line)
    #         # print(x.group())
    #         # print(x)
    print(count)
#%%
import re
def check_web_address(text):
  pattern = '[\w\.\+-]\w*\.[a-zA-Z]*$'
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True
#%%
import re
def check_time(text):
  pattern = '[1-9]+:[0-5][0-9]\s?[aApP][mM]'
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
#%%
import re
def contains_acronym(text):
  pattern = '\([A-Z0-9][a-zA-Z0-9]+\)' 
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True
#%%
import re
def check_zip_code (text):
  result = re.search(r"\s[0-9]{5}-?[0-9]*", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False
#%%
import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]:\s([A-Z]*)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
#%%
import re
def transform_record(record):
  new_record = re.sub(r'([0-9-]+)' , r'+1-\1', record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer
#%%
import re
def multi_vowel_words(text):
  pattern = r'\w*[aeiou]{3,}\w*'
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []
#%%
import re
def transform_comments(line_of_code):
  #result = re.sub(r'([=\+\w\s\)\(])#+\s()')
  result = re.sub(r'(#+)', r'//', line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"
#%%
import re
def convert_phone_number(phone):
  result = re.sub(r'(\d{3})-(\d{3}-\d{,4})', r'(\1) \2', phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300
#%%
import re
def show_time_of_pid(line):
  pattern = r'^([\w\s\d]+:\d\d:\d\d)[\s\w\.=]+\[(\d+)\]'
  result = re.search(pattern, line)
  return f'{result[1]} pid:{result[2]}'

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440
print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187
print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187
print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440
print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807
print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440
print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440
#%%


