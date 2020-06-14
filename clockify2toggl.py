import csv
import datetime
import sys

with open(sys.argv[1]) as fp:
    assert fp.readline().strip() == '"Project","Client","Description","Task","User","Email","Tags","Billable","Start Date","Start Time","End Date","End Time","Duration (h)","Duration (decimal)","Billable  Rate (USD)","Billable Amount (USD)"'
    reader = csv.reader(fp)

    with open(sys.argv[2], 'w') if len(sys.argv) > 2 else sys.stdout as fp2:
        writer = csv.writer(fp2)

        writer.writerow([
            'Email',
            'Client',
            'Project',
            'Task',
            'Description',
            'Billable',
            'Start date',
            'Start time',
            'Duration',
            'Tags',
        ])

        for project, client, description, task, user, email, tags, billable, start_date, start_time, end_date, end_time, duration_h, duration_decimal, billable_rate_USD, billable_amount_USD in reader:
            start = datetime.datetime.strptime(
                start_date + ' ' + start_time,
                '%m/%d/%Y %I:%M:%S %p'
            )

            writer.writerow([
                email,
                client if client != '(Without client)' else '',
                project,
                task if task != '(Without task)' else '',
                description,
                billable,
                start.strftime('%Y-%m-%d'),
                start.strftime('%H:%M:%S'),
                duration_h,
                tags if tags != '(Without tags)' else '',
            ])
