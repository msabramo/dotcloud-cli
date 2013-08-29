Changelog
=========

v0.9.7
------

- Added support for requests 1.1.0, 1.2.0
- Added `traffic` command to retrieve traffic metrics from the API including request/second and latency for an application
- Added `memory` command to retrieve memory metrics from the API including memory used, memory unused, and memory available
- rsync should know display progress when uploading during `dotcloud push`.
- Fixed bug: password prompt should not break anymore on Windows
- Fixed bug with `--branch` argument when using git or hg to push

v0.9.4
------

- Improved fault tolerance at the request-level (should get rid of the *"Max retries exceeded"* error)
- Improved application feedback when pushing code from a child directory of a connected application.

v0.9.3
------

- Implemented auto-retry when streaming deployment logs (there can be a short delay before the logs start becoming available)
- Added the `dotcloud upgrade` command (enables increasing the container version, similar to `dotcloud push --clean` but for a specific service.)
- Added debug mode through `--debug` (shorthand `-D`) option
- Improved feedback when an exceptional situation occurs (hibernating application, `dotcloud ssh` command, no logs retrieved...)
- Various bugfixes (encoding, timestamp parsing, git local branch detection)
- Doc fixes (`-A` instead of `-a`)

v0.9.2
------

*Initial non-beta release*
