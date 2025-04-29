#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from ..stopwatch import Stopwatch

class TestStart(unittest.TestCase):
    """Unit tests for the Stopwatch.start method."""

    def test_start_sets_running_true(self):
        """Start should set the internal `_running` flag to True."""
        sw = Stopwatch()
        sw.start()
        self.assertTrue(sw._running)

    def test_multiple_starts_dont_change_state(self):
        """Calling start multiple times should not alter behavior."""
        sw = Stopwatch()
        sw.start()
        sw.start()
        self.assertTrue(sw._running)

class TestStop(unittest.TestCase):
    """Unit tests for the Stopwatch.stop method."""

    def test_stop_sets_running_false(self):
        """Stop should set the internal `_running` flag to False."""
        sw = Stopwatch()
        sw.start()
        sw.stop()
        self.assertFalse(sw._running)

    def test_multiple_stops_dont_change_state(self):
        """Calling stop multiple times should have no side effects."""
        sw = Stopwatch()
        sw.stop()
        self.assertFalse(sw._running)

class TestTick(unittest.TestCase):
    """Unit tests for the Stopwatch.tick method."""

    def test_tick_increases_time_when_running(self):
        """Tick should increase internal time if stopwatch is running."""
        sw = Stopwatch()
        sw.start()
        sw.tick(3)
        self.assertEqual(sw.elapsed(), 3)

    def test_tick_does_not_increase_time_when_stopped(self):
        """Tick should have no effect when stopwatch is not running."""
        sw = Stopwatch()
        sw.tick(4)
        self.assertEqual(sw.elapsed(), 0)

    def test_tick_default_is_one(self):
        """Tick should default to incrementing time by 1 second."""
        sw = Stopwatch()
        sw.start()
        sw.tick()
        self.assertEqual(sw.elapsed(), 1)

    def test_tick_negative_raises(self):
        """Tick should raise ValueError for negative input."""
        sw = Stopwatch()
        sw.start()
        with self.assertRaises(ValueError):
            sw.tick(-1)

class TestElapsed(unittest.TestCase):
    """Unit tests for the Stopwatch.elapsed method."""

    def test_elapsed_returns_zero_initially(self):
        """Elapsed time should be 0 before the stopwatch starts."""
        sw = Stopwatch()
        self.assertEqual(sw.elapsed(), 0)

    def test_elapsed_returns_correct_total(self):
        """Elapsed time should reflect all accumulated tick values."""
        sw = Stopwatch()
        sw.start()
        sw.tick(2)
        sw.tick(3)
        self.assertEqual(sw.elapsed(), 5)

class TestReset(unittest.TestCase):
    """Unit tests for the Stopwatch.reset method."""

    def test_reset_sets_time_to_zero(self):
        """Reset should zero out the accumulated time."""
        sw = Stopwatch()
        sw.start()
        sw.tick(10)
        sw.reset()
        self.assertEqual(sw.elapsed(), 0)

    def test_reset_stops_stopwatch(self):
        """Reset should stop the stopwatch even if it was running."""
        sw = Stopwatch()
        sw.start()
        sw.reset()
        self.assertFalse(sw._running)

class TestStopwatchIntegration(unittest.TestCase):
    """Integration tests for sequences of method calls on Stopwatch."""

    def test_start_tick_stop_tick_elapsed_sequence(self):
        """Verify time is only added while running; stop disables ticking."""
        sw = Stopwatch()
        sw.start()
        sw.tick(2)
        sw.stop()
        sw.tick(3)  # Should have no effect
        self.assertEqual(sw.elapsed(), 2)

    def test_reset_allows_reuse(self):
        """After reset, the stopwatch can be reused normally."""
        sw = Stopwatch()
        sw.start()
        sw.tick(4)
        sw.reset()
        sw.start()
        sw.tick(2)
        self.assertEqual(sw.elapsed(), 2)
