def write_log(log_text: str) -> None:
    print('write it to file', log_text)

def write_log_to_file(log_text: str) -> None:
    with open('log_file.log', 'a', encoding='utf-8') as f:
        f.write('write it to file:%s\n' % log_text)