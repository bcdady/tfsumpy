from typing import TextIO
import sys
import os

class BaseReporter:
    """Base class for all reporters with common functionality."""

    COLORS: dict[str, str] = {}  # populated lazily

    def __init__(self, *, enable_color: bool | None = None, output: TextIO = sys.stdout):
        self.output = output

        # Decide if colour should be enabled
        self._color_enabled = enable_color if enable_color is not None else self._should_enable_color()

        if self._color_enabled and BaseReporter.COLORS is None:
            # Lazy import – only when we first need colours
            from colorama import Fore, Style, init  # local import
            init(strip=not self._color_enabled)
            BaseReporter.COLORS = {
                "high": Fore.RED,
                "medium": Fore.YELLOW,
                "low": Fore.GREEN,
                "green": Fore.GREEN,
                "blue": Fore.BLUE,
                "red": Fore.RED,
                "reset": Style.RESET_ALL,
                "bold": Style.BRIGHT,
            }

    def _should_enable_color(self) -> bool:
        """Determine if color output should be enabled."""
        # Disable colors if NO_COLOR is set
        if 'NO_COLOR' in os.environ:
            return False

        # Disable colors if output is not a terminal
        if not hasattr(self.output, 'isatty') or not self.output.isatty():
            return False

        return True

    def _colorize(self, text: str, color_key: str) -> str:
        """Apply color to text using colorama.

        Args:
            text: Text to colorize
            color_key: Key from COLORS dict

        Returns:
            Colorized text if enabled, original text otherwise
        """
        color = self.COLORS.get(color_key, '')
        if not color:
            return text

        return f"{color}{text}{self.COLORS['reset']}"

    def _print_header(self, title: str) -> None:
        """Print report header with consistent formatting.

        Args:
            title: Header title text
        """
        self.output.write(f"\n{self._colorize(title, 'bold')}\n")
        self.output.write("=" * 50 + "\n")

    def _write(self, text: str) -> None:
        """Write text to output stream.

        Args:
            text: Text to write
        """
        self.output.write(text)