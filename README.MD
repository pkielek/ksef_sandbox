Little project based around [ksef4dev/sample-requests](https://github.com/ksef4dev/sample-requests) repository, trying to implement basic requests to KSEF test environvment - initializing session, getting and uploading invoices
# Files contained:
- **src**: contains single .java file from [ksef4dev/sample-requests](https://github.com/ksef4dev/sample-requests), which is used along Dockerfile to encrypt token and get Auth challenge
- **pom.xml**: used by Dockerfile to configure project dependencies (based on [ksef4dev/sample-requests](https://github.com/ksef4dev/sample-requests))
- **Dockerfile**: used by run.py to run Java project from [ksef4dev/sample-requests](https://github.com/ksef4dev/sample-requests) to encrypt token and get Auth challenge
- **sampleFA2.xml**: example invoice, included in [ksef4dev/sample-requests](https://github.com/ksef4dev/sample-requests)
- **run.py**: runs requests to initialize session, get and upload invoices
