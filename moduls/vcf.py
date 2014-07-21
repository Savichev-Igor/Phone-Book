import vobject
import click


def create_contact_vcf(final_dict):
    with click.progressbar(final_dict) as bar:
        for number in bar:
            f = open('contacts/'+final_dict[number]+'.vcf', 'w')
            person = vobject.vCard()
            person.add('fn')
            person.add('n')
            FN = final_dict[number].split(' ')
            first_name = FN[0]
            last_name = FN[1]
            person.n.value = vobject.vcard.Name(family=first_name,
                                                given=last_name)
            person.fn.value = final_dict[number]
            person.add('tel')
            person.tel.type_param = "work"
            person.tel.value = number
            f.write(person.serialize())
