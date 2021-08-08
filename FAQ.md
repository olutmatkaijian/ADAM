## Why the SSL?

The suite works with the client identifying using a unique identifier
and a pre-shared key. Sending a pre-shared key unencrypted is like 
sending your credit card number, it's expiry date and it's CCV using
a post card: Anybody could use it. 
Furthermore, so that people can't insert junk into the databases.

TL;DR: To prevent man-in-the-middle attacks.

# Why is there a LEGACY_LISTENER and why shouldn't it be used

I included the LEGACY_LISTENER for something my father is developing,
which can only send information in clear text. Since this information
is inserted into a database, it's inherently insecure (anybody could
insert something into the database who has access to the ADAM server,
even with regex rules, I would not trust it). 
This could be mitigated with a good network plan, but best practice
is not to use it at all. 
To disable it, set "USE_LEGACY_LISTENER" to "False" or "0" in 
server configuration

NOTE: LEGACY_LISTENER is not implemented yet

# Why is ADAM and it's client asynchronous?
To allow it to run tasks that do not block each other, like recieving
measurement data, controlling the process, inserting and recieving data
from the databases, and so on.

# When will it be finished? 

I don't know. When it will be finished.

# Why is there no user interface yet?

Because it's not developed yet. I'm not even sure what libraries to
use for the frontend.

# Why control the GPIO down to the pin?

To give the software and user more flexibility. It shouldn't matter
if you want to control a jam preserver, a toaster or a giant industrial
plant. By making it possible to control each and every GPIO pin of 
every device connected to ADAM, it allows for very very granular control
schemes. 

# Is ADAM secure?

I do not know yet. Once the software is finished, pen-testing is highly
welcome. I am trying my best to make it secure enough to put on an
open web server - something I couldn't do with previous iterations,
because automated attack attempts kept crashing it.
