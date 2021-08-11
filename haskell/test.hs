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
