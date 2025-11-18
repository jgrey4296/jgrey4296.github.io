class JGScriptPlugin: Plugin<Project> {
    /* A Simple Plugin Script Example

    Be aware the 'project' object is not implicit in 'apply'.
    */

    fun simpleFunction () {
        println("simple function")
    }

    override fun apply(project: Project) {
        val providers = project.providers
        project.tasks.register("jg") {
            group = "JG"
            val myname: String? by project
            val myval = "blah"


            doFirst {
                println("---- Starting ----")
                println("Start action")
            }

            doLast {
                println("---- Finishing ----")
                println("Value: ${myname ?: "not provided"}")
                providers.exec {
                    commandLine("echo", myval)
                }
                simpleFunction()
            }

        }
    }
}

// Called when the file is imported with 'apply' in the build.gradle.kts file
// without this, the plugin isn't activated.
apply<JGScriptPlugin>()
