---
title: "Boyer–Moore Majority Vote Algorithm"
layout: post
date: 2020-08-17
#headerImage: false
tag:
- Algorithms
- Coding
star: true
category: blog
author: EshaanGandhi 
description: "Pretty cool algorithm"
---
Let's get straight into it. The problem that I came across was as follows:

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

To understand the problem better imagine that an area is conducting an election where for a candidate to win, they have to get more that 50% of the votes. Each candidate is given a numberical id and every time someone votes for the candidate we add the id to the array. So if the array is [7, 7, 9, 10] someone came in voted for candidate number 7, then someone else came in voted for 7 again. Then someone else came in and voted for candidate number 9. So and so forth we populate the array. Since there are going to be a lot of votes we need to find a quick way to get the majority element. This is where this algorithm shines.

Basically we want to see if there is one over powering element like in an election. One number vs all the numbers in the array.

Let the array be
[7, 3, 7, 9, 7, 6, 7, 7, 7, 8, 9]

The length of this array is 11 and there are 6 '7' elements. This makes the desired answer as 7.

The algorihtm basically divides and kills the array. For eg:

[7, 3, | 7, 9, | 7, 6, | 7, 7, 7, 8, 9]

Let's look at the first block: [7, 3] - if this section of the array was disregarded from the array, it would make no difference to the election, because the both 'cancel' each other. So let's look at the code for this algorithm

~~~java
class Solution {
    public int majorityElement(int[] nums) {
        
        int count = 0;
        int contender = 0;
        
        for(int i=0;i<nums.length;i++){
            
            if(count==0){
                contender = nums[i];
            }
            if(contender==nums[i]){
                count++;
            }
            else{
                count--;
            }
        }
        return contender;
    }
}
~~~
