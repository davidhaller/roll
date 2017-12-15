# roll

`roll` is a command line tool which simulates rolling a die like those used in Dungeons and Dragons, the Pen and Paper role playing game.

## Usage

Run the roll script from your command line. You will get a shell-like prompt where you can enter roll commands like this:

    $ roll
    roll> 1d20 + 4
    [15] + 4 = 19
    roll> 2d8
    [6, 1] + 0 = 7
    roll> 3 * d6 - 1
    [6] - 1 = 5
    [3] - 1 = 2
    [4] - 1 = 3

Quit the program by typing `exit` or `quit`.

You can also pipe commands into `roll`:

    $ echo "1d12 + 3; 1d4; 6d6 - 1" | roll
    [8] + 3 = 11
    [3] + 0 = 3
    [5, 6, 4, 2, 1, 6] - 1 = 23

If you want bash-like command history controlled by your arrow keys, I recommend using `rlwrap`, which should be available through your distribution's package repository.

    $ rlwrap roll

## Dependencies

You will only need a Python interpreter installed. No external dependencies required.