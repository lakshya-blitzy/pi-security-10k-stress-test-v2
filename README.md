# PI Security ~10K Finding Test Corpus (v2)

**Purpose:** QA-only corpus for measuring Proactive Insights Security scan throughput and remediation grouping.

**Important:** This repository contains intentionally insecure *test fixtures*. Do not deploy, run, or expose these fixtures. The corpus contains 10,000 distinct candidate issue instances; it is **not guaranteed** to produce 10,000 scanner findings. Detection, deduplication, severity, and remediation grouping are determined by the scanner.

## Layout
- `security_fixtures/python/`: 1,000 files, each with 10 varied insecure-code patterns.
- `security_fixtures/config/`: representative insecure configuration samples.
- `security_fixtures/docker/`: intentionally weak container configuration.
- `security_fixtures/dependencies/`: dependency manifests for scanner analysis.
- `app/`: small harmless marker application used for a follow-up commit.
- `scripts/generate_corpus.py`: reproducibly regenerates the Python corpus.

## Suggested validation
1. Push this repository to a new GitHub repository.
2. Onboard the default branch in the staging environment.
3. Run the first Security scan and record: detected findings, remediation groups, advisories, and elapsed time.
4. If the result is below 10K, use the scan's actual detection ratio to scale the corpus; do not assume source instances equal findings.
5. After the first scan, make a harmless commit to `app/README_marker.txt`.
6. Trigger the next scan and verify completion, finding-to-remediation coverage, retention of existing groups, and elapsed time.

## Safety
These files are static scanner fixtures. They are not a functioning vulnerable service. Do not install the listed packages or deploy/run the fixtures.
