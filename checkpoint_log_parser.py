import re

log_file = "C:\Users\\awate\Documents\Miscellaneous\server.log"
#log_file = "one_line_cp.log"
log_list = list()

def extract_fields_to_dict():
    with open(log_file) as ol:
        for line in ol:
            try:
                rx = \
                r"([A-Za-z0-9_:;. ]*)(>eth[0-9]{1,2} )([A-Za-z0-9_:;.{}&\- ]*)"
                m = re.match(rx,line)
                event = m.group(3).split("; ")   # content after the interface
                fields = dict(el.split(": ") for el in event)
                log_list.append(fields)
            except:
                continue
        return log_list

def main():
    print extract_fields_to_dict()

if __name__ == '__main__':
    main()
