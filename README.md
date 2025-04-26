General idea was to create Phone book based on complicated JSON file with collections included in values of initial dict.
Just for JSON parsing practice.
But I added only one more level which was presented as dict.
That is why some functions (edit_contact, create_new_contact) have checks only for dict 
(it need to be improved for more complicated structures with lists of dicts at lower levels of JSON)

Idea is to replace these checks with recursion possibly, but it is not a good way in case of very lagre JSON parsing.

Maybe you can advise better solution?

Also, I did not apply checks for digit input of Phone Numbers.
I did it with purpose to keep universal way of phone number input
