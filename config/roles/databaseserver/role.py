# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Red Hat, Inc.
#
# Authors:
# Thomas Woerner <twoerner@redhat.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import dbus
import dbus.service
import slip.dbus
import slip.dbus.service

from rolekit.config import *
from rolekit.config.dbus import *
from rolekit.logger import log
from rolekit.server.decorators import *
from rolekit.server.rolebase import *
from rolekit.dbus_utils import *
from rolekit.errors import *

class Role(RoleBase):
    # Use _DEFAULTS from RoleBase and overwrite settings or add new if needed.
    # Without overwrites or new settings, this can be omitted.
    _DEFAULTS = dict(RoleBase._DEFAULTS, **{
        "version": 1,
        "services": [ "postgresql.service" ],
        "packages": [ "postgresql-server", "postgresql-contrib" ],
        "firewall": { "ports": [], "services": [ "postgresql" ] },
#        "myownsetting": "something",
    })

    # Use _READONLY_SETTINGS from RoleBase and add new if needed.
    # Without new readonly settings, this can be omitted.
#    _READONLY_SETTINGS = RoleBase._READONLY_SETTINGS + [
#        "myownsetting"
#    ]

    # maximum number of instances of this role
    _MAX_INSTANCES = 1


    # Initialize role
    def __init__(self, name, directory, *args, **kwargs):
        super(Role, self).__init__(name, directory, *args, **kwargs)

    def do_start_async(self, sender=None):
        yield async.call_future(self.start_services_async())

    def do_stop_async(self, sender=None):
        yield async.call_future(self.stop_services_async())


    # Deploy code
    def do_deploy_async(self, values, sender=None):
        # Do the magic
        #
        # In case of error raise an exception
        # FIXME: install packages, run initdb, enable services
        raise NotImplementedError()


    # Redeploy code
    def do_redeploy(self, values, sender=None):
        # Do the magic
        #
        # In case of error raise an exception
        # FIXME: should just chain to parent for the common fields?
        raise NotImplementedError()


    # Decommission code
    def do_decommission_async(self, force=False, sender=None):
        # Do the magic
        #
        # In case of error raise an exception
        # FIXME: disable services
        raise NotImplementedError() # FIXME: what about the data?


    # Update code
    def do_update(self, sender=None):
        # Do the magic
        #
        # In case of error raise an exception
        # FIXME: should just chain to parent for the common fields?
        raise NotImplementedError()


    # Check own properties
    def do_check_property(self, prop, value):
        return False


    # Static method for use in roles and instances
    #
    # Usage in roles: <class>.do_get_dbus_property(<class>, key)
    #   Returns settings as dbus types
    #
    # Usage in instances: role.do_get_dbus_property(role, key)
    #   Uses role.get_property(role, key)
    #
    # This method needs to be extended for new role settings.
    # Without additional properties, this can be omitted.
#   @staticmethod
#   def do_get_dbus_property(x, prop):
#       # Cover additional settings and return a proper dbus type.
#       if prop == "myownsetting":
#           return dbus.String(x.get_property(x, prop))
#       raise RolekitError(INVALID_PROPERTY, prop)


    # D-Bus Property handling
#    if hasattr(dbus.service, "property"):
#        # property support in dbus.service
#
#        @dbus.service.property(DBUS_INTERFACE_ROLE_INSTANCE, signature='s')
#        @dbus_handle_exceptions
#        def myownsetting(self):
#            return self.get_dbus_property(self, "myownsetting")
