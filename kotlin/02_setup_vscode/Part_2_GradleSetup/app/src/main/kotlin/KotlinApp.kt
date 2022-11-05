package part_2_gradlesetup


class KotlinApp {

    public fun getGreeting() : String {
        return "Hello World in Kotlin from vscode!";
    }
}

fun main() {
    println(KotlinApp().getGreeting())
}