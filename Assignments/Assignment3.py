def input_students():
    students = []
    n = int(input("Enter number of students: "))
    for i in range(1, n + 1):
        name = input(f"Enter student {i} name: ")
        score = float(input(f"Enter {name}'s score: "))
        students.append((name, score))
    return students


def print_students(students):
    print("\nAll students and scores:")
    for name, score in students:
        print(f"{name} - {score}")



def sum_scores_recursive(scores):
    if not scores:
        return 0
    return scores[0] + sum_scores_recursive(scores[1:])


def average_score(students):
    if not students:
        return 0
    scores = [score for _, score in students]
    total = sum_scores_recursive(scores)
    return total / len(scores)


def top_student(students):
    if not students:
        return None
    top = students[0]
    for student in students:
        if student[1] > top[1]:
            top = student
    return top


def failed_students(students):
    return [name for name, score in students if score < 60]


def main():
    students = input_students()
    print_students(students)

    avg = average_score(students)
    top = top_student(students)
    failed = failed_students(students)

    print(f"\nAverage score: {avg:.1f}")

    if top:
        print(f"Top student: {top[0]} ({top[1]})")
    else:
        print("No students entered.")

    if failed:
        print("Failed students:", ", ".join(failed))
    else:
        print("No failed students!")


if __name__ == "__main__":
    main()
