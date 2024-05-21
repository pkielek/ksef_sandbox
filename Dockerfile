# Use an official OpenJDK runtime as a parent image
FROM openjdk:11

# Install Maven
RUN apt-get update && apt-get install -y maven

# Set the working directory inside the container
WORKDIR /usr/src/myapp

# Copy the pom.xml file and the source code
COPY pom.xml .
COPY src ./src

# Run the Maven package command to build the project
RUN mvn clean package

# Run the application with the specified arguments
CMD ["java", "-jar", "target/java-ksef-sample-1.0.0-SNAPSHOT.jar", "1111111111", "2809A0A6818D0867AB2D429268782D45C9109F704318CD0F519F5C8759A8DAFE"]
