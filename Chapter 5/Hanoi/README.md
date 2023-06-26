## Exercise
The Tower of Hanoi is a mathematical game or puzzle consisting of three rods and a number of disks of various diameters, which can slide onto any rod. 

![Alt text](600px-Tower_of_Hanoi.jpg)

The objective of the puzzle is to move the entire stack to the last rod, obeying the following rules.

1. Only one disk may be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
3. No disk may be placed on top of a disk that is smaller than it. 

Write a code that inputs the number of disks, outputs each step in solving the puzzle, and outputs the number of moves required to solve the puzzle. 

Note that **`A`** refers to the first rod, **`B`** refers to the middle rod, and **`C`** refers to the last rod.

## Example
### input
<pre>
4
</pre>
### output
<pre>
A → B
A → B
C → B
A → B
C → B
C → B
A → B
A → B
C → B
C → B
A → B
C → B
A → B
A → B
C → B
The number of movements is 15.
</pre>