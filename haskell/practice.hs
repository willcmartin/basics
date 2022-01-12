-- http://learnyouahaskell.com

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

reverse' :: [a] -> [a]
reverse' [] = []
reverse' (x:xs) = reverse xs ++ [x]

quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) =
    let smSorted = quicksort [a | a <- xs, a <= x]
        bigSorted = quicksort [a | a <- xs, a > x]
    in smSorted ++ [x] ++ bigSorted

zipWith' :: (a -> b -> c) -> [a] -> [b] -> [c]
zipWith' _ [] _ = []
zipWith' _ _ [] = []
zipWith' f (a:as) (b:bs) = f a b : zipWith' f as bs

applyTwice :: (a -> a) -> a -> a
applyTwice f x = f (f x)

map' :: (a -> b) -> [a] -> [b]
map' _ [] = []
map' f (x:xs) = f x : map' f xs

filter' :: (a -> Bool) -> [a] -> [a]
filter' _ [] = []
filter' f (x:xs)
    | f x = x : filter' f xs
    | otherwise = filter' f xs
