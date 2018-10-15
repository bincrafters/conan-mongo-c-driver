#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conan.packager import ConanMultiPackager
from bincrafters import build_shared

if __name__ == "__main__":
    name = build_shared.get_name_from_recipe()
    username, channel, version = build_shared.get_env_vars()
    reference = "{0}/{1}".format(name, version)
    upload = "https://api.bintray.com/conan/{0}/opensource".format(username.lower())
    bincrafters = "https://api.bintray.com/conan/bincrafters/public-conan"

    builder = ConanMultiPackager(
        username=username,
        channel=channel,
        reference=reference,
        upload=upload,
        remotes=[upload, bincrafters],
        upload_only_when_stable=True,
        stable_branch_pattern="stable/*")

    builder.add_common_builds(shared_option_name=name + ":shared")
    builder.run()
