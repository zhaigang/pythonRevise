from Mlog import Mlog
class classB:
    def __init__(self):
        self.log = Mlog()


if __name__ == '__main__':
    obj = classB()
    import pdb
    pdb.set_trace()
    obj.log.write_log_to_file()


