# -*- encoding: utf-8 -*-
# vim: ts=4 sw=4 expandtab ai

"""
Test class for capsule installer CLI
"""

from tests.cli.basecli import BaseCLI


class TestCapsuleInstaller(BaseCLI):

    def capsule_installer_parent_reverse_proxy_neg(self):
        """
        @Feature: Capsule Installer
        @Test: invalid (non-boolean) parameters cannot be passed to flag
        @Setup: na
        @Steps:
          1.  attempt to provide a variety of invalid parameters
          to installer (strings, numerics, whitespace, etc.)
        @Assert: user is told that such parameters are invalid and
        install aborts.
        @Status: Manual
        """

    def capsule_installer_parent_reverse_proxy_port_neg(self):
        """
        @Feature: Capsule Installer
        @Test: invalid (non-integer) parameters cannot be passed to flag
        @Setup: na
        @Steps:
         1. attempt to provide a variety of invalid parameters to
           --parent-reverse-proxy-port flag
           (strings, numerics, whitespace, etc.)
        @Assert: user told parameters are invalid; install aborts.
        @Status: Manual
        """

    def capsule_installer_parent_reverse_proxy_pos(self):
        """
        @Feature: Capsule Installer
        @Test:  valid parameters can be passed to --parent-reverse-proxy (true)
        @Setup: note that this requires an accompanying, valid port value
        @Steps:
         1.  Attempt to provide a value of "true" to --parent-reverse-proxy
        @Assert: Install commences/completes with proxy installed correctly.
        @Status: Manual
        """

    def capsule_installer_parent_reverse_proxy_port_pos(self):

        """
        @Feature: Capsule Installer
        @Test:  valid parameters can be passed to
        --parent-reverse-proxy-port (integer)
        @Setup: note that this requires an accompanying, valid host for
        proxy parameter
        @Steps:
         1.  Attempt to provide a valid proxy port # to flag
        @Assert: Install commences and completes with proxy installed
        correctly.
        @Status: Manual
        """
