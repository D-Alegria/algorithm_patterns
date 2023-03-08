from typing import Any


def restore_ip_addresses(s):
    # check that the string that form a valid IP (12 digit or less)
    # Start back tracking with 0 dots, [] results,
    # Base case 1: if the dots are greater than 4 return
    # Base case 2: if the dots == 4 and the current IP is < 255
    # Return results

    # Example: 2. 5.5.255255255

    result = []

    def backtracking(dots, current_ip, i):
        if dots == 4 and i == len(s):
            result.append(current_ip[:-1])
            return

        if dots > 4:
            return

        for j in range(i, min(i + 3, len(s))):
            subnet = s[i:j + 1]
            if int(subnet) < 256 and (i == j or s[i] != '0'):
                backtracking(dots + 1, current_ip + subnet + '.', j + 1)

    backtracking(0, "", 0)
    return result


if __name__ == '__main__':
    # input streams of IP addresses
    ip_addresses = ["0000", "25525511135", "12121212",
                    "113242124", "199219239", "121212", "25525511335", "12012012"]

    # loop to execute till the length of input IP addresses
    for i in range(len(ip_addresses)):
        print(i + 1, ".\t Input addresses: '", ip_addresses[i], "'", sep="")
        print("\t Possible valid IP Addresses are: ",
              restore_ip_addresses(ip_addresses[i]), sep="")
        print("-" * 100)
