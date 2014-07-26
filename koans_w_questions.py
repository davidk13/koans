     def test_what_exception_do_you_get_when_calling_nonexistent_methods(self):
        """
        What is the Exception that is thrown when you call a method that does
        not exist?

        Hint: launch python command console and try the code in the
        block below.

        Don't worry about what 'try' and 'except' do, we'll talk about
        this later
        """
        try:
            None.some_method_none_does_not_know_about()
        except Exception as ex:
            # What exception has been caught?
            #
            # Need a recap on how to evaluate __class__ attributes?
            #   https://github.com/gregmalcolm/python_koans/wiki/Class-Attribute

            self.assertEqual(__, ex.__class__)

            # What message was attached to the exception?
            # (HINT: replace __ with part of the error message.)
            self.assertMatch(__, ex.args[0])
    
    def test_slicing_lists(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(__, noms[0:1])
        self.assertEqual(__, noms[0:2])
        self.assertEqual(__, noms[2:2])
        self.assertEqual(__, noms[2:20])
        self.assertEqual(__, noms[4:0])
        self.assertEqual(__, noms[4:100])
        self.assertEqual(__, noms[5:0])