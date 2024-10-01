# argparse
import os
import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='CSAF Tester')
    #parser.add_argument('-u', '--user', required=True,
    #                    help='***required*** Put your username to login to Bugdb service')
    #parser.add_argument('-p', '--password', required=True,
    #                    help='***required*** Put your user password to login to Bugdb service')
    #parser.add_argument('-b', '--url', required=True,
    #                    help='***required*** Put Bugdb api url (production or staging)')
    #parser.add_argument('action', choices=['create', 'get', 'generate_notes', 'post_notes'],
    #                    help='***required*** Bugz tool supported actions')
    #parser.add_argument('--cve', metavar=('CVE-YYYY-NNNN'), nargs='*',
    #                    help='CVE-YYYY-NNNN'),
    #parser.add_argument('--arch', metavar=('ARCHITECTURE'),
    #                    help='ex: x86_64, aarch64'),
    #parser.add_argument('--path', metavar=('(JENKINS)BUILD_LOG_PATH'),
    #                    help='path to build.log'),
    #parser.add_argument('--feature', action='store_true')
    #parser.add_argument('--no-feature', dest='feature', action='store_false')
    #parser.add_argument('action', choices=['name', 'version', 'longver'],
    #                    help='***required*** types to process the package name')
    #parser.add_argument('--package', '-p', nargs='?',
    #                    help='looking for specific package')
    #parser.add_argument('--package', '-p',
    #                    help='looking for specific package')
    parser.add_argument('--errata', '-eid',
                        help='Errata ID')
    parser.add_argument('--fpath', '-f',
                        help='Read Errata IDs from file')
    parser.add_argument('-d', '--debug', action='store_true',
                        help='debug mode')
    #parser.set_defaults(feature=True)
    return parser

# ===================================================
# args

parser = get_parser()
args = parser.parse_args()
print(args)

is_debug = False


def debug(s):
    if is_debug or args.debug:
      print("[DEBUG] %s" % (s))

def info(s):
    if is_debug or args.debug:
      print("[INFO] %s" % (s))

def warn(s):
    if is_debug or args.debug:
      print("[WARN] %s" % (s))



# ===================================================
# config




# ===================================================

def test(qid):
    ''' Tester'''
    # TODO: Write tester here...


def test_from_file(fpath):
    with open(fpath, "r") as f:
        lines = f.readlines()
        for line in lines:
            print("[Tester] Processing line:", line.strip())
            print(test(line.strip()))
    print("[Tester] test_from_file(), done!")

def main():
    if args.fpath:
        test_from_file(args.fpath)
    else:
        print(test(args.errata))
        print("[Tester] test(), done!")
        

if __name__ == "__main__":
    main()
