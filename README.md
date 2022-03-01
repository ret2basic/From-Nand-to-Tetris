# nand2tetris

**"nand2tetris"** (From Nand to Tetris) is a collection of projects that let student **build a computer from scratch**. It is a hands-on journey that starts with the most elementary logic gate, called **Nand**. and ends up, 12 projects later, with a **general-purpose computer system capable of running Tetris**. Specifically, the 12 projects are:

1. [Boolean Logic](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/01)
2. [Boolean Arithmetic](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/02)
3. [Memory](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/03)
4. [Machine Language](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/04)
5. [Computer Architecture](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/05)
6. [Assembler](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/06)
7. [Virtual Machine I: Processing](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/07)
8. [Virtual Machine II: Control](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/08)
9. [High-Level Language](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/09)
10. [Compiler I: Syntax Analysis](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/10)
11. [Compiler II: Code Generation](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/11)
12. [Opearting System](https://github.com/ret2basic/From-Nand-to-Tetris/tree/main/projects/12)

# Chapter 1: Boolean Logic

## Course

We know that And gate, Or gate, and Not gate are the most fundamental logical gates of computer hardware. In fact, these three gates can be reduced to Nand gate, and we claim that **Nand gate is THE most fundamental logical gate**. We prove this claim informally:

- According to De Morgan's law, `x Or y = Not((Not a) And (Not y))`, so Or gate is reduced to Not gate and And gate.
- `Not(x) = Nand(x, x)`, so Not gate is reduced to Nand gate.
- `And(x, y) = Not(Nand(x, y))`, so And gate is reduced to Nand gate.

Based on these three observations, And gate, Or gate, and Not gate can be reduced to Nand gate. In nand2tetris, we are given a ready-to-go Nand chip (it is actually the only thing we have) and we are going to build a modern computer on top of it.

## Project

In Project 1, we are going to implement:

- Not
- And
- Or
- Xor
- Mux
- DMux
- Not16
- And16
- Or16
- Mux16
- Or8Way
- Mux4Way16
- Mux8Way16
- DMux4Way
- DMux8Way

The interesting part of this project is the implementation of **multiplexer (Mux)** and **demultiplexer (DMux)**:

- **Multiplexer (Mux)**
  - This chip takes 2 data inputs `a` and `b` as well as a "selector" input `sel` and produces 1 output `out`. If `sel == 0`, then Mux sets `out = a`; otherwise, Mux sets `out = b`.
  - In other words, Mux computes "many to one".
- **Demultiplexer (DMux)**
  - This chip takes 1 data input `in` as well as a "selector" input `sel`. It produces 2 outputs `a` and `b`. If `sel == 0`, then DMux sets `a = in and b = 0`; otherwise, DMux sets `a = 0 and b = in`.
  - In other words, DMux computes "one to many".

**Note:** In HDL, bits are numbered from right to left, starting with 0. For example, we have sel = 110, then:

- `sel[0] = 0`
- `sel[1] = 1`
- `sel[2] = 1`

# Chapter 2: Boolean Arithmetic

## Course

Inside computers, **everything** is represented using binary codes. In this chapter, we are going to play with **binary addition** and **sign convertion**.

A pair of binary numbers can be added bitwise from right to left. For each pair of bits, binary addition produces two outputs: `sum` and `carry`. Note that the last carry bit is the overflow bit. For example, consider 1001 + 1001 = (1)0010 with word size 4. The very first step is adding the LSBs of both operands, that is, `1 + 1`. Here we get `sum = 0` and `carry = 1`. The very last step is adding the MSBs of both operands, that is, `1 + 1`. Again, here we get `sum = 0` and `carry = 1`, but this carry bit exceeds the word size hence is thrown away, so the final result is 0010 instead of 10010. This phenomenon is called **overflow**.

In order to represent negative numbers, we use **2's complement**. Suppose the word size is `n` and `x` is a negative number, then the 2's complement representation of `x` is `2**n - x`. This design is better than the naive "sign bit" design since there is no "positive 0" and "negative 0" issue. To compute the negative of a number, we convert this number to its binary representation, flip all bits, and then add 1 to it. For example, we are given number 4 and we want to compute -4 in 2's complement. The binary representation of 4 is 0100, flip all bits and we get 1011, then add 1 to it we get 1100. That is, -4 = 1100 in 2's complement.

## Project

In Project 2, we are going to implement:

- HalfAdder
- FullAdder
- Add16
- Inc16
- ALU

The interesting part of this project is the implementation of **ALU**.

# Chapter 3: Memory

## Course

The chips that we built in Project 1 and Project 2 are **time-independent** (or **combinational**). In this chapter, we introduce the concept of **time** and move on to **time-dependent** (or **sequential**) logic.

Time is a profound notion. In computer science, we have no way to model **continuous** time as what we are experience in real life. Instead, we divide time into small chunks so that it becomes **discrete**. Each chunk is called a **clock cycle**, and it is the smallest time interval that a computer can measure. The choice of clock cycle is not random. It must follow these two principles:

1. The clock cycle shouldn't be too small, because small clock cycle is not able to handle time delay properly and errors may occur. 
2. The clock cycle shouldn't be too large, because large clock cycle slows down the computer.

In order to balance out these two conditions, **we let clock cycle to be slightly larger than the maximal time delay in any chip in the system**.

With the notion of (discrete) time, we are ready to implement computer memory. Memory chips are designed to "remember", or store, information over time. The low-level devices that facilitate this storage abstraction are named **flip-flop gates**, of which there are several variants. In Nand to Tetris we use a variant named **data flip-flop**, or **DFF**. Like the Nand chip, DFF is given to us so we are not going to implement it. We are going to implement the following types of computer memory:

- Registers
- RAM
- Counter

Note that the "counter" here is just the program counter.

## Project

In Project 3, we are going to implement:

- Bit
- Register
- RAM8
- RAM64
- RAM512
- RAM4K
- RAM16K
- PC

The interesting part of this project is the implementation of **PC**.

**Note:** in HDL, bits are numbered from right to left, starting with 0. For example, we have address = abcdef, then:

- `address[0] = f`
- `address[1] = e`
- `address[2] = d`
- `address[3] = c`
- `address[4] = b`
- `address[5] = a`

# Chapter 4: Machine Language

## Course



## Project

In Project 4, we are going to implement:

- Mult
- Fill

The interesting part of this project is the implementation of **Fill**.

# Chapter 5: Computer Architecture

## Course

The **von Neumann machine** is a practical model that informs the construction of almost all computer platforms today. At the heart of this architecture lies the **stored program** concept: the computer's memory stores not only the data that the computer manipulates but also the instructions that tell the computer what to do. A von Neumann machine contains the following components:

- **Memory (RAM)**
  - *Data memory:* stores data and allows reading/writing.
  - *Instruction memory:* stores the instructions of an executable.
- **Central Processing Unit (CPU)**
  - *Arithmetic Logic Unit (ALU):* handles fundamental computations such as addition and bitwise operations.
  - *Registers:* high-speed and expensive memory that prevents starvation.
    - data registers
    - address registers
    - program counter
    - instruction register
  - *Control Unit:* a binary decoder that decodes instructions into micro-codes.
- **Input and Output (I/O)**
  - *Memory-maped I/O:* create a binary emulation of the I/O device, making it appear to the CPU as if it were a regular linear memory segment.

## Project

In Project 5, we are going to implement:

- Memory
- CPU
- Computer

The interesting part of this project is the implementation of **CPU**.

# Chapter 6: Assembler

## Course



## Project

In Project 6, we are going to implement:



# Chapter 7: Virtual Machine I: Processing

## Course



## Project

In Project 7, we are going to implement:



# Chapter 8: Virtual Machine II: Control

## Course



## Project

In Project 8, we are going to implement:



# Chapter 9: High-Level Language

## Course



## Project

In Project 9, we are going to implement:



# Chapter 10: Compiler I: Syntax Analysis

## Course



## Project

In Project 10, we are going to implement:



# Chapter 11: Compiler II: Code Generation

## Course



## Project

In Project 11, we are going to implement:



# Chapter 12: Operating System

## Course



## Project

In Project 12, we are going to implement:

