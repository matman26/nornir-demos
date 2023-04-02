import math
from djxml import xmlmodels

class NumbersExample(xmlmodels.XmlModel):

    class Meta:
        extension_ns_uri = "urn:local:number-functions"
        namespaces = {"fn": extension_ns_uri,}

    all_numbers  = xmlmodels.XPathIntegerListField("//num")
    even_numbers = xmlmodels.XPathIntegerListField("//num[fn:is_even(.)]")
    sqrt_numbers = xmlmodels.XPathFloatListField("fn:sqrt(//num)")

    @xmlmodels.lxml_extension
    def is_even(self, context, number_nodes):
        numbers = [getattr(n, 'text', n) for n in number_nodes]
        return all([bool(int(num) % 2 == 0) for num in numbers])

    @xmlmodels.lxml_extension
    def sqrt(self, context, number_nodes):
        sqrts = []
        for number_node in number_nodes:
            number = getattr(number_node, 'text', number_node)
            sqrts.append(repr(math.sqrt(int(number))))
        return sqrts


def main():
    numbers_xml = u"""
    <numbers>
        <num>1</num>
        <num>2</num>
        <num>3</num>
        <num>4</num>
        <num>5</num>
        <num>6</num>
        <num>7</num>
    </numbers>"""

    example = NumbersExample.create_from_string(numbers_xml)

    print("all_numbers  = %r" % example.all_numbers)
    print("even_numbers = %r" % example.even_numbers)
    print("sqrt_numbers = [%s]" % ', '.join(['%.3f' % n for n in example.sqrt_numbers]))
    # all_numbers  = [1, 2, 3, 4, 5, 6, 7]
    # even_numbers = [2, 4, 6]
    # sqrt_numbers = [1.000, 1.414, 1.732, 2.000, 2.236, 2.449, 2.646]

if __name__ == '__main__':
    main()
