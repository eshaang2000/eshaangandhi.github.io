---
title: "Calculating the number of walks possible in a Manhattan Lattice"
layout: post
headerImage: false
tag:
- Math
- Combinatorics
category: blog
author: eshaan 
description: Proof that the number of of walks possible in a manhattan lattice is given by the formula below
---

<!-- Math 454 Eshaan Gandhi

Problem .We want to prove our conjecture: the numbers of walks in a Manhattan lattice
(w/o Broadway) from (0,0) to (m,n) is given by the formula(mm+!·nn!)!

```
Proof.We use the mathematical technique of induction
Base case (m = 0, n) OR (m, n = 0):
There is onlyoneway you could walk up from (0,0) to either (m,0) or (0,n)
Inductive Hypothesis:
Assume the total number of walks you could make from (0,0) to (m-1, n) is((mm+−n1)!−·1)!n! AND
Assume the total number of walks you could make from (0,0) to (m, n-1) is ((mm)!+·(nn−−1)!1)!
Inductive Step: We must show: number of walks from (0,0) to (m,n) is(mm+!·nn!)!
The number of walks to (m,n) are simply the sum of the walks to (m-1, n) and (m, n-1)
```
```
T he number of walks to(m, n) =
(m+n−1)!
(m−1)!·n!
```
## +

```
(m+n−1)!
(m)!·(n−1)!
= (m+n−1)!·
```
## (

## 1

```
(m−1)!·n!
```
## +

## 1

```
m!·(n−1)!
```
## )

```
= (m+n−1)!·
```
## (

## 1

```
(m−1)!·n·(n−1)!
```
## +

## 1

```
m·(m−1)!·(n−1)!
```
## )

## ·

## =

```
(m+n−1)!
(m−1)!·(n−1)!
```
## ·

## (

## 1

```
n
```
## +

## 1

```
m
```
## )

## =

```
(m+n−1)!
(m−1)!·(n−1)!
```
## ·

## (

```
m+n
nm
```
## )

## =

```
(m+n)!
m!·n!
This is the desired result. QED

There is a much faster way to do it and that is using Maple, so that’s pretty ridiculous.
```
## 1 -->

## I have no clue how to compile LaTeX in markdown 

so I have another site where I post my LaTeX stuff. checkout gandhieshaan.me


![Proof](/assets/walksProof-1.png)

<!-- $$\documentclass[12pt]{article}
 
\usepackage[margin=1in]{geometry} 
\usepackage{amsmath,amsthm,amssymb,scrextend}
\usepackage{fancyhdr}
\pagestyle{fancy}

 
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\I}{\mathbb{I}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\Q}{\mathbb{Q}}
\renewcommand{\qed}{\hfill$\blacksquare$}
\let\newproof\proof
\renewenvironment{proof}{\begin{addmargin}[1em]{0em}\begin{newproof}}{\end{newproof}\end{addmargin}\qed}
% \newcommand{\expl}[1]{\text{\hfill[#1]}$}
 
\newenvironment{theorem}[2][Theorem]{\begin{trivlist}
\item[\hskip \labelsep {\bfseries #1}\hskip \labelsep {\bfseries #2.}]}{\end{trivlist}}
\newenvironment{lemma}[2][Lemma]{\begin{trivlist}
\item[\hskip \labelsep {\bfseries #1}\hskip \labelsep {\bfseries #2.}]}{\end{trivlist}}
\newenvironment{problem}[2][Problem]{\begin{trivlist}
\item[\hskip \labelsep {\bfseries #1}\hskip \labelsep {\bfseries #2.}]}{\end{trivlist}}
\newenvironment{exercise}[2][Exercise]{\begin{trivlist}
\item[\hskip \labelsep {\bfseries #1}\hskip \labelsep {\bfseries #2.}]}{\end{trivlist}}
\newenvironment{reflection}[2][Reflection]{\begin{trivlist}
\item[\hskip \labelsep {\bfseries #1}\hskip \labelsep {\bfseries #2.}]}{\end{trivlist}}
\newenvironment{proposition}[2][Proposition]{\begin{trivlist}
\item[\hskip \labelsep {\bfseries #1}\hskip \labelsep {\bfseries #2.}]}{\end{trivlist}}
\newenvironment{corollary}[2][Corollary]{\begin{trivlist}
\item[\hskip \labelsep {\bfseries #1}\hskip \labelsep {\bfseries #2.}]}{\end{trivlist}}
 
\begin{document}
 
% --------------------------------------------------------------
%                         Start here
% --------------------------------------------------------------

\lhead{Math 454}
\chead{Eshaan Gandhi}
%\rhead{\today}
 
% \maketitle
 
\begin{problem}{} %You can use theorem, proposition, exercise, or reflection here.  Modify x.yz to be whatever number you are proving
%Delete this text and write theorem statement here. We can draw the sets $\R$, $\Q$, $\I$, $\Z$, and $\N$. Let's assume our problem was: Prove that: $$(\forall x \in \N) \left [\sum_{i = 0}^{n}i = \frac{n(n+1)}{2}\right ]$$
We want to prove our conjecture: the numbers of walks in a Manhattan lattice (w/o Broadway) from (0,0) to (m,n) is given by the formula ${\frac{(m+n)!}{m!\cdot n!}}$
\end{problem}
 
\begin{proof}
We use the mathematical technique of induction\\
%Note 1: The * tells LaTeX not to number the lines.  If you remove the *, be sure to remove it below, too.
%Note 2: Inside the align environment, you do not want to use $-signs.  The reason for this is that this is already a math environment. This is why we have to include \text{} around any text inside the align environment.
\textbf{Base case (m = 0, n) OR (m, n = 0):} \\There is only {\bfseries one} way you could walk up from (0,0) to either (m,0) or (0,n) \\
\textbf{Inductive Hypothesis: } \\Assume the total number of walks you could make from (0,0) to (m-1, n) is ${\frac{(m+n-1)!}{(m-1)!\cdot n!}}$ AND\\
Assume the total number of walks you could make from (0,0) to (m, n-1) is ${\frac{(m+n-1)!}{(m)! \cdot (n-1)!}}$
\textbf{Inductive Step: } We must show: number of walks from (0,0) to (m,n) is ${\frac{(m+n)!}{m!\cdot n!}}$
\\
The number of walks to (m,n) are simply the sum of the walks to (m-1, n) and (m, n-1) 
\begin{align*}
The\  number\ of\ walks\ to\ (m,n) &= {\frac{(m+n-1)!}{(m-1)!\cdot n!}} + {\frac{(m+n-1)!}{(m)!\cdot (n-1)!}}\\
&=(m+n-1)!\cdot \left( \frac{1}{(m-1)!\cdot n!}+\frac{1}{m!\cdot (n-1)!} \right)\\
&=(m+n-1)!\cdot \left( \frac{1}{(m-1)!\cdot n \cdot (n-1)!}+\frac{1}{m\cdot (m-1)!\cdot (n-1)!} \right)\cdot \\
&=\frac{(m+n-1)!}{(m-1)!\cdot (n-1)!}\cdot \left(\frac{1}{n}+\frac{1}{m}\right)\\
&=\frac{(m+n-1)!}{(m-1)!\cdot (n-1)!}\cdot \left(\frac{m+n}{nm}\right)\\
&=\frac{(m+n)!}{m!\cdot n!}
\end{align*}
This is the desired result. QED

\end{proof}

There is a much faster way to do it and that is using Maple, so that's pretty ridiculous. 
% --------------------------------------------------------------
%     You don't have to mess with anything below this line.
% --------------------------------------------------------------
 
\end{document}$$ -->





