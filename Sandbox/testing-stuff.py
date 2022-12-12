'''
Keep us out of google search results..

$ od -d /dev/urandom | head
0000000     60215   28778   29227   28548   62686   45171    7826   48766
0000020     17118   15225   12852   34781   31955   19087   39563   43614
0000040      6710   38515   14573   64087   17026   25598   42913   14209
0000060     10723   31307   19071   14798    2462   46253   35626   32436
0000100      1739   27712    5667   12212   47077   41722   54452   38461
0000120      4816   15014   28623   10928   54028   64523   54632   54187
0000140     61631   54499   18307    5514   50743   50591   25172   54018
0000160     31990   26248    4383   46452   42156   62320   51052   28621
0000200     27226   65296   56305   33375    4813   42283   19980    1922
0000220     57061   29322   27073   64986   15219   26234   24100   21204
'''

'''
Copy this file and run `pbpaste | base64` to generate challenge text. Copious
white space is at the bottom of the file to ensure trailing `==` and hint at
base64.
'''

import codecs
import string
import sys
import time

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.twofactor.totp import TOTP


ONE_WEEK_IN_SECONDS = 604_800


def generate_secret():
    totp = TOTP(
        key=codecs.encode(string.ascii_letters, encoding="utf-8"),
        length=8,
        algorithm=SHA1(),
        time_step=ONE_WEEK_IN_SECONDS,
        backend=default_backend(),
    )
    seed = int(time.time())
    token = codecs.decode(totp.generate(seed), encoding="utf-8")
    return f"{token}-{seed}"


if __name__ == "__main__":
    sys.stdout.write(
        f"Please head to https://ramp.com/careers and use this secret when "
        f"you apply: {generate_secret()}\n"
    )


