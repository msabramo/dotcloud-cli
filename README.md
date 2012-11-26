# dotCloud CLI

This is the dotCloud command line interface.

## What's New

This version of CLI is designed to work with the application directory
linked to thremote dotCloud application.

This allows you to avoid typing the same application names multiple
times, and reduce the possiblity of making typos and overwrite wrong
applications by repeating the command line history.

    # New CLI 
    > dotcloud push
    > dotcloud info
    > dotcloud run www bash

    # Old CLI
    > dotcloud push myapp .
    > dotcloud info myapp
    > dotcloud run myapp.www bash

The command line executable is installed as `dotcloud`.

## Setup

First, you have to configure your CLI.

    > dotcloud setup
    Dotcloud Username: your-user-name
    Password: **********

You're asked to provide your username and password for dotCloud, to
register the new CLI client as a dotCloud REST API consumer. You can
also use email, instead of your username.

The CLI won't save this credentials locally - instead, it will save
the OAuth2 access token in the local disk. Once the setup is complete,
you can run the check command to see if everything is configured
correctly.

    > dotcloud check
    --> Checking the authentication status
    OK: Client is authenticated as <your-username>

If this fails, try removing the directory `~/.dotcloud_cli` and start
over from the setup.

## Working with your application

    > cd ~/dev
    > mkdir myapp
    > (write some code)

### Create

Once you've done writing your awesome application, run the `create` command:

    > dotcloud create myapp
    --> Creating a new application called "myapp"
    Application "myapp" created.
    Connect the current directory to "myapp"? [Yn]: y
    --> Connecting with the application "myapp"
    --> Connected.

As you see, the CLI asks you if you want to connect the current
working directory to the remote application. This allows you to omit
typing the application name from now on.

### Running commands

To push the code to the dotCloud platform, simply type:

    > dotcloud push

and it will upload the code from the current directory to the
application. You can see the currently connected application by typing:

    > dotcloud app
    myapp

You can see the list of commands by running `dotcloud -h`.

If you typed `n` when asked to connect the current directory, the CLI
can't find the application name for the commands. You can specify the
application name in such case, using the `--application` (or `-a` for
short) option:

    > dotcloud -a myapp info

You can also use this option when you want to run commands against the
application that you don't have the working directory for.

### Connect

Similarly, if you already have a working directory *and* a dotCloud
remote application and want to connect them together, instead of
creating a new application, run the connect command:

    > cd ~/dev/myapp
    > dotcloud connect myapp

It will link your current working directory with the (existing) dotCloud application `myapp`.

## Contributing

If you've found a bug or have a feature request for the new CLI, the
best way to send feedbacks is to open it in the github issues list.

If you really want to contribute your code by submitting patches (that
is awesome!), fork a project on github, and send us a pull
request. Note that by forking and sending pull requests, you agree to
assign the copyright to dotCloud Inc.

