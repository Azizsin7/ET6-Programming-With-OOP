#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Stopwatch:
    """A stopwatch that tracks elapsed time in seconds.

    This class does not interact with real time. It simulates a stopwatch for use in tests or
    controlled environments. Time is added manually using `tick()`.

    Example:
        >>> sw = Stopwatch()
        >>> sw.start()
        >>> sw.tick(5)
        >>> sw.elapsed()
        5
        >>> sw.stop()
        >>> sw.tick(2)
        >>> sw.elapsed()
        5
        >>> sw.reset()
        >>> sw.elapsed()
        0
    """

    def __init__(self):
        """Initialize the stopwatch with zero time and stopped."""
        self._running = False
        self._time = 0

    def start(self) -> None:
        """Start the stopwatch. Has no effect if already running."""
        self._running = True

    def stop(self) -> None:
        """Stop the stopwatch. Has no effect if already stopped."""
        self._running = False

    def tick(self, seconds: int = 1) -> None:
        """Advance the stopwatch by a number of seconds.

        Args:
            seconds (int): Number of seconds to advance.

        Raises:
            ValueError: If `seconds` is negative.

        Note:
            Time only advances if the stopwatch is running.
        """
        if seconds < 0:
            raise ValueError("Seconds must be non-negative.")
        if self._running:
            self._time += seconds

    def elapsed(self) -> int:
        """Return the number of seconds elapsed since start.

        Returns:
            int: Total seconds counted since last reset.
        """
        return self._time

    def reset(self) -> None:
        """Reset the stopwatch to zero time and stop it."""
        self._time = 0
        self._running = False
