

data DecisionTree =
    Leaf {  result :: Class } |
    Node {  value :: String,
            attr :: Attribute,
            children :: [DecisionTree] }

data Attribute = Attribute 
    {   label :: String,
        values :: [String] }

type Class = String

type TrainingData = (Data, Class)

type Data = [(Attribute, String)]

type LabeledAttribute = (Attribute,String,Class)

expandTrainingData :: [TrainingData] -> [LabeledAttribute]
expandTrainingData ((d,c):xs) = map (\(a,s) -> (a,s,c)) d

entropy :: [Double] -> Double
entropy [] = 0
entropy [x] = (-x) * logBase 2 x
entropy (x:xs) = entropy [x] + entropy xs

