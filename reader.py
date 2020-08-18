import pstats
import sys
from optparse import OptionParser

def main():
    version_msg = "%prog 1.0"
    usage_msg = """
    [-cnt] [-r results] FILE"""

    sortkey = ""

    parser = OptionParser(version=version_msg, usage=usage_msg)
    parser.add_option("-r", "--results",
                      action="store", dest="num_results", default=-1, type="int",
                      help="display first X results (X a positive integer)")
    parser.add_option("-c", "--cumulative",
                      action="store_true", dest="cumulative", default=False,
                      help="sort by cumulative time in function")
    parser.add_option("-n", "--name",
                      action="store_true", dest="name", default=False,
                      help="sort by name")            
    parser.add_option("-t", "--time",
                      action="store_true", dest="time", default=False,
                      help="sort by time spent within function (good for finding looping functions)")                        
    
    options, args = parser.parse_args(sys.argv[1:])

    if not (options.cumulative ^ options.name) ^ options.time:
        parser.error("please choose one flag from -cnt")

    p = pstats.Stats(args[0])

    sort_string = ''
    if options.cumulative:
        sort_string = 'cumulative'
    if options.name:
        sort_string = 'name'
    if options.time:
        sort_string = 'time'

    result = p.sort_stats(sort_string)

    if options.num_results == -1:
        result.print_stats(options.num_results)
    else:
        result.print_stats()

if __name__ == "__main__":
    main()