from datetime import timedelta
from typing import List

from django.db.models.functions import TruncDate
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Event(models.Model):

    unique_id = models.CharField(primary_key=True, max_length=127)
    datetime = models.DateTimeField(_('Время события хроники'))
    aircraft = models.CharField(max_length=127)

    class Meta:
        verbose_name = _('событие')
        verbose_name_plural = _('События')
        ordering = ('unique_id', )

    def __str__(self) -> str:
        return f'{self.aircraft}: {self.datetime}'


class Chronicle(models.Model):

    Open, Closed = 'Open', 'Closed'
    ChronicleStatuses = (
        (Open, Open),
        (Closed, Closed),
    )

    unique_id = models.CharField(primary_key=True, max_length=127)
    min_timestamp = models.DateTimeField(_('Время начала хроники'))
    max_timestamp = models.DateTimeField(_('Время окончания хроники'))
    status = models.CharField(_('Статус'), max_length=6, choices=ChronicleStatuses, default=Open)
    aircraft = models.CharField(max_length=127)

    class Meta:
        verbose_name = _('хроника')
        verbose_name_plural = _('Хроники')
        ordering = ('unique_id', )

    def __str__(self) -> str:
        return f'{self.min_timestamp} - {self.max_timestamp}'

    def n_days_of_chronicle(self, n: int = 20) -> List[int]:
        '''
        в какие из последних n дней хроники происходили события, а в какие нет
        :return: 1 если событие происходило, иначе 0
        '''
        # первый из n дней хроники
        n_days_before = self.max_timestamp - timedelta(days=n)
        n_days_before = n_days_before if n_days_before >= self.min_timestamp else self.min_timestamp

        # события которые происходили в последние n дней хроники
        events = Event.objects.filter(datetime__range=(n_days_before, self.max_timestamp)) \
                              .annotate(date=TruncDate('datetime')) \
                              .values_list('date', flat=True)
        days = []
        current_date = n_days_before.date()

        # проверяем каждый день, последних n дней хроники
        while current_date <= self.max_timestamp.date():
            days.append(1 if current_date in events else 0)
            current_date += timedelta(days=1)
        return days


