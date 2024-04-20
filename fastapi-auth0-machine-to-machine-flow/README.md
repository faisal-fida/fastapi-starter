# Auth0 Machine-to-Machine (M2M) Flow

## Introduction

Auth0 provides authentication and authorization services for applications. The machine-to-machine (M2M) flow is specifically designed for secure communication between machines, such as servers, APIs, or services, without human intervention. This flow is based on the use of Custom Database.

## Flow

- Create a Machine to Machine application in Auth0 Dashboard.
For more information, visit [Auth0 Documentation](https://auth0.com/docs/get-started/auth0-overview/create-applications/machine-to-machine-apps).

- After creating the application, you will get a Client Id and Client Secret. Along with your Auth0 Domain, you need to set these values in .env file.

## Features

- Sign Up
    - Create a user in your custom database via Auth0 database action scripts and Auth0 python SDK.
- Login
    - Login by email and password and get a auth token along with a id token.
