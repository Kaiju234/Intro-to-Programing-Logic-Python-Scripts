County = input("Enter the county name: ")
County = County.lower()


if County == "bay":
    print("The tax rate for Bay County is 7.00 percent.")
elif County == "franklin":
    print("The tax rate for Franklin County is 7.00 percent.")
elif County == "holmes":
    print("The tax rate for Holmes County is 7.50 percent.")
elif County == "lee":
    print("The tax rate for Lee County is 6.50 percent.")
else:
    print("Enter the County Name again.")
