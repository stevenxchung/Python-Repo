'''
Given a log with ip addresses and user info find the IP address(es) which access the site most often.
'''


class Solution:
    def findMaxIPs(self, log):


samplelog = [
    "64.242.88.10 - User 1 - [07/Mar/2004:16:05:49 -0800] \"/GET /twiki/bin/edit/Main/Double_bounce_sender?topicparent=Main.ConfigurationVariables HTTP/1.1\" 401 12846",
    "64.242.88.10 - User 1 - [07/Mar/2004:16:06:51 -0800] \"GET /twiki/bin/rdiff/TWiki/NewUserTemplate?rev1=1.3&rev2=1.2 HTTP/1.1\" 200 4523",
    "64.242.88.10 - User 1- [07/Mar/2004:16:10:02 -0800] \"GET /mailman/listinfo/hsdivision HTTP/1.1\" 200 6291",
    "64.242.88.11 - User 2 - [07/Mar/2004:16:11:58 -0800] \"GET /twiki/bin/view/TWiki/WikiSyntax HTTP/1.1\" 200 7352",
    "64.242.88.11 - User 2 - [07/Mar/2004:16:20:55 -0800] \"GET /twiki/bin/view/Main/DCCAndPostFix HTTP/1.1\" 200 5253",
    "64.242.88.13 - User 3 - [07/Mar/2004:16:23:12 -0800] \"GET /twiki/bin/oops/TWiki/AppendixFileSystem?template=oopsmore¶m1=1.12¶m2=1.12 HTTP/1.1\" 200 11382"
]
sol = Solution()
print(sol.findMaxIPs(samplelog))
