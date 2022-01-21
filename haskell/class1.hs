-- class 1 examples

e0z :: Int -> Int
e0z x = x ^ 2

e0b :: Int -> Int -> Int
e0b x y = x * y

e0ba :: Int -> (Int -> Bool) -- do not need parentheses
e0ba x y = x < y 

e1 :: (Int -> Int) -> Bool -- do need parentheses
e1 h = h 0 == 0

e0a :: (a,a) -> a
e0a (x,y) = x
