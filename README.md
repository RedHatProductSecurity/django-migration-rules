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

## How to use

Simply call `semgrep` with a link to the raw version of any of the yaml rule
definitions as a config:

```bash
$ semgrep -f 'https://raw.githubusercontent.com/RedHatProductSecurity/django-migration-rules/master/rules/django-migration-slow-default.yaml'
```

Semgrep allows chaining multiple configs, thus you can run multiple rules like so:

```bash
$ semgrep -f 'https://raw.githubusercontent.com/RedHatProductSecurity/django-migration-rules/master/rules/django-migration-slow-default.yaml' \
  -f 'https://raw.githubusercontent.com/RedHatProductSecurity/django-migration-rules/master/rules/django-migration-remove-field.yaml'
```

Alternatively, cloning the repository or having it as a submodule in your project also works:

```bash
$ semgrep -f ../django-migration-rules/rules
```
