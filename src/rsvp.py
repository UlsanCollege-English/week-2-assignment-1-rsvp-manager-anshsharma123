# src/rsvp.py
from collections import Counter
from typing import List, Tuple, Optional


def dedupe_emails_case_preserve_order(emails: List[str]) -> List[str]:
    """Remove duplicate emails, case-insensitive, preserving first occurrence order."""
    seen = set()
    result = []
    for email in emails:
        if "@" not in email:
            continue  # skip invalid entries
        key = email.lower()
        if key not in seen:
            seen.add(key)
            result.append(email)
    return result


def first_with_domain(emails: List[str], domain: str) -> Optional[int]:
    """Return the index of the first email with given domain (case-insensitive)."""
    domain = domain.lower()
    for i, email in enumerate(emails):
        if "@" in email:
            _, d = email.split("@", 1)
            if d.lower() == domain:
                return i
    return None


def domain_counts(emails: List[str]) -> List[Tuple[str, int]]:
    """Return list of (domain, count), sorted by domain name, ignoring invalid emails."""
    domains = []
    for email in emails:
        if "@" in email:
            _, d = email.split("@", 1)
            domains.append(d.lower())
    counter = Counter(domains)
    return sorted(counter.items())
