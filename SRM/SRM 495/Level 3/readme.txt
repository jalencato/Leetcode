When cat Taro went to an internship, he found a strange elevator in the office's skyscraper.
The skyscraper contains 58 floors.
The elevator is composed of 2 boxes and these 2 boxes move together.
When the lower box stops at the x-th floor, the upper box always stops at the (x+1)-th floor.
The lower box stops only on odd floors (1st, 3rd, 5th, ..., 57th).
The upper box stops only on even floors (2nd, 4th, 6th, ..., 58th).
He is very interested by this elevator, and he wants to
compute the number of possible elevators composed of N boxes in a skyscraper of height H.



The elevators must satisfy the following conditions:
For each floor, exactly one box stops at that floor.
The distance between 2 boxes is an integer and never changes.
More formally, for each pair of boxes (A,B), there must be some integer d
such that box B always stops at the (x+d)-th floor when box A stops at the x-th floor.
If the (x+d)-th floor doesn't exist, box A must not stop at the x-th floor.


Two elevators are different if the following is true.
When the bottommost box is at the first floor, there exists an i such
that a box is at the i-th floor in one elevator and no box is at the i-th floor
in the other elevator. You are given two integers H and N.
Return the number of possible elevators that have N boxes in a skyscraper of height H,
modulo 1,000,000,007.


Solution:
A very nice problem here.
We should consider one core problem:
the whole entity can be structural and cyclical

the first transition is that we have to divide the whole longtitude of the elevator area into
the shortest area to fit the minimum size( e.g we can use the same long elevator into 20-long elevator
and the 120-long elevator, at this time the 20 is the one that is more fit)

the second transition is that we should find how to solve the minimum fit problem
as we go through the whole floors we stop for H/N times
and we have N positions to stop at this time
due to the symmetric factor, we can consider it with exchanging the N and the H