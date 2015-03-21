def setLog(program_name = '', log_dir = 'logs/', log_ext = '.log'):
    '''
        This Python program sets up an easy-to-use logger.

        It sets up a log filename based on the current month and program name.
        The default log directory is 'logs,' relative to current directory.
        The function will try to create the directory if it doesn't exist.

        Name:       Logger
        Creator:    Matt Gagnon <mattjgagnon@gmail.com>
        Created:    2012-05-10
        Revised:
        Version:    1.0
        Python:     2.6
        Example:    main = setLog('program-name', 'log', '.txt')
                    main.error('log an error')
                    main.warning('log a warning')
                    main.info('log information')
    '''

    # import native python modules
    import time, datetime, logging, os, errno

    # check if the program name exists and prepare it for the filename string
    if program_name:
        program_name = '-'+program_name

    # check if the log directory does not have an ending slash
    if log_dir[len(log_dir) - 1] != '/':
        # add a slash
        log_dir = log_dir + '/'

    try:
        # try to create the directory if it doesn't exist
        os.makedirs(log_dir)
    except OSError, e:
        # catch errors and raise them
        if e.errno != errno.EEXIST:
            raise

    # create a log object
    log = logging.getLogger(program_name)

    # %Y = year, %m = month, %d = day, %M = minute
    date_time = datetime.datetime.now().strftime("%Y-%m-%M")

    # put our log filename string together and assign to the file handler
    handler = logging.FileHandler(log_dir+date_time+program_name+log_ext)

    # put our log record string together and assign to the formatter
    formatter = logging.Formatter('%(asctime)s %(levelname)s - %(message)s')

    # now set up our handler with that format
    handler.setFormatter(formatter)

    # add the file handler to our log object
    log.addHandler(handler)

    # set the logging level to info
    log.setLevel(logging.INFO)

    # return our log object
    return log

main = setLog('program-name')
main.error('log an error')
main.warning('log a warning')
main.info('log information')
