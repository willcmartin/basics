doubleMe x = x + x

doubleUs x y = x*2 + y*2

addThree :: Int -> Int -> Int -> Int
addThree x y z = x + y + z


factorial :: Int -> Int
factorial 0 = 1
factorial a = a * factorial (a-1)

factorial' :: (Integral b) => b -> b
factorial' b
        | b == 0 = 1
        | otherwise = b * factorial' (b-1)


replicate' :: (Num i, Ord i) => i -> i -> [i]
replicate' a b
        | a <= 0 = []
        | otherwise = b:replicate' (a-1) b

-- take' 3 [5,4,3,2,1] ==> [5,4,3]
take' :: (Num i, Ord i) => i -> [a] -> [a]
take' a [_]
        | a <= 0 = []
take' _ [] = []
take' a (x:xs) = x : take' (a-1) xs
