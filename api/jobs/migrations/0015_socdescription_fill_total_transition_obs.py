# Generated by Django 3.1 on 2021-01-31 22:14

from django.db import migrations, models


class Migration(migrations.Migration):
        """
        Populate the total_transition_obs field in jobs_occupationtransitions table. jobs_socdescription and
        occupation_transition are populated by an earlier migration as part of the Python ingestion code

        According to Schubert, Stansbury, and Taska (2020), the total_obs field need not be an integer since it can be
        reweighted by age.

            UPDATE jobs_occupationtransitions AS jobs
            SET total_transition_obs = original.total_obs
            FROM occupation_transition AS original
            WHERE original.soc1 = jobs.soc1
                AND original.soc2 = jobs.soc2;

            UPDATE jobs_socdescription AS jobs
            SET total_transition_obs = original.total_obs
            FROM (SELECT DISTINCT soc1, total_obs
                  FROM occupation_transition) AS original
            WHERE original.soc1 = jobs.soc_code;
        """
        dependencies = [
            ('jobs', '0014_socdescription_total_transition_obs'),
        ]

        operations = [
            migrations.RunSQL([
                ("UPDATE jobs_occupationtransitions AS jobs "
                 "SET total_transition_obs = original.total_obs "
                 "FROM occupation_transition AS original "
                 "WHERE original.soc1 = jobs.soc1 "
                 "  AND original.soc2 = jobs.soc2;"),
            ],
            ["UPDATE jobs_occupationtransitions SET total_transition_obs = NULL;"]),
            migrations.RunSQL([
                ("UPDATE jobs_socdescription AS jobs "
                 "SET total_transition_obs = original.total_obs "
                 "FROM (SELECT DISTINCT soc1, total_obs "
                    "FROM occupation_transition) AS original "
                 "WHERE original.soc1 = jobs.soc_code;"),
            ],
            ["UPDATE jobs_occupationtransitions SET total_transition_obs = NULL;"])
        ]