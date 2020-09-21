---
title: "Probably My Greatest Snippet of Code"
layout: post
headerImage: false
tag:
- Math
star: true
category: blog
author: eshaan 
description: "Maple code to to calculate the number of derangements"
---

So what is a derangement?
In combinatorial mathematics, a derangement is a permutation of the elements of a set, such that no element appears in its original position. In other words, a derangement is a permutation that has no fixed points.

So number of these can be estimated pretty nicely using eulers number, but we hate estimations. So I wrote a maple procedure to calculate the number of derangements. 
```
derangement := proc(n) 
option remember; 
if n = 0 then 
return 0; 
end if; 
if n = 1 then 
return 0; 
end if; 
if n = 2 then return 1; 
end if; 
(n - 1)*(derangement(n - 1) + derangement(n - 2)); end proc
```
