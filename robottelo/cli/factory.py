#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: ts=4 sw=4 expandtab ai

import logging

from robottelo.cli.model import Model
from robottelo.cli.proxy import Proxy
from robottelo.cli.user import User
from robottelo.common import conf
from robottelo.common.constants import FOREMAN_PROVIDERS
from robottelo.common.helpers import generate_name, generate_string
from robottelo.cli.computeresource import ComputeResource


logger = logging.getLogger("robottelo")


def update_dictionary(default, updates):
    """
    Updates default dictionary with elements from
    optional dictionary.

    @param default: A python dictionary containing the minimal
    required arguments to create a CLI object.
    @param updates: A python dictionary containing attributes
    to overwrite on default dictionary.

    @return default: The modified default python dictionary.
    """

    if updates:
        for key in set(default.keys()).intersection(set(updates.keys())):
            default[key] = updates[key]

    return default


def create_object(cli_object, args):
    """
    Creates <object> with dictionary of arguments.

    @param cli_object: A valid CLI object.
    @param args: A python dictionary containing all valid
    attributes for creating a new object.
    @raise Exception: Raise an exception if object cannot be
    created.
    """

    result = cli_object().create(args)

    # If the object is not created, raise exception, stop the show.
    if result.return_code != 0 and not cli_object().exists(
            ('name', args['name'])):

        logger.debug(result.stderr)  # Show why creation failed.
        raise Exception("Failed to create object.")


def make_model(options=None):
    """
    Usage:
        hammer model create [OPTIONS]

    Options:
        --name NAME
        --info INFO
        --vendor-class VENDOR_CLASS
        --hardware-model HARDWARE_MODEL
    """

    args = {
        'name': generate_name(),
        'info': None,
        'vendor-class': None,
        'hardware-model': None,
    }

    # Override default dictionary with updated one
    args = update_dictionary(args, options)
    create_object(Model, args)

    return args


def make_proxy(options=None):
    """
    Usage:
        hammer proxy create [OPTIONS]

    Options:
        --name NAME
        --url URL
    """

    args = {
        'name': generate_name(),
        'url': 'http://%s:%s' % (generate_string('alpha', 6),
                                 generate_string('numeric', 4)),
    }

    args = update_dictionary(args, options)
    create_object(Proxy, args)

    return args


def make_user(options=None):
    """
    Usage:
        hammer user create [OPTIONS]

    Options:
        --login LOGIN
        --firstname FIRSTNAME
        --lastname LASTNAME
        --mail MAIL
        --admin ADMIN                 Is an admin account?
        --password PASSWORD
        --auth-source-id AUTH_SOURCE_ID
    """

    login = generate_name(6)

    #Assigning default values for attributes
    args = {
        'login': login,
        'firstname': generate_name(),
        'lastname': generate_name(),
        'mail': "%s@example.com" % login,
        'admin': None,
        'password': generate_name(),
        'auth-source-id': 1,
    }

    args = update_dictionary(args, options)
    create_object(User, args)

    return args


def make_compute_resource(options=None):
    """
    Usage:
        hammer compute_resource create [OPTIONS]

    Options:
        --name NAME
        --provider PROVIDER           Providers include Libvirt, Ovirt, EC2,
            Vmware, Openstack, Rackspace, GCE
        --url URL                     URL for Libvirt, Ovirt, and Openstack
        --description DESCRIPTION
        --user USER                   Username for Ovirt, EC2, Vmware,
            Openstack. Access Key for EC2.
        --password PASSWORD           Password for Ovirt, EC2, Vmware,
            Openstack. Secret key for EC2
        --uuid UUID                   for Ovirt, Vmware Datacenter
        --region REGION               for EC2 only
        --tenant TENANT               for Openstack only
        --server SERVER               for Vmware
        -h, --help                    print help
    """
    options = options or {}
    args = {
        'name': generate_name(8, 8),
        'provider': FOREMAN_PROVIDERS['libvirt'],
        'url': "qemu+tcp://%s:16509/system" %
            conf.properties['main.server.hostname']
    }

    args = update_dictionary(args, options)
    create_object(ComputeResource, args)

    return args
