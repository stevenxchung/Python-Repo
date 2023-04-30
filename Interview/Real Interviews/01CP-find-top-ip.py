'''
*Custom problem

Given a log with ip addresses and user info find the IP address(es) which access the site most often.
'''
from typing import List


class Solution:
    def findMaxIPs(self, log: List[str]) -> List[str]:
        ips = {}
        max_accesses = []
        for line in log:
            for i in range(0, len(line)):
                # If there is whitespace we know we have found an IP
                if line[i] == ' ':
                    # If key does not exist we need to check for that
                    if line[0:i] not in ips:
                        # First initial value
                        ips[line[0:i]] = 1
                    else:
                        # IP is already there so add to dictionary
                        ips[line[0:i]] += 1
                    # Must break out of loop
                    break

        for ip in ips:
            if ips[ip] == max(ips.values()):
                max_accesses.append(ip)
        return max_accesses


if __name__ == '__main__':
    sample_log = [
        '64.242.88.10 - User 1 - [07/Mar/2004:16:05:49 -0800] \'/GET /twiki/bin/edit/Main/Double_bounce_sender?topicparent=Main.ConfigurationVariables HTTP/1.1\' 401 12846',
        '64.242.88.10 - User 1 - [07/Mar/2004:16:06:51 -0800] \'GET /twiki/bin/rdiff/TWiki/NewUserTemplate?rev1=1.3&rev2=1.2 HTTP/1.1\' 200 4523',
        '64.242.88.10 - User 1- [07/Mar/2004:16:10:02 -0800] \'GET /mailman/listinfo/hsdivision HTTP/1.1\' 200 6291',
        '64.242.88.11 - User 2 - [07/Mar/2004:16:11:58 -0800] \'GET /twiki/bin/view/TWiki/WikiSyntax HTTP/1.1\' 200 7352',
        '64.242.88.11 - User 2 - [07/Mar/2004:16:20:55 -0800] \'GET /twiki/bin/view/Main/DCCAndPostFix HTTP/1.1\' 200 5253',
        '64.242.88.13 - User 3 - [07/Mar/2004:16:23:12 -0800] \'GET /twiki/bin/oops/TWiki/AppendixFileSystem?template=oopsmore¶m1=1.12¶m2=1.12 HTTP/1.1\' 200 11382',
    ]
    test = Solution()
    print(test.findMaxIPs(sample_log))
