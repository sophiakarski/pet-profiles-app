from pets import pets

def main():
    print("Hello from pets!")

    # 'pets' is a module
    ali = pets.Pet("Ali", 4, "dog", "male")
    # print(leila.name)
    # leila.describe()
    ali.describe()

if __name__ == "__main__":
    main()
