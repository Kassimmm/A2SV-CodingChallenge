class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("()", "o")
        command = command.replace("(", "")
        command = command.replace(")", "")
        return command  


# class Solution:
#     def interpret(self, command: str) -> str:
#         res = []
#         left = 0
#         while left < len(command):
#             if command[left] == "G":
#                 res.append("G")
#                 left += 1
#             elif command[left] == "(" and command[left+1] == ")":
#                 res.append("o")
#                 left += 2
#             else:
#                 res.append("al")
#                 left += 4
#         return "".join(res)

        
