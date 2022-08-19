# Semgrep rules for safe and performant Django migrations

This repository contains a collection of semgrep rules with the goal of
enabling zero-downtime (or close to zero :-)) Django migrations.

It does so by checking for common patterns that can result in slow or
backwards-incompatible migrations in production, such as:

* NOT NULL fields being added to an existing table without an explicit
  SQL default.

* Removal of fields.

* Renaming of fields.

* Dropping models.

...
