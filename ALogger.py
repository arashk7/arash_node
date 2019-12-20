import logging

# Color codes with color names and Color codes for message types
class MsgColors:
    # Text format
    CEND = '\33[0m'
    CBOLD = '\33[1m'
    CITALIC = '\33[3m'
    CURL = '\33[4m'
    CBLINK = '\33[5m'
    CBLINK2 = '\33[6m'
    CSELECTED = '\33[7m'

    # Color codes
    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'

    CBLACKBG = '\33[40m'
    CREDBG = '\33[41m'
    CGREENBG = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG = '\33[46m'
    CWHITEBG = '\33[47m'

    CGREY = '\33[90m'
    CRED2 = '\33[91m'
    CGREEN2 = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2 = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2 = '\33[96m'
    CWHITE2 = '\33[97m'

    CGREYBG = '\33[100m'
    CREDBG2 = '\33[101m'
    CGREENBG2 = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2 = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2 = '\33[106m'
    CWHITEBG2 = '\33[107m'

    # Message type color
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    ERROR = CRED
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ALogger:

    # Set this True to store messages in a file (log_file_name)
    active_logging = False

    # The log file name can be changed here
    log_file_name = "arash_node.log"

    # python logger commands
    logger = logging.getLogger('arash')
    handler = logging.FileHandler(log_file_name)

    # Set log format here
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Manage what it has to be done if the program can not create the log file
    logger.setLevel(logging.WARNING)

    # Print simple chatty messages
    def print_msg(message, msg_color=MsgColors.CWHITE):
        print(msg_color+message+MsgColors.ENDC)
        if ALogger.active_logging:
            ALogger.logger.info(message)

    # Print important information
    def print_info(message):
        print(MsgColors.CBLUE2 + "Info: " + message + MsgColors.ENDC)
        if ALogger.active_logging:
            ALogger.logger.info(message)

    # Print errors
    def print_error(message):
        print(MsgColors.ERROR + "Error: " + message + MsgColors.ENDC)
        if ALogger.active_logging:
            ALogger.logger.error(message)

    # Print warnings
    def print_warning(message):
        print(MsgColors.WARNING + "Warning: " + message + MsgColors.ENDC)
        if ALogger.active_logging:
            ALogger.logger.warning(message)
