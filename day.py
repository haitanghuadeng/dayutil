# -*- coding:utf-8 -*-


from datetime import datetime, timedelta


class DayPy:
    def __init__(self, date=None):
        if not date:
            self.date = datetime.now()
        elif len(date) == 4:
            self.date = datetime.strptime(date, "%Y")
        elif len(date) == 7:
            self.date = datetime.strptime(date, "%Y-%m")
        elif len(date) == 10:
            self.date = datetime.strptime(date, "%Y-%m-%d")
        elif len(date) == 13:
            self.date = datetime.strptime(date, "%Y-%m-%d %H")
        elif len(date) == 16:
            self.date = datetime.strptime(date, "%Y-%m-%d %H:%M")
        else:
            self.date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

    def subtract(self, amount, unit):
        """
        subtract(amount, unit)方法与add()方法类似，但它是将指定的时间量（amount）从当前日期中减去。
        """

        if unit == "year":
            self.date -= timedelta(days=amount * 365)
        elif unit == "month":
            self.date -= timedelta(days=amount * 30)
        elif unit == "week":
            self.date -= timedelta(weeks=amount)
        elif unit == "day":
            self.date -= timedelta(days=amount)
        elif unit == "hour":
            self.date -= timedelta(hours=amount)
        elif unit == "minute":
            self.date -= timedelta(minutes=amount)
        elif unit == "second":
            self.date -= timedelta(seconds=amount)

        # 添加更多的判断条件来处理其他单位
        return self

    def add(self, amount, unit):
        """
        add(amount, unit)方法用于将指定的时间量（amount）添加到当前日期。
        单位（unit）可以是"year"、"month"、"week"、"day"、"hour"、"minute"或"second"。
        根据单位的不同，我们使用timedelta类在当前日期上增加相应的时间量。
        """

        if unit == "year":
            self.date = self.date.replace(year=self.date.year + amount)
        elif unit == "month":
            new_month = self.date.month + amount
            year_offset = (new_month - 1) // 12
            new_year = self.date.year + year_offset
            new_month = (new_month - 1) % 12 + 1
            self.date = self.date.replace(year=new_year, month=new_month)
        elif unit == "week":
            self.date += timedelta(weeks=amount)
        elif unit == "day":
            self.date += timedelta(days=amount)
        elif unit == "hour":
            self.date += timedelta(hours=amount)
        elif unit == "minute":
            self.date += timedelta(minutes=amount)
        elif unit == "second":
            self.date += timedelta(seconds=amount)

        # 添加更多的判断条件来处理其他单位
        return self

    def toFormat(self, fmt="%Y-%m-%d %H:%M:%S"):
        """
        toFormat()用于传入所需的日期格式进行格式化输出。
        """
        return self.date.strftime(fmt)

    def startOfDay(self):
        """
        startOfDay()方法来获取给定日期的当天开始时间。
        """

        start_of_day = datetime(year=self.date.year, month=self.date.month, day=self.date.day, hour=0, minute=0,
                                second=0)
        return start_of_day

    def endOfDay(self):
        """
        endOfDay()方法返回给定日期的当天结束时间（23:59:59）。
        """
        end_of_day = datetime(year=self.date.year, month=self.date.month, day=self.date.day, hour=23, minute=59,
                              second=59)
        return end_of_day

    def isBefore(self, other_date):
        """
        isBefore()方法用于比较两个日期，判断当前日期是否在另一个日期之前。
        """
        return self.date < other_date.date

    def isAfter(self, other_date):
        """
        isAfter()方法用于比较两个日期，判断当前日期是否在另一个日期之后。
        """
        return self.date > other_date.date

    def isSameOrBefore(self, other_date):
        """
        isSameOrBefore()方法用于比较两个日期，判断当前日期是否与另一个日期相同或在其之前。
        """
        return self.date <= other_date.date

    def isSameOrAfter(self, other_date):
        """
        isSameOrAfter()方法用于比较两个日期，判断当前日期是否与另一个日期相同或在其之后。
        """
        return self.date >= other_date.date

    def diff(self, other_date, unit: str = "second"):
        """
        diff()方法用于计算两个日期之间的差异，并返回指定单位下的差异值（年、月、日等）。
        """
        delta = self.date - other_date.date

        if unit == "year":
            return abs(delta.days // 365)
        elif unit == "month":
            return abs(delta.days // 30)
        elif unit == "day":
            return abs(delta.days)
        elif unit == "hour":
            return abs(delta.seconds // 60 // 60)
        elif unit == "minute":
            return abs(delta.seconds // 60)
        else:
            return abs(delta.seconds)

    def toArray(self):
        """
        toArray()方法将日期转换为包含年、月、日、小时、分钟和秒的列表形式。
        """
        return [self.date.year, self.date.month, self.date.day, self.date.hour, self.date.minute, self.date.second]

    def toDate(self):
        """
        toDate()方法返回原始的Python日期对象。
        """
        return self.date

    def isLeapYear(self):
        """
        isLeapYear()方法用于判断给定日期所属年份是否是闰年。
        """
        year = self.date.year
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True

    def isBetween(self, start_date, end_date):
        """
        isBetween()方法用于判断给定日期是否处于指定的起始日期和结束日期之间。
        """
        return start_date.date <= self.date <= end_date.date

    def isSame(self, other_date):
        """
        isSame()方法用于比较两个日期，判断它们是否相同。
        """
        return self.date == other_date.date

    def clone(self):
        """
        clone()方法用于克隆当前日期对象，返回一个新的DayJS对象。
        """
        return self.date

    def isToday(self):
        """
        isToday()方法用于判断给定日期是否是今天。
        """
        today = datetime.now().date()
        return self.date.date() == today

    def isYesterday(self):
        """
        isYesterday()方法用于判断给定日期是否是昨天。
        """
        yesterday = datetime.now().date() - timedelta(days=1)
        return self.date.date() == yesterday

    def isTomorrow(self):
        """
        isTomorrow()方法用于判断给定日期是否是明天。
        """
        tomorrow = datetime.now().date() + timedelta(days=1)
        return self.date.date() == tomorrow

    def isThisYear(self):
        """
        isThisYear()方法用于判断给定日期是否是今年。
        """
        this_year = datetime.now().date().year
        return self.date.year == this_year

    def isNextYear(self):
        """
        isNextYear()方法用于判断给定日期是否是明年。
        """
        next_year = datetime.now().date().year + 1
        return self.date.year == next_year

    def isLastYear(self):
        """
        isLastYear()方法用于判断给定日期是否是去年。
        """
        last_year = datetime.now().date().year - 1
        return self.date.year == last_year

    def isSunday(self):
        """
        isSunday()方法用于判断给定日期是否是星期日。
        """
        return self.date.weekday() == 6

    def isMonday(self):
        """
        isMonday()方法用于判断给定日期是否是星期一。
        """
        return self.date.weekday() == 0

    def isTuesday(self):
        """
        isTuesday()方法用于判断给定日期是否是星期二。
        """
        return self.date.weekday() == 1

    def isWednesday(self):
        """
        isWednesday()方法用于判断给定日期是否是星期三。
        """
        return self.date.weekday() == 2

    def isThursday(self):
        """
        isThursday()方法用于判断给定日期是否是星期四。
        """
        return self.date.weekday() == 3

    def isFriday(self):
        """
        isFriday()方法用于判断给定日期是否是星期五。
        """
        return self.date.weekday() == 4

    def isSaturday(self):
        """
        isSaturday()方法用于判断给定日期是否是星期六。
        """
        return self.date.weekday() == 5

    def daysInMonth(self):
        """
        daysInMonth()方法用于获取给定日期所在月份的天数。
        """
        year = self.date.year
        month = self.date.month
        if month == 12:
            next_year = year + 1
            next_month = 1
        else:
            next_year = year
            next_month = month + 1
        last_day_of_month = (datetime(next_year, next_month, 1) - timedelta(days=1)).day
        return last_day_of_month

    def formatRelative(self, base_date):
        """
        formatRelative()方法用于根据给定基准日期，返回当前日期相对于基准日期的相对格式化字符串。例如，如果当前日期是基准日期的前一天，则返回"昨天"；如果当前日期是基准日期的后两天，则返回"2 天后"。
        """
        delta = self.date - base_date.date
        if delta.days == 0:
            return "今天"
        elif delta.days == 1:
            return "明天"
        elif delta.days == -1:
            return "昨天"
        elif delta.days > 1:
            return f"{delta.days} 天后"
        elif delta.days < -1:
            return f"{abs(delta.days)} 天前"
        else:
            return "Invalid"

    def fromNow(self, include_suffix=False):
        """
        返回现在到当前实例的相对时间。
        """
        now = datetime.now()
        diff = now - self.date

        years = abs(diff.days) // 365
        months = abs(diff.days) // 30
        weeks = abs(diff.days) // 7
        days = abs(diff.days)
        hours = abs(diff.seconds) // 3600
        minutes = (abs(diff.seconds) // 60) % 60

        if years > 0:
            time_ago = f"{years}年"
        elif months > 0:
            time_ago = f"{months}个月"
        elif weeks > 0:
            time_ago = f"{weeks}周"
        elif days > 0:
            time_ago = f"{days}天"
        elif hours > 0:
            time_ago = f"{hours}小时"
        elif minutes > 0:
            time_ago = f"{minutes}分钟"
        elif diff.seconds > 0:
            time_ago = f"{diff.seconds}秒钟"
        else:
            return "刚刚"

        if include_suffix:
            return time_ago

        return time_ago + "前"

    def toNow(self, include_suffix=False):
        """
        返回当前实例到现在的相对时间。
        """
        now = datetime.now()
        diff = now - self.date

        years = abs(diff.days) // 365
        months = abs(diff.days) // 30
        weeks = abs(diff.days) // 7
        days = abs(diff.days)
        hours = abs(diff.seconds) // 3600
        minutes = (abs(diff.seconds) // 60) % 60

        if years > 0:
            time_ago = f"{years}年"
        elif months > 0:
            time_ago = f"{months}个月"
        elif weeks > 0:
            time_ago = f"{weeks}周"
        elif days > 0:
            time_ago = f"{days}天"
        elif hours > 0:
            time_ago = f"{hours}小时"
        elif minutes > 0:
            time_ago = f"{minutes}分钟"
        elif diff.seconds > 0:
            time_ago = f"{diff.seconds}秒钟"
        else:
            return "刚刚"

        if include_suffix:
            return time_ago

        return time_ago + "后"

    def formerly(self, target_date: str = ..., include_suffix=False):
        if isinstance(target_date, str):
            target_date = datetime.strptime(target_date, "%Y-%m-%d")

        diff = target_date - self.date

        years = abs(diff.days) // 365
        months = abs(diff.days) // 30
        weeks = abs(diff.days) // 7
        days = abs(diff.days)
        hours = abs(diff.seconds) // 3600
        minutes = (abs(diff.seconds) // 60) % 60

        if years > 0:
            time_ago = f"{years}年"
        elif months > 0:
            time_ago = f"{months}个月"
        elif weeks > 0:
            time_ago = f"{weeks}周"
        elif days > 0:
            time_ago = f"{days}天"
        elif hours > 0:
            time_ago = f"{hours}小时"
        elif minutes > 0:
            time_ago = f"{minutes}分钟"
        else:
            return "刚刚"

        if include_suffix:
            return time_ago

        return time_ago + "前"

    def to(self, target_date: str = ..., include_suffix=False):
        if isinstance(target_date, str):
            target_date = datetime.strptime(target_date, "%Y-%m-%d")

        diff = target_date - self.date

        years = abs(diff.days) // 365
        months = abs(diff.days) // 30
        weeks = abs(diff.days) // 7
        days = abs(diff.days)
        hours = abs(diff.seconds) // 3600
        minutes = (abs(diff.seconds) // 60) % 60

        if years > 0:
            time_ago = f"{years}年"
        elif months > 0:
            time_ago = f"{months}个月"
        elif weeks > 0:
            time_ago = f"{weeks}周"
        elif days > 0:
            time_ago = f"{days}天"
        elif hours > 0:
            time_ago = f"{hours}小时"
        elif minutes > 0:
            time_ago = f"{minutes}分钟"
        else:
            return "刚刚"

        if include_suffix:
            return time_ago

        return time_ago + "后"

    def yearsDiff(self, compare_date):
        """
        yearsDiff()方法用于计算给定日期与另一个日期之间的年份差异。
        """
        return self.date.year - compare_date.year

    def monthsDiff(self, compare_date):
        """
        monthsDiff()方法用于计算给定日期与另一个日期之间的月份差异。
        """
        return (self.date.year - compare_date.year) * 12 + self.date.month - compare_date.month

    def weeksDiff(self, compare_date):
        """
        weeksDiff()方法用于计算给定日期与另一个日期之间的周数差异。
        """
        delta = (self.date - compare_date).days
        return delta // 7

    def daysDiff(self, compare_date):
        """
        daysDiff()方法用于计算给定日期与另一个日期之间的天数差异。
        """
        delta = self.date - compare_date
        return delta.days

    def hoursDiff(self, compare_date):
        """
        hoursDiff()方法用于计算给定日期与另一个日期之间的小时数差异。
        """
        delta = self.date - compare_date
        return delta.total_seconds() // 3600

    def toUnix(self, ms=False):
        """
        toUnix()方法用于将当前日期转换为Unix时间戳。
        ms: 毫秒，单位是否为毫秒
        """
        unix_timestamp = int(self.date.timestamp() * 1000 if ms else self.date.timestamp())

        return unix_timestamp

    def startOf(self, unit):
        """
        startOf()方法用于获取当前日期所属单位开始的日期时间。它接受一个单位参数，可以是"year"、"month"、"week"、"day"、"hour"、"minute"或"second"。
        """
        if unit == "year":
            return datetime(self.date.year, 1, 1)
        elif unit == "month":
            return datetime(self.date.year, self.date.month, 1)
        elif unit == "week":
            start_of_week = self.date - timedelta(days=self.date.weekday())
            return datetime(start_of_week.year, start_of_week.month, start_of_week.day)
        elif unit == "day":
            return datetime(self.date.year, self.date.month, self.date.day)
        elif unit == "hour":
            return datetime(self.date.year, self.date.month, self.date.day, self.date.hour)
        elif unit == "minute":
            return datetime(self.date.year, self.date.month, self.date.day, self.date.hour, self.date.minute)
        elif unit == "second":
            return datetime(self.date.year, self.date.month, self.date.day, self.date.hour, self.date.minute,
                            self.date.second)
        else:
            raise ValueError("Invalid unit")

    def endOf(self, unit):
        """
        endOf()方法用于获取当前日期所属单位结束的日期时间。它也接受一个单位参数，与`startOf()`方法相同。
        """
        if unit == "year":
            return datetime(self.date.year, 12, 31, 23, 59, 59)
        elif unit == "month":
            next_month = self.date.month + 1 if self.date.month < 12 else 1
            next_year = self.date.year + 1 if self.date.month == 12 else self.date.year
            last_day_of_month = (datetime(next_year, next_month, 1) - timedelta(days=1)).day
            return datetime(self.date.year, self.date.month, last_day_of_month, 23, 59, 59)
        elif unit == "week":
            end_of_week = self.date + timedelta(days=6 - self.date.weekday())
            return datetime(end_of_week.year, end_of_week.month, end_of_week.day, 23, 59, 59)
        elif unit == "day":
            return datetime(self.date.year, self.date.month, self.date.day, 23, 59, 59)
        elif unit == "hour":
            return datetime(self.date.year, self.date.month, self.date.day, self.date.hour, 59, 59)
        elif unit == "minute":
            return datetime(self.date.year, self.date.month, self.date.day, self.date.hour, self.date.minute, 59)
        elif unit == "second":
            return datetime(self.date.year, self.date.month, self.date.day, self.date.hour, self.date.minute,
                            self.date.second)
        else:
            raise ValueError("Invalid unit")

    def isValid(self):
        """
        isValid()方法用于检查当前日期是否有效。它使用strptime函数将日期格式化成字符串，并在此基础上解析为datetime对象，如果解析成功则说明日期有效，返回True；否则，说明日期无效，返回False。
        """
        try:
            datetime.strptime(self.date.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
            return True
        except ValueError:
            return False

    def utc(self):
        """
        utc()方法用于将当前日期转换为UTC时间。它通过使用utcnow()函数获取当前的UTC时间，并返回一个新的DayJS对象，该对象包含了转换后的UTC时间。
        """
        utc_date = self.date.utcnow()
        return utc_date

    def local(self):
        """
        local()方法用于将当前日期转换为本地时间。它通过使用replace()函数将当前日期的时区信息移除，并返回一个新的DayJS对象，该对象包含了转换后的本地时间。
        """
        local_date = self.date.replace(tzinfo=None)
        return local_date

    def utcOffset(self, offset):
        """
        utcOffset(offset)方法用于将当前日期偏移指定的分钟数。它通过使用timedelta()函数创建一个时间差对象，并将其加到当前日期上，从而实现时区偏移。返回一个新的DayJS对象，该对象包含了偏移后的日期时间。
        """
        delta = timedelta(minutes=offset)
        offset_date = self.date + delta
        return offset_date

    def calendar(self):
        """
        calendar()方法用于将当前日期与给定日期进行比较，并返回相应的日历格式。它可以计算当前日期与给定日期之间的差值，并根据差值返回适当的日历格式。如果给定日期是未来的日期，则返回"未来"；如果给定日期是今天，根据时间差显示"刚刚"、"x分钟前"或"x小时前"；如果给定日期是本周内的日期，则返回星期几和具体时间，否则返回日期和具体时间。
        """
        now = datetime.now()
        diff = now - self.date
        seconds = diff.seconds
        minutes = seconds // 60
        hours = minutes // 60
        days = diff.days

        if days < 0:
            return "未来"
        elif days == 0:
            if hours < 1:
                if minutes < 1:
                    return "刚刚"
                else:
                    return "{}分钟前".format(minutes)
            else:
                return "{}小时前".format(hours)
        elif days < 7:
            if now.weekday() - self.date.weekday() < 7:
                return self.date.strftime("%A %H:%M")
            else:
                return self.date.strftime("%m月%d日 %H:%M")
        else:
            return self.date.strftime("%Y年%m月%d日 %H:%M")

    def isoWeeksInYear(self):
        """
        isoWeeksInYear()方法。该方法用于计算给定日期所在年份的ISO周数。
        """
        year = self.date.year
        last_day = datetime(year, 12, 31)
        last_week = last_day.isocalendar()[1]
        if last_day.weekday() == 6:
            return last_week
        return last_week + 1

    def get(self, unit):
        """
        get()方法获取年份、月份、日期、小时、分钟、秒数、毫秒数、星期几和ISO周数。
        """
        if unit == "year":
            return self.date.year
        elif unit == "month":
            return self.date.month
        elif unit == "date" or unit == "day":
            return self.date.day
        elif unit == "hour":
            return self.date.hour
        elif unit == "minute":
            return self.date.minute
        elif unit == "second":
            return self.date.second
        elif unit == "millisecond":
            return int(self.date.microsecond / 1000)
        elif unit == "weekday":
            return self.date.weekday()
        elif unit == "isoWeek":
            return self.date.isocalendar()[1]
        else:
            raise ValueError("Invalid unit")

    def year(self):
        """
        获取年份
        """
        return self.date.year

    def setYear(self, year):
        """
        设置年份
        """
        self.date = self.date.replace(year=year)

    def month(self):
        """
        获取月份
        """
        return self.date.month

    def setMonth(self, month):
        """
        设置月份
        """
        self.date = self.date.replace(month=month)

    def date(self):
        """
        获取日期/天数
        """
        return self.date.day

    def setDate(self, day):
        """
        设置日期/天数
        """
        self.date = self.date.replace(day=day)

    def hour(self):
        """
        获取小时
        """
        return self.date.hour

    def setHour(self, hour):
        """
        设置小时
        """
        self.date = self.date.replace(hour=hour)

    def minute(self):
        """
        获取分钟
        """
        return self.date.minute

    def setMinute(self, minute):
        """
        设置分钟
        """
        self.date = self.date.replace(minute=minute)

    def second(self):
        """
        获取秒数
        """
        return self.date.second

    def setSecond(self, second):
        """
        设置秒数
        """
        self.date = self.date.replace(second=second)

    def millisecond(self):
        """
        获取毫秒数
        """
        return int(self.date.microsecond / 1000)

    def setMillisecond(self, millisecond):
        """
        设置毫秒数
        """
        microseconds = millisecond * 1000
        self.date = self.date.replace(microsecond=microseconds)

    def day(self):
        """
        获取星期几 (0为星期一，6为星期日)
        """
        return self.date.weekday()

    def isoWeek(self):
        """
        获取ISO周数
        """
        return self.date.isocalendar()[1]

    def getWeekDates(self, week_num):
        """
        getWeekDates()方法并传递指定周数作为参数，然后打印返回结果。您将会得到包含该周所有七天日期的列表。
        如果未传递周数，则默认使用self.date所在的周数。
        """
        start_date = datetime.strptime(f'{self.date.year}-W{week_num}-1', "%Y-W%W-%w")
        week_dates = [start_date + timedelta(days=i) for i in range(7)]

        return [date.strftime("%Y-%m-%d") for date in week_dates]

    def getMonthDates(self):
        """
        getMonthDates()会根据当前日期确定所在的月份，并依次增加天数直至下个月开始的一天，期间所有日期都被存储在列表dates中并返回。
        """
        dates = []
        current_month = self.date.month
        next_month = current_month + 1 if current_month < 12 else 1
        next_year = self.date.year if next_month > current_month else self.date.year + 1

        while self.date.month != next_month or self.date.year != next_year:
            dates.append(self.date.strftime("%Y-%m-%d"))
            self.date += timedelta(days=1)

        return dates

    def generateMonthList(self, end_date):
        """
        generateMonthList()会根据当前日期确定所在的月份，并依次增加月数直至指定月，期间所有日期都被存储在列表month_list中并返回。
        """
        month_list = []

        while self.date <= end_date.date:
            month_list.append(self.date.strftime("%Y-%m"))
            self.add(1, "month")

        return month_list


if __name__ == "__main__":
    # 示例用法
    # print(DayPy().add(7, "day").toFormat("%Y-%m-%d"))
    # print(DayPy("2022-01-01").to(target_date="2024-01-01"))
    # print(DayPy("2023").getWeekDates(31))
    # print(DayPy("2023-01-01 12:56:20").diff(DayPy("2023-01-01 08:16:14"), "minute"))
    print(DayPy("2023-01-01 12:56:20").toUnix(ms=True), 1635329130.3962116)
    # print(DayPy("2022-01").generateMonthList("2023-12"))
