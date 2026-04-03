"""Figure configuration presets for different call-log chart types."""

from utils.utils import average_total_sec, cal_total_min, frequency_count


def _build_config(
    field_dict: dict,
    group_by: list[str],
    function: callable,
    col_name: str,
    title: str,
    fig_attr: dict | None = None,
) -> dict:
    """Build a standardised chart-configuration dictionary."""
    config = {
        "field_dict": field_dict,
        "group_by": group_by,
        "function": function,
        "col_name": col_name,
        "title": title,
    }
    if fig_attr:
        config["fig_attr"] = fig_attr
    return config


DIRECTION_GROUPED = {"color": "Direction", "barmode": "group"}


def total_in_vs_out() -> dict:
    """Person-wise Total Outgoing VS Incoming."""
    return _build_config(
        field_dict={"Status": "Answered"},
        group_by=["Name", "Direction"],
        function=cal_total_min,
        col_name="Minute",
        title="Person wise Total Outgoing VS Incoming",
        fig_attr=DIRECTION_GROUPED,
    )


def person_wise_total_call() -> dict:
    """Total Duration of Calls with Each Person."""
    return _build_config(
        field_dict={"Status": "Answered"},
        group_by=["Name"],
        function=cal_total_min,
        col_name="Minute",
        title="Total Duration of Calls with Each Person",
    )


def avg_talktime() -> dict:
    """Average Talk-Time with Each Person."""
    return _build_config(
        field_dict={"Status": "Answered"},
        group_by=["Name", "Direction"],
        function=average_total_sec,
        col_name="Seconds",
        title="Average Talk-Time with Each Person",
        fig_attr=DIRECTION_GROUPED,
    )


def missed_call() -> dict:
    """Who gave me Most Missed Call."""
    return _build_config(
        field_dict={"Status": "Missed"},
        group_by=["Name"],
        function=frequency_count,
        col_name="Frequency",
        title="Who gave me Most Missed Call",
    )


def rejected_call_by_me() -> dict:
    """Call Rejected by Me."""
    return _build_config(
        field_dict={"Status": "Call Rejected"},
        group_by=["Name"],
        function=frequency_count,
        col_name="Frequency",
        title="Call Rejected by Me",
    )


def rejected_call_by_other() -> dict:
    """My Call Rejected by Other."""
    return _build_config(
        field_dict={"Status": "Unanswered"},
        group_by=["Name"],
        function=frequency_count,
        col_name="Frequency",
        title="My Call Rejected by Other",
    )


func_dict = {
    "Total Incoming VS Outgoing": total_in_vs_out,
    "Total Duration of Calls with Each Person": person_wise_total_call,
    "Average Talk-Time with Each Person": avg_talktime,
    "Who gave me Most Missed Call": missed_call,
    "Call Rejected by Me": rejected_call_by_me,
    "My Call Rejected by Other": rejected_call_by_other,
}
