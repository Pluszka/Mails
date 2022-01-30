#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open('./Input/Letters/starting_letter.txt') as letter:
    letter = letter.readlines()

print(letter)
with open('./Input/Names/invited_names.txt') as names:
    names = names.readlines()
just_names = []
for name in names:
    just_names.append(name.replace('\n', ""))

to_change = letter[0]

for name in just_names:
    letter[0] = to_change.replace('[name]', f'{name}')
    print(letter)
    # with open(f'.\Output\ReadyToSend\InvitationFor{name}.txt', 'w') as invitation:
    #     invitation.write(str(new_letter))
