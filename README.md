# Scuba Diving Club Management System

This project is a web-based management system for a Scuba Diving Club. It handles member registration, training sessions scheduling, equipment management, and tour planning.

## Features

- Member Management: Add, update, and remove club members.
- Training Sessions: Organize and schedule training sessions.
- Equipment Tracking: Keep an inventory of equipment and its status.
- Tour Management: Plan and schedule tours.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python installed on your system (Python 3.8+ recommended). You can download Python from [here](https://www.python.org/downloads/).

### Installing

First, clone the repository to your local machine:

```bash
git clone https://github.com/liw25/scuba_diving_club.git
```

Navigate to the project directory:

```bash
cd scuba_diving_club
```

Set up a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

On Windows:

```bash
venv\Scripts\activate
```

On Unix or MacOS:

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### Running the Application

To run the application, use the following command:

```bash
python -m flask run
```

The server should start, and you'll be able to access the application at `localhost:5000` in your web browser.

## Usage

Here's how to use the system:

1. Add a new member by navigating to `/add_member`.
2. Schedule a training session via `/schedule_training`.
3. Assign equipment to a tour with `/assign_equipment`.

Further usage instructions and routes can be found in the application's documentation.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/yourusername/scuba_diving_club/tags).

## Authors

 [liw25](https://github.com/liw25)

See also the list of [contributors](https://github.com/yourusername/scuba_diving_club/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc
```

