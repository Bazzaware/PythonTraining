class Formatter:
    def headings(self, headers):
        '''
        Emit the headers
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()

class HTMLFormatter(Formatter):
    '''
    Output data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print('<th>{}</th>'.format(h), end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print('<td>{}</td>'.format(d), end='')
        print('</tr>')

class TextFormatter(Formatter):
    '''
    Output data in plain-text format.
    '''
    def headings(self, headers):
        for h in headers:
            print('{:>20}'.format(h), end=' ')
        print()
        print(('-'*20 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print('{:>20}'.format(d), end=' ')
        print()


def create_formatter(name):
    '''
    Create an appropriate formatter given an output format name
    '''
    if name == 'txt':
        return TextFormatter()
    elif name == 'csv':
        return CSVFormatter()
    elif name == 'html':
        return HTMLFormatter()
    else:
        raise RuntimeError('Unknown format {}'.format(name))
