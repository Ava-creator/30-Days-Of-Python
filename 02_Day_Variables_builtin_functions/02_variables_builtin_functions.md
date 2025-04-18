<div align="center">
  <h1>Python Adventure: Day 2 - Variables and Functions for Little Coders!</h1>
  <sub>
    by Dayo Dayo<br>
    Last edited 13 days ago
  </sub>
</div>

Join Valerie Vole and Fritz Fox on today's exciting journey into the world of Python!  
We'll explore magical containers called "variables" and help our animal friends pack their backpacks with code treasures.

---

- [📘 Day 2](#-day-2)
  - [Built in functions](#built-in-functions)
  - [Variables & Magical Backpacks](#variables--magical-backpacks)
    - [Declaring Multiple Variables in a Line](#declaring-multiple-variables-in-a-line)
  - [Data Types](#data-types)
  - [Checking Data Types and Casting](#checking-data-types-and-casting)
  - [Numbers and Treasures](#numbers-and-treasures)
  - [Introducing Python Functions – Magic Spells](#introducing-python-functions--magic-spells)
  - [💻 Adventure Exercises – Day 2](#-adventure-exercises--day-2)

# 📘 Day 2

## Built in functions

Python provides loads of built-in functions that are ready to use without any extra setup. Our adventure guides (Valerie and Fritz) will use these functions as magical tools to inspect their treasures. Some common ones include: _print()_, _len()_, _type()_, _int()_, _float()_, _str()_, _input()_, _list()_, _dict()_, _min()_, _max()_, _sum()_, _sorted()_, and even _help()_ and _dir()_.

![Built-in Functions](../images/builtin-functions.png)

Let’s begin our quest in the Python shell and experiment with these magic tools!

![Built-in functions](../images/builtin-functions_practice.png)

Watch how Valerie and Fritz use these functions to reveal secrets of their magical items. Notice that Python even reserves certain words (reserved words) as special; these are like enchanted spells you cannot use to name your backpacks!

![Help and Dir Built in Functions](../images/help_and_dir_builtin.png)

As seen above, reserved words are off limits for naming your variables. Now, let’s pack our adventure backpacks!

![Min Max Sum](../images/builtin-functional-final.png)

## Variables & Magical Backpacks

Variables are like magical backpacks that store all kinds of treasures—from numbers and words to secret messages. Just like every adventurer needs a uniquely named backpack, variables require names that follow some friendly rules:

- Must start with a letter or an underscore (think of these as your secret symbols).
- Cannot start with a number.
- Can only contain letters, numbers, and underscores.
- And remember, names are case-sensitive. _magicPack_ and _Magicpack_ are not the same!

### Valid Backpack Names (Variables)

```shell
acorn_count
treasure
first_name
last_name
_country
```

Invalid names would be like using broken or forbidden symbols:

```shell
first-name
first@name
1treasure
```

We use snake_case naming for our backpacks to keep things neat (for example: first_name, last_name).

### Adventurer’s Example: Packing the Backpacks

Below is an example showing how Valerie and Fritz pack and update their variable backpacks.

```py
# Valerie's Variable Acorn Counter
acorn_count = 5              # Create the backpack with 5 acorns
acorn_count = acorn_count + 3  # Add 3 more acorns to the backpack
acorn_count = acorn_count - 2  # Share or lose 2 acorns

print("Valerie's acorn count:", acorn_count)
```

```py
# Fritz's Treasure Chest
treasure = "shiny"    # Initially, the treasure is shiny
treasure = "sparkly"  # Then, Fritz notices it is sparkly
treasure = "golden"   # Finally, he calls it golden

print("Fritz's treasure is now:", treasure)
```

### Unpacking Our Magical Backpacks

See how you can create a new adventure variable and then check what’s inside:

```py
magic_pack = 8  # Our new magical backpack!
print("Magic pack contains:", magic_pack)
```

### Declaring Multiple Variables in a Line

For quick packing, you can declare multiple variables at once. Just like packing several treasures in one go:

```py
first_name, last_name, country, age, is_married = 'Valerie', 'Vole', 'Wonderland', 10, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name:', last_name)
print('Country:', country)
print('Age:', age)
print('Married:', is_married)
```

You can even collect treasures from fellow adventurers using the built-in _input()_ function:

```py
first_name = input('What is your adventurer name: ')
age = input('How many years of adventure? ')

print("Welcome to the journey,", first_name)
print("Age:", age)
```

---

## Data Types

In our magical world, every treasure has a type. Data types tell us what kind of treasure a variable holds. We can use the _type_ function to peek inside our backpacks:

```py
first_name = 'Valerie'   # a string treasure
age = 10                 # an integer treasure
pi_value = 3.14          # a float treasure

print(type(first_name))  # shows: <class 'str'>
print(type(age))         # shows: <class 'int'>
print(type(pi_value))    # shows: <class 'float'>
```

---

## Checking Data Types and Casting

Before using a treasure, it’s wise to check its type and even change its form (casting) when needed. For instance:

```py
# Converting an integer treasure to a float:
num_int = 10
num_float = float(num_int)
print('Converted treasure:', num_float)
```

Casting lets you transform treasures so you can combine them in your spells (arithmetic operations)!

```py
# From string treasure to a list of characters:
name = "Valerie"
name_list = list(name)
print(name_list)  # Reveals each letter as a separate treasure
```

---

## Numbers and Treasures

Our world is full of numbers that come in different forms:

1. **Integers:** Like counting acorns (..., -3, -2, -1, 0, 1, 2, 3, …)
2. **Floats:** Treasures with decimals (e.g., 3.14, 2.71)
3. **Complex Numbers:** A bit magical, with a twist (1 + 1j)

🌕 You are awesome—completing these challenges means you are growing stronger on your adventure!

---

## Introducing Python Functions – Magic Spells

Functions are like magic spells that perform a special task whenever you call them. Write your spell once, then use it again and again to help your friends on their journey.

### Creating Our First Function

Let’s define a simple greeting spell for adventurers:

```py
def greet_user():
    print("Hello, adventurer!")
    
# Casting the greeting spell
greet_user()
```

- **Define Function:** Use the keyword `def` to start your spell.
- **Name Function:** Give it a magical name like `greet_user`.
- **Add Code:** Write the code (the spell words) indented beneath the definition.
- **Call the Spell:** Simply call the function’s name to activate the magic.

---

## 💻 Adventure Exercises – Day 2

Now it’s your turn to pack your own coding backpack and cast some magic spells!

### Exercises: Level 1

1. Inside the *30DaysOfPython* folder, create a `day_2` folder. In that folder, create a file called `variables.py`.
2. Start with a Python comment:  
  `# Python Adventure: Day 2 - Variables and Functions for Little Coders!`
3. Declare a variable **first_name** and assign it your adventurer name (e.g., `"Valerie"`).
4. Declare a variable **last_name** and assign it your family name (e.g., `"Vole"`).
5. Create a variable **full_name** by combining **first_name** and **last_name**.
6. Declare a variable **country** for your adventure land (e.g., `"Wonderland"`).
7. Declare a variable **city** where your adventure begins (e.g., `"Rabbit Hole"`).
8. Declare a variable **age** with your adventure age (e.g., `10`).
9. Declare a variable **year** representing the current adventure year (e.g., `2023`).
10. Create a variable **is_married** (True or False) as a fun fact about your journey.
11. Declare a variable **is_ready** (or **is_light_on**) to signal if you are ready for adventure.
12. Try declaring multiple variables on one line (like packing several treasures at once), for example:  
   ```py
   first_name, last_name, country, age, is_married = 'Valerie', 'Vole', 'Wonderland', 10, False
   ```

### Exercises: Level 2

1. Use the _type()_ built-in function to check the type of all your adventure variables. For example:  
   ```py
   print(type(first_name))  # <class 'str'>
   print(type(age))         # <class 'int'>
   ```
2. Use _len()_ to find the length (number of characters) in your **first_name**.  
   ```py
   print(len(first_name))  # e.g., 7 for "Valerie"
   ```
3. Compare the lengths of your **first_name** and **last_name**.  
   ```py
   print(len(first_name) > len(last_name))  # True or False
   ```
4. Declare two numerical treasures: assign `5` to **num_one** and `4` to **num_two**. Perform the following operations:  
   - Add them and save the result in **total**.  
   - Subtract them and save the result in **diff**.  
   - Multiply them to get **product**.  
   - Divide **num_one** by **num_two** and call it **division**.  
   - Use modulus division for **remainder** (what’s left when dividing).  
   - Calculate **num_one** raised to the power of **num_two** as **exp**.  
   - Perform floor division (integer division) and store it in **floor_division**.  
   Example:  
   ```py
   num_one, num_two = 5, 4
   total = num_one + num_two
   diff = num_one - num_two
   product = num_one * num_two
   division = num_one / num_two
   remainder = num_one % num_two
   exp = num_one ** num_two
   floor_division = num_one // num_two
   print(total, diff, product, division, remainder, exp, floor_division)
   ```
5. The radius of a circle is `30` meters. Perform the following:  
   - Calculate the area of the circle; store it as **area_of_circle**.  
    Formula: `area = π * radius ** 2`  
   - Calculate the circumference; store it as **circum_of_circle**.  
    Formula: `circumference = 2 * π * radius`  
   - Then, let the circle’s radius be found with a user input and calculate its area.  
   Example:  
   ```py
   import math
   radius = 30
   area_of_circle = math.pi * radius ** 2
   circum_of_circle = 2 * math.pi * radius
   print("Area:", area_of_circle, "Circumference:", circum_of_circle)

   # User input for radius
   radius = float(input("Enter the radius of the circle: "))
   area_of_circle = math.pi * radius ** 2
   print("Area with user input:", area_of_circle)
   ```
6. Use the _input()_ function to get your **first_name**, **last_name**, **country**, and **age** from the user and store them.  
   ```py
   first_name = input("Enter your first name: ")
   last_name = input("Enter your last name: ")
   country = input("Enter your country: ")
   age = int(input("Enter your age: "))
   print(first_name, last_name, country, age)
   ```
7. In the Python shell (or your file), run `help('keywords')` to discover the reserved words (magical incantations) you cannot use as variable names.  
   ```py
   help('keywords')
   ```

---

Happy coding and may your adventure be filled with magical discoveries!
