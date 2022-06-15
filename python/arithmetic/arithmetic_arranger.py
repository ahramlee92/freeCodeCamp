def arithmetic_arranger(problems, ans=False):
  # Check problems. The limit is five.
  if len(problems) > 5:
      return "Error: Too many problems."

  firstNum = []
  secondNum = []
  arithmetic = []
  
  # Split problems
  for problem in problems:
      problem = problem.split()
      firstNum.append(problem[0])
      arithmetic.append(problem[1])
      secondNum.append(problem[2])

  # Check operators. Only addition and subtraction are available.
  if "*" in arithmetic or "/" in arithmetic:
      return "Error: Operator must be '+' or '-'."

  # Check number(operand). Only contain digits.
  for i in range(len(firstNum)):
      if not (firstNum[i].isdigit() and secondNum[i].isdigit()):
          return "Error: Numbers must only contain digits."

  # Check operand. Only max of four digits in width
  for i in range(len(firstNum)):
      if len(firstNum[i]) > 4 or len(secondNum[i]) > 4:
          return "Error: Numbers cannot be more than four digits."

  firstLine = []
  secondLine = []
  thirdLine = []
  forthLine = []

  # Make each lines
  for i in range(len(firstNum)):
      if len(firstNum[i]) > len(secondNum[i]):
          firstLine.append(" " * 2 + firstNum[i])
      else:
          firstLine.append(" " * (len(secondNum[i]) - len(firstNum[i]) + 2) + firstNum[i])
  for i in range(len(secondNum)):
      if len(secondNum[i]) > len(firstNum[i]):
          secondLine.append(arithmetic[i] + " " + secondNum[i])
      else:
          secondLine.append(
              arithmetic[i] + " " * (len(firstNum[i]) - len(secondNum[i]) + 1) + secondNum[i])
  for i in range(len(firstNum)):
      thirdLine.append("-" * (max(len(firstNum[i]), len(secondNum[i])) + 2))
    
  # calculate all when ans equals True
  if ans:
      for i in range(len(firstNum)):
          if arithmetic[i] == "+":
              answer = str(int(firstNum[i]) + int(secondNum[i]))
          else:
              answer = str(int(firstNum[i]) - int(secondNum[i]))

          if len(answer) > max(len(firstNum[i]), len(secondNum[i])):
              forthLine.append(" " + answer)
          else:
              forthLine.append(" " * (max(len(firstNum[i]), len(secondNum[i])) - len(answer) + 2) + answer)
      arranged_problems = "    ".join(firstLine) + "\n" + "    ".join(secondLine) + "\n" + "    ".join(
          thirdLine) + "\n" + "    ".join(forthLine)
  else:
      arranged_problems = "    ".join(firstLine) + "\n" + "    ".join(secondLine) + "\n" + "    ".join(thirdLine)
  return arranged_problems