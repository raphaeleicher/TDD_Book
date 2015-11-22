from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_item(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter ont the empty input box

        # The home page refrehses, and there is an error message saying
        # that list items cannot be blnak

        # She tries atain with som text for the item, which now works

        # Perversely, she now decides to submit a second blank list item

        # She receives a similar warnin on the list page

        # And she can correct it by filling som text in
        self.fail('write me!')

