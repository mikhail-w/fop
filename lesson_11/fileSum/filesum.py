def file_sum(txt):
    total = 0
    try:
        with open(txt, "r") as infile:
            for line in infile:
                total += float(line.strip())
                print(total)

        with open("sum.txt", "w") as outfile:
            outfile.write(f"Total: {str(total)}\n")
    except FileNotFoundError:
        print("The file was not found.")


nums = "num.txt"
file_sum(nums)
