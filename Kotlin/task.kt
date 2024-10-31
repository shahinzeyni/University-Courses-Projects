fun main(){
    LoopFor()
    conditionFunc()
    add()
    main1()
    println("Hellp World!")
}

fun main1(){
    val name = "Shahin"
    var age = 22
    println(name)
    println(age)

    age = 23
    
    println("Name: $name, Age: $age")

    val isStudent: Boolean = true
    println("$name is student $isStudent")
}

fun add(){
    var a = 5
    var b = 10

    println("a + b = ${a + b}")
    println("a * b = ${a * b}")
}

fun conditionFunc(){
    var score = 100
    if (score >= 90){
        println("Excellent")
    }else if (score >= 60){
        println("Good")
    }else{
        println("Try harder")
    }


    val a = 'a'
    println(a.isLowerCase()) // true
    println(a.isDigit()) // false
}

fun LoopFor(){
    for (i in 1..5){
        println(i)
    }

    var count = 1
    while(count <= 5){
        println(count)
        count++
    }
}

fun stringFunc(){
    var text: String = "Hello World"
}