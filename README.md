# GroupMe Media Downloader

A Python script that downloads all images and videos from a specified GroupMe group using the GroupMe API. The project also includes shell scripts necessary to correctly parse the API output.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Download Media](#download-media)
  - [Clear Media](#clear-media)
  - [Revise Media](#revise-media)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Getting Started

These instructions will help you set up a local copy of the project and get it up and running.

### Prerequisites

- Python 3.6 or higher
- GroupMe API access token

### Installation

1. Clone the repo:

`git clone https://github.com/your_username/groupme-media-downloader.git`


2. Install the required dependencies:

`pip install requests`


## Usage

### Download Media

To download all images and videos from a specified GroupMe group, follow these steps:

1. Set the `GROUPME_ACCESS_TOKEN` environment variable to your GroupMe API access token. You can do this in your terminal or add it to your `.bashrc`, `.zshrc`, or `.env` file.

`export GROUPME_ACCESS_TOKEN=your_access_token_here`

2. Open the `main.py` script and replace `your_group_id_here` with your GroupMe group ID:


`GROUP_ID = 'your_group_id_here'`

3. Run the 'main.py' script

`python main.py`

All downloaded media files will be saved in the media folder.

4. Run the 'revisemedia.sh' script

```
chmod +x revosemedia.sh
./revisemedia.sh
```


### Clear Media

To delete all files in the media folder, run the clearmedia.sh script:

```
chmod +x clearmedia.sh
./clearmedia.sh
```

## Contributing

If you would like to contribute to the project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b your-feature-branch`)
3. Commit your changes (`git commit -am 'Add a new feature'`)
4. Push to the branch (`git push origin your-feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Thanks to the [GroupMe API](https://dev.groupme.com/docs/v3) for providing the necessary API endpoints to access group messages and media.

