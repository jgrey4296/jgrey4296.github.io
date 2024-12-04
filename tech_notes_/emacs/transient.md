# Transient

[Transient Macros](https://github.com/jgrey4296/jg-el-macros)

## Modifying Transient

I Have a main 'Toggles' transient, which I build in a function,
which also runs hooks that add sub-transients to it:

```lisp

(defun build-main-transient ()
    (transient-define-prefix my-toggles-main ()
    "Main toggle transient"
    [["Global Triggers"
        ...
    ]]
    ["Subsections" []]
    transient-quit!
    )

    (run-hooks 'my-transient-builder-hooks)
)

```

### pcase pattern

Each hook looks like the following:

```lisp

(defun make-a-sub-transient ()
    (transient-define-prefix a-sub-transient () ...)

    (pcase (transient-get-suffix 'my-toggles-main '(1 -1))
        ((and `[1 transient-columns nil ,x]
            (guard (< (length x) 4)))
        ;; Add to existing column section
        (transient-append-suffix 'my-toggles-main
            '(1 -1 -1)  a-sub-transient))
        (t (transient-append-suffix 'my-toggles-main
        ;; Add a new column section
        '(1 -1)  [ a-sub-transient ]))
    )
)

```

Notice the `pcase` usage. It inspects the existing main transient,
looking at the second section ("subsections"), at the last subelement.
It adds just the sub-transient to an existing column, if the column is 4 or less rows. Otherwise it adds a new column.

### transient-quit!

Also, I have a prefix segment called `transient-quit!`.
This adds a default binding of `q` to quit the transient,
returning to the previous prefix if there is one.

```lisp

(defvar transient-quit!
  [
   ""
   [("q" "Quit Local" transient-quit-one)]
   [("Q" "Quit Global" transient-quit-all)]
   [("|" "Quit" transient-quit-all)]
   ]
  " Reusable simple quit for transients "
)

```

### Formatting functions

- TODO: `transient-title-mode-formatter`
- TODO: `fmt-as-bool!`

### Prefix construction macros

- TODO: `transient-make-mode-toggle!`
- TODO: `transient-make-var-toggle!`
- TODO: `transient-make-call!`
- TODO: `transient-make-int-call!`
- TODO: `transient-make-subgroup!`
- TODO: `transient-args!`
