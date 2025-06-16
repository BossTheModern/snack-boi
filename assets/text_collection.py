# Text collection to store text for fancy printing

class TextCollection: 
    def __init__(self) -> None:
        self._start_intro: str = "I am so hungry today\n" \
                           "It's time to snack!\n" \
                           "This place is huge! I might find something tasty here\n"
        self._extra_snack_intro: str = "Man I'm still hungry as usual\n" \
                                 "Maybe there's something more tasty here\n"
        self._traps_intro: str = "Oh, so you're here\n" \
                           "The infamous snack eater\n" \
                           "I don't know how you got here, but it doesn't matter right now\n" \
                           "I will use you as a test subject for my fancy little inventions\n" \
                           "So go ahead\n" \
                           "Do your worst\n" \
                           "Eat until you're done for. I bet you won't last for long\n"