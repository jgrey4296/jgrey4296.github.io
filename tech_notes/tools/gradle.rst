.. -*- mode: ReST -*-

.. _gradle:

======
Gradle
======

.. contents:: Contents
   :local:

`Gradle <gradle_home>`_ is a build tool with a kotlin DSL.
The problem is that DSL is extensible and not easily discoverable.
These are my notes from having hacked around in it.

.. include:: example_build.gradle.kts
   :code: kotlin

-----------------------------------
Important Files and Implicit Values
-----------------------------------

Gradle builds rely on `settings.gradle.kts`, `build.gradle.kts`,
`init.gradle.kts` and `gradle.properties` files.
Some builds also use a `libs.versions.toml` file in the `gradle` directory.
Crucially, those kotlin files each are implicitly bound to three different
object types:
the `Settings <gradle_settings_object>`_, `Project <gradle_project_object>`_,
and the `script <gradle_script_object>`_ objects.

In practice, this means that in a `build.gradle.kts` file, when you see `version
= "1.0"`, that is setting `Project.version`.

   
------------------------------------------
Containers and Kotlin's Type-safe builders
------------------------------------------

https://kotlinlang.org/docs/type-safe-builders.html


---------------------------
Kotlins Extension Functions
---------------------------

https://kotlinlang.org/docs/extensions.html


------------------
Declarative...ish
------------------

plugins at the top of the file, sourcesets before configurations.

------------
Dependencies
------------

------------
Sub Projects
------------

setting the build directory


-------------
Writing Tasks
-------------

-------------
Useful Idioms
-------------

-------
Plugins
-------

Java
----

Kotlin
------

Android
-------

Plugin Scripts
--------------

Gradle typically wants you to put local scripts in a `buildSrc` directory.
If you don't want to do that, you can write free-standing scripts and call `apply(from="my.gradle.kts")`
in a `build.gradle.kts` to have custom plugins. They typically look like:

.. include:: example_script.gradle.kts
   :code: kotlin


.. --------------------------------------------------
.. Links
.. --------------------------------------------------
   
.. _gradle_home: https://docs.gradle.org/current/userguide/userguide.html

.. _gradle_project_object: https://docs.gradle.org/current/kotlin-dsl/gradle/org.gradle.api/-project/index.html

.. _gradle_settings_object: https://docs.gradle.org/current/kotlin-dsl/gradle/org.gradle.api.initialization/-settings/index.html

.. _gradle_script_object: https://docs.gradle.org/current/kotlin-dsl/gradle/org.gradle.api/-script/index.html

.. _gradle_task_interface: https://docs.gradle.org/current/kotlin-dsl/gradle/org.gradle.api/-task/index.html
