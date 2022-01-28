import Data.Char
import Data.List

p2 :: (a,b) -> (b,a)
p2 (x,y) = (y,x)

applyTwice :: (a -> a) -> a -> a
applyTwice f x = f (f x) -- or f . f

g4 :: [a -> b] -> [a] -> [b]
g4 = zipWith($)

g7 = map . filter

g5 :: Num a => [a] -> a
g5 = foldr (+) 0
