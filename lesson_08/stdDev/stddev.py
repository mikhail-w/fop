class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age


def std_dev(person_list):
    total_age = 0
    ages = []
    sqrd_dif_arr = []
    total_people = len(person_list)

    # Calculate the mean (simple average of the numbers).
    for person in person_list:
        age = person.get_age()
        total_age += age
        ages.append(age)

    age_mean = total_age / total_people
    print(
        f"Ages: {ages}\nTotal age: {total_age}\nTotal People: {total_people}\nMean: {age_mean}\n"
    )

    # For each number: Subtract the mean. Square the result.
    for age in ages:
        sqrd_dif_arr.append((age - age_mean) ** 2)
    print(f"For each number:\nSubtract the mean.\nSquare the result:")
    print(f"Squared Differences Array\n{sqrd_dif_arr}\n")

    # Calculate the mean of those squared differences. This is the variance.
    print(f"Squared Difference Array Total: {sum(sqrd_dif_arr)}\n")
    variance = sum(sqrd_dif_arr) / total_people
    print(f"Variance: {variance}\n")

    # Take the square  of that to obtain the population standard deviation.
    standard_div = variance**0.5
    return standard_div


p1 = Person("Kyoungmin", 73)
p2 = Person("Mercedes", 24)
p3 = Person("Beatrice", 48)
person_list = [p1, p2, p3]
answer = std_dev(person_list)
print(f"Standard Deviation: {answer}\n")
