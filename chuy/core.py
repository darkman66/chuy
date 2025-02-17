from pathlib import Path
from colores import error_no_traceback, setup_colorama

from .helpers import exec_commands, get_commands, get_config, get_config_file


def entry_point() -> None:
    """
    Chuy entry point
    """

    setup_colorama()

    home = str(Path.home())
    accept_files = ["chuy.json", "pyproject.toml", "chuy.toml"]
    if home:
        tmp_dir = []
        for item in accept_files:
            tmp_dir.append(f"{home}/{item}")
        accept_files += tmp_dir
    config = get_config(get_config_file(accept_files))

    for command in get_commands(config):
        try:
            exec_commands(config[command])
        except KeyError as command_not_defined_in_config:
            raise BaseException(
                "That command is not defined in your configuration!"
            ) from command_not_defined_in_config


def main():
    """
    General 'try, catch' as handler
    """
    try:
        entry_point()
    except KeyboardInterrupt:
        error_no_traceback("\nProcess killed by the user!")
    except BaseException as e:
        error_no_traceback(str(e))


if __name__ == "__main__":
    main()
