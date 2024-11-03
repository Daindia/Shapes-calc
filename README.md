# Shapes-calc
The project calculates the area and perimeter of various shapes, which include circles, triangles, and squares. Each shape has its own equation.

## **Table of Contents**
1. Project Overview
2. Installation
3. Usage 
4. Classes and Methods 
5. Deactivate Virtual Environment
## **Project Overview**
This project utilizes OOP to imitate a calculator for area and perimeter of various shapes. It allows users to calculate area and perimeter, utilises both class and instance variables. It demonstrates inheritance and polymorphism, with the `Shapes` superclass and subclasses `Cirle`, `Triangle` and `Square`.
## **Installation**
```
git clone https://github.com/Daindia/Shapes-calc.git
cd Shapes-calc
```
### **Creating a virtual environment:**

`python -m venv Shapes-calc`

### **Activating the virtual environment**
1. **For Windows:**\
   `.\Shapes-calc\Scripts\activate`
   
3. **For Linux:**\
   `source shapes-calc/bin/activate`

## **Usage**
> Runs with any code editor that supports python
- **You can create a `Circle`, `Triangle`, & `Square` object like:**
  ```python
  circle = Circle(radius = 12)
  triangle = Triangle(base=5, height=8, side_1=9, side_2=6)
  square = Square(side=5)
  ```
  
- **You can calculate the area like this:**
  ```python
  circle.calc_area()
  triangle.calc_area()
  square.calc_area()
  ```

- **You can also calculate the perimeter like this:**
  ```python
  circle.calc_perimeter()
  triangle.calc_perimeter()
  square.calc_perimeter()
  ```
## **Classes and Methods**
> This project uses one super class and three subclassess to represent shapes and the calculator system
- `Shapes` : A base class with methods `calc_area()` and `calc_perimeter`.
- `Circle`, `Triangle` and `Square` : Subclasses that inherit from the base class, and ovrrides `calc_area()` and `calc_perimeter` to produce unique equations. They also initialize their own instance variables.
## **Deactivate Virtual Environment**
`deactivate`
