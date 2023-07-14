from utils.utils import cal_total_min, average_total_sec, frequency_count


def total_in_vs_out():
    '''
    Person wise Total Outgoing VS Incoming
    '''
    field_dict = {'Status': 'Answered'}

    group_by = ['Name', 'Direction']
    col_name = 'Minute'
    title = 'Person wise Total Outgoing VS Incoming'

    fig_attr = {'color': 'Direction', 'barmode': 'group'}

    kwrgs = {'field_dict': field_dict, 'group_by': group_by, 'function': cal_total_min,
             'col_name': col_name, 'title': title, 'fig_attr': fig_attr}
    return kwrgs


def person_wise_total_call():
    '''
    Total Duration of Calls with Each Person
    '''
    field_dict = {'Status': 'Answered'}

    group_by = ['Name']
    col_name = 'Minute'
    title = 'Total Duration of Calls with Each Person'

    kwrgs = {'field_dict': field_dict, 'group_by': group_by, 'function': cal_total_min,
             'col_name': col_name, 'title': title}
    return kwrgs


def avg_talktime():
    '''
    Average Talk-Time with Each Person
    '''
    field_dict = {'Status': 'Answered'}

    group_by = ['Name', 'Direction']

    col_name = 'Seconds'
    title = 'Average Talk-Time with Each Person'

    fig_attr = {'color': 'Direction', 'barmode': 'group'}

    kwrgs = {'field_dict': field_dict, 'group_by': group_by, 'function': average_total_sec,
             'col_name': col_name, 'title': title, 'fig_attr': fig_attr}
    return kwrgs


def missed_call():
    '''
    Who gave me Most Missed Call
    '''
    field_dict = {'Status': 'Missed'}

    group_by = ['Name']
    col_name = 'Frequency'
    title = 'Who gave me Most Missed Call'

    kwrgs = {'field_dict': field_dict, 'group_by': group_by, 'function': frequency_count,
             'col_name': col_name, 'title': title}
    return kwrgs


def rejected_call_by_me():
    '''
    Call Rejected by Me
    '''
    field_dict = {'Status': 'Call Rejected'}

    group_by = ['Name']
    col_name = 'Frequency'
    title = 'Call Rejected by Me'

    kwrgs = {'field_dict': field_dict, 'group_by': group_by, 'function': frequency_count,
             'col_name': col_name, 'title': title}
    return kwrgs


def rejected_call_by_other():
    '''
    My Call Rejected by Other
    '''
    field_dict = {'Status': 'Unanswered'}

    group_by = ['Name']
    col_name = 'Frequency'
    title = 'My Call Rejected by Other'

    kwrgs = {'field_dict': field_dict, 'group_by': group_by, 'function': frequency_count,
             'col_name': col_name, 'title': title}
    return kwrgs


func_dict = {'Total Incoming VS Outgoing': total_in_vs_out,
             'Total Duration of Calls with Each Person': person_wise_total_call,
             'Average Talk-Time with Each Person': avg_talktime,
             'Who gave me Most Missed Call': missed_call,
             'Call Rejected by Me': rejected_call_by_me,
             'My Call Rejected by Other': rejected_call_by_other
             }
