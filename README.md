```uml
@startuml
skinparam shadowing false
scale 2
hide circle

class "Viking" as b {
food:String[]
FoodChoice(food):boolean
FoodRegister(food):boolean
}


class "Meal" as d {

}

class "SetMenu" as s {
food:String[]
moment:String[]
FoodChoice(food:String):boolean
FoodRegister(food:String):boolean
MomentChoice(moment:String):boolean
MomentResister(moment:String):boolean
}
class "FoodList" as slct{
add(foodname:String[]):void
delete(foodname:String[]):void
display(content:String[]):boolean
Check():boolean
}

class "Controller" as x {
  BreakfastVikingSurvey: void
  SetMenuProvide(): void
  FoodAddDelete(): void
  run():void
}

class "MainView" as y {
}

y -- x
x o---> "1\n FoodList" slct
d "0..1" <|-- "1" b
d "0..1" <|-- "1" s
slct "1"-->"1..*" s
slct "1"-->"0..*" b

@enduml
