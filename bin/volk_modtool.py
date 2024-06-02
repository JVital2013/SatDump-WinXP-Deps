#!C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_64\python.exe
#!/usr/bin/env python
#
# Copyright 2013, 2014 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#


from volk_modtool import volk_modtool, volk_modtool_config
from optparse import OptionParser, OptionGroup

import os
import sys

if __name__ == '__main__':
    parser = OptionParser();
    actions = OptionGroup(parser, 'Actions');
    actions.add_option('-i', '--install', action='store_true',
                       help='Create a new volk module.')
    parser.add_option('-b', '--base_path', action='store', default=None,
                      help='Base path for action. By default, volk_modtool.cfg loads this value.')
    parser.add_option('-n', '--kernel_name', action='store', default=None,
                      help='Kernel name for action. No default')
    parser.add_option('-c', '--config', action='store', dest='config_file', default=None,
                      help='Config file for volk_modtool.  By default, volk_modtool.cfg in the local directory will be used/created.')
    actions.add_option('-a', '--add_kernel', action='store_true',
                       help='Add kernel from existing volk module. Requires: -n. Optional: -b')
    actions.add_option('-A', '--add_all_kernels', action='store_true',
                       help='Add all kernels from existing volk module. Optional: -b')
    actions.add_option('-x', '--remove_kernel', action='store_true',
                       help='Remove kernel from module. Required: -n. Optional: -b')
    actions.add_option('-l', '--list', action='store_true',
                       help='List all kernels in the base.')
    actions.add_option('-k', '--kernels', action='store_true',
                       help='List all kernels in the module.')
    actions.add_option('-r', '--remote_list', action='store_true',
                       help='List all available kernels in remote volk module. Requires: -b.')
    actions.add_option('-m', '--moo', action='store_true',
                       help='Have you mooed today?')
    parser.add_option_group(actions)

    (options, args) = parser.parse_args();
    if len(sys.argv) < 2:
        parser.print_help()

    elif options.moo:
        print("         (__)    ")
        print("         (oo)    ")
        print("   /------\/     ")
        print("  / |    ||      ")
        print(" *  /\---/\      ")
        print("    ~~   ~~      ")

    else:
        my_cfg = volk_modtool_config(options.config_file);

        my_modtool = volk_modtool(my_cfg.get_map(my_cfg.config_name));


        if options.install:
            my_modtool.make_module_skeleton();
            my_modtool.write_default_cfg(my_cfg.cfg);


        if options.add_kernel:
            if not options.kernel_name:
                raise IOError("This action requires the -n option.");
            else:
                name = options.kernel_name;
            if options.base_path:
                base = options.base_path;
            else:
                base = my_cfg.cfg.get(my_cfg.config_name, 'base');
                my_modtool.import_kernel(name, base);

        if options.remove_kernel:
            if not options.kernel_name:
                raise IOError("This action requires the -n option.");
            else:
                name = options.kernel_name;
            my_modtool.remove_kernel(name);

        if options.add_all_kernels:

            if options.base_path:
                base = options.base_path;
            else:
                base = my_cfg.cfg.get(my_cfg.config_name, 'base');
            kernelset = my_modtool.get_current_kernels(base);
            for i in kernelset:
                my_modtool.import_kernel(i, base);

        if options.remote_list:
            if not options.base_path:
                raise IOError("This action requires the -b option.  Try -l or -k for listing kernels in the base or the module.")
            else:
                base = options.base_path;
            kernelset = my_modtool.get_current_kernels(base);
            for i in kernelset:
                print(i);

        if options.list:
            kernelset = my_modtool.get_current_kernels();
            for i in kernelset:
                print(i);

        if options.kernels:
            dest = my_cfg.cfg.get(my_cfg.config_name, 'destination');
            name = my_cfg.cfg.get(my_cfg.config_name, 'name');
            base = os.path.join(dest, 'volk_' + name);
            kernelset = my_modtool.get_current_kernels(base);
            for i in kernelset:
                print(i);
