import subprocess


class Monitor():
    def __init__(self, id='eDP1'):
        self.id = id

    def change_orientation(self, new_orientation):
        if new_orientation not in [0, 90, 180, 270]:
            raise ValueError("New orientation value is not 0, 90, 180, or 270")

        xrandr_orientation_mappings = {
            0: 'normal',
            90: 'right',
            180: 'inverted',
            270: 'left'
        }

        rotate_command = "xrandr --output {id} --rotate {orientation}".format(
            id=self.id,
            orientation=xrandr_orientation_mappings[new_orientation]
        )

        # check_call will raise subprocess.CalledProcessError if we get a nonzero exit status
        subprocess.check_call(rotate_command, shell=True)

