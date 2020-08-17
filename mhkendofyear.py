import xlwings as xw
# column range A to P
# strings range from I to P
class MhkEndOfYear:

    def __init__(self, brm_emails, brms, clients, eoy, current_sit, see_attached, acceptance, issues, price, final_res):
        self.brm_emails = brm_emails
        self.brms = brms
        self.clients = clients
        self.eoy = str(eoy)
        self.current_sit = current_sit
        self.see_attached = see_attached
        self.acceptance = acceptance
        self.issues = issues
        self.price = price
        self.final_res = final_res

    # helper functions
    def number_of_clients(self,sht):
        counter = 2
        checker = sht.range('A%s' % counter).value
        while bool(checker):
            counter += 1
            checker = sht.range('A%s' % counter).value
        return counter

    def brm_finder(self, shrt_brm):
        if bool(shrt_brm):
            splitter = shrt_brm.split(' ')
            first_name = splitter[0]
            last_name = splitter[1]
            if first_name in str(self.brms):
                for full_name in self.brms:
                    if first_name in full_name:
                        fullast = full_name.split(' ')[1]
                        if last_name[0] == fullast[0]:
                            return full_name
                        else:
                            pass
                    else:
                        pass
        print("Name not listed in BRMS list.")
        return None

    def fill_strings(self):
        input_letters = range(65,73)
        output_letters = range(73,81)
        client_col = 'A'
        brm_col = 'C'
        hour_col = 'E'
        """
        contact1_col = 'G'
        contact2_col = 'H'
        """
        current_sit = 'I'
        propose_sol = 'J'
        deliverables = 'K'
        acceptance = 'L'
        client_res = 'M'
        issues = 'N'
        price = 'O'
        final_res = 'P'
        wb = xw.sheets[0]
        client_len = self.number_of_clients(wb)
        for h in range(2,client_len):
            i = str(h)
            for g in input_letters:
                x = chr(g)
                cell_valued = wb.range(x+i).value
                if bool(cell_valued):
                    cell_value = str(cell_valued).strip()
                    if x == client_col:
                        client_full = self.clients[cell_value]
                        cli = cell_value
                    elif x == brm_col:
                        bm = self.brm_finder(cell_value)
                    elif x == hour_col:
                        hr = cell_value[:-2]
                        """
                    elif x == contact1_col:
                        c1 = cell_value
                    elif x == contact2_col:
                        c2 = cell_value
                        """
                    else:
                        pass
                else:
                    if x == client_col:
                        client_full = '______________________________'
                        cli = '____'
                    elif x == brm_col:
                        bm = '______________________'
                    elif x == hour_col:
                        hr = '___'
                    else:
                        pass
            for g in output_letters:
                x = chr(g)
                if x == current_sit:
                    wb.range(x+i).value = self.current_sit.format(client_full, cli, self.eoy)
                elif x == propose_sol:
                    wb.range(x+i).value = self.see_attached.format(self.eoy)
                elif x == deliverables:
                    wb.range(x+i).value = self.see_attached.format(self.eoy)
                elif x == acceptance:
                    wb.range(x+i).value = self.acceptance
                elif x == client_res:
                    wb.range(x+i).value = self.see_attached.format(self.eoy)
                elif x == issues:
                    wb.range(x+i).value = self.issues.format(self.eoy, bm)
                elif x == price:
                    wb.range(x+i).value = self.price.format(times=hr)
                elif x == final_res:
                    wb.range(x+i).value = self.final_res.format(self.brm_emails[bm])
                else:
                    pass
        print("Data has been filled in for EOY " + self.eoy + ".")
        return None

if __name__ == "__main__":
    question = 'What year are you performing EOY for (one year ahead of current).'
    print(question)
    prompt = '>'
    eoy = input(prompt)
    brm_emails = {
        'Angela Clock' : 'aclock@mhk.com',
        'Deborah Hannon' : 'dhannon@mhk.com',
        'Adam Kamen' : 'akamen@mhk.com',
        'Lance Horowitz' : 'lhorowitz@mhk.com',
        'Brian Mclaughlin': 'bmclaughlin@mhk.com',
        'Ian Robbins': 'irobbins@mhk.com',
        None : '______________________',
        '______________________' : '______________________'
    }
    brms = [
        'Angela Clock',
        'Deborah Hannon',
        'Adam Kamen',
        'Lance Horowitz',
        'Brian Mclaughlin',
        'Ian Robbins',
        ]

    clients = {
        'AET' : 'HealthEdge Systems',
        'AVM' : 'AvMed',
        'BCA' : 'Blue Cross Blue Shield of Arizona',
        'BCN' : 'Blue Care Network of Michigan',
        'BPA' : '?????????????????????',
        'CCA' : 'Commonwealth Care Alliance',
        'CHP' : '??????????',
        'DST' : 'DST Health Solutions, Inc.',
        'EIC' : 'Envision Insurance Company',
        'ELD' : 'Elderplan, Inc.',
        'EMB' : 'Emblem Health',
        'EON' : 'Eon Health Plan, LLC',
        'GUN' : 'Quartz',
        'HFN' : 'HF Management Services, LLC.',
        'HNE' : 'Health New England',
        'HPP' : 'Health Partners Plans',
        'HUM' : 'Humana Inc.',
        'KPC' : 'Kaiser Permanente of California',
        'KPW(GHC)' : 'Kaiser Permanente of Washington',
        'MHP' : 'Meridian Health Plan',
        'MMM' : 'MMM Holdings, Inc.',
        'MMF' : 'MMM Holdings, Inc.',
        'MVP' : 'MVP Health Plan Inc',
        'PRS' : 'Presbyterian Health Plan',
        'TUF' : 'Tufts Health Plan',
        'UMH' : 'Univ of Maryland Medical Health Plans'
    }
    current_sit = "{} ({}) uses MarketProminence (MP) to manage their Medicare members. To continue compliance into the new year ('{}'), there are multiple data points outlined in the Proposed Solution section of this scope that need to be updated to allow MP to continue processing member transactions properly."
    see_attached = "See attached pdf—'MarketProminence Year-end {}'."
    acceptance = "Please verify that all deliverables in the attached file are implemented in test and after internal testing is completed, promoted to production. The client is responsible for the items listed under client responsibilities in the attached document. Send email to BRM when items are successfully implemented to production."
    issues = "Any variances determined after loading the January 1st {} MMR file will be investigated once the client initiates a new request {}."
    price = "MHK/MarketProminence estimates {times} hours to complete this project. {times} hours will be deducted from the prepaid amount. Any hours over the monthly hours will first be deducted from the current years remaining rollover hours. Hours in excess of the monthly and carryover will be billed at the contracted postpaid rate."
    final_res = "Please email a signed copy of this scope to {}. Any changes made to this scope will require a new revision and appropriate approvals."
    wb = xw.sheets[0]
    MhkEndOfYear(brm_emails, brms, clients, eoy, current_sit, see_attached, acceptance, issues, price, final_res).fill_strings()
"""
class test:
    def __init__(self, stuff):
        self.stuff = stuff
    def thing(self):
        ano = 'K'
        print(self.stuff.format(ano))
        return None
mine = 'stuff{}'
test(mine).thing()
"""