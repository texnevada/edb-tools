#from colorama import init, Fore
#from InquirerPy import inquirer
#from InquirerPy.validator import EmptyInputValidator

from resources.setup_logger import get_log

__version__ = "0.0.1"
log = get_log(__name__)


def splash():
    log.info(f"#" * 80)

    # log.info("   ███████╗██████╗ ██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗")
    # log.info("   ██╔════╝██╔══██╗██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝")
    # log.info("   █████╗  ██║  ██║██████╔╝       ██║   ██║   ██║██║   ██║██║     ███████╗")
    # log.info("   ██╔══╝  ██║  ██║██╔══██╗       ██║   ██║   ██║██║   ██║██║     ╚════██║")
    # log.info("   ███████╗██████╔╝██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗███████║")
    # log.info("   ╚══════╝╚═════╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝")

    log.info("       ______   ____     ____     ______            __    ")
    log.info("      / ____/  / __ \\   / __ )   /_  __/___  ____  / /____")
    log.info("     / __/    / / / /  / __  |    / / / __ \\/ __ \\/ / ___/")
    log.info("    / /___   / /_/ /  / /_/ /    / / / /_/ / /_/ / (__  ) ")
    log.info("   /_____/  /_____/  /_____/    /_/  \\____/\\____/_/____/  ")
    log.info(f"   Version: {__version__}")

    log.info(f"#" * 80)

splash()
