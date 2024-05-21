Little project based around [ksef4dev/sample-requests](https://github.com/ksef4dev/sample-requests) and [ksef4dev/ksef-java-sample](https://github.com/ksef4dev/ksef-java-sample) repositories, trying to implement basic requests to KSEF test environvment - initializing session, getting and uploading invoices
# Files contained:
- **src**: contains single .java file from [ksef4dev/ksef-java-sample](https://github.com/ksef4dev/ksef-java-sample), which is used along Dockerfile to encrypt token and get Auth challenge
- **pom.xml**: used by Dockerfile to configure project dependencies (based on [ksef4dev/ksef-java-sample](https://github.com/ksef4dev/ksef-java-sample))
- **Dockerfile**: used by run.py to run Java project from [ksef4dev/ksef-java-sample](https://github.com/ksef4dev/ksef-java-sample) to encrypt token and get Auth challenge
- **sampleFA2.xml**: example invoice, included in [ksef4dev/ksef-java-sample](https://github.com/ksef4dev/ksef-java-sample)
- **run.py**: runs requests to initialize session, get and upload invoices
