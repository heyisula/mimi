<div align="center">

  <img src="assets/banner.png?raw=true" alt="Mimi Project Banner" width="100%" />

  <br />
  <br />

  <h1>🐱 Mimi</h1>

  <p><strong>A gentle, AI-powered companion living on your home screen, brought to life in loving memory of a little friend.</strong></p>

  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License: Apache 2.0" /></a>
    <img src="https://img.shields.io/badge/Platform-iOS%20%7C%20Android-lightgrey.svg" alt="Platform: iOS | Android" />
    <img src="https://img.shields.io/badge/Flutter-%2302569B.svg?logo=flutter&logoColor=white" alt="Flutter" />
    <img src="https://img.shields.io/badge/Dart-%230175C2.svg?logo=dart&logoColor=white" alt="Dart" />
    <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB.svg?logo=python&logoColor=white" alt="Python 3.10+" />
    <img src="https://img.shields.io/badge/FastAPI-%23009688.svg?logo=fastapi&logoColor=white" alt="FastAPI" />
    <img src="https://img.shields.io/badge/Build-passing-brightgreen.svg" alt="Build Status" />
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome" />
    <img src="https://img.shields.io/badge/Made%20with-♥%20and%20paws-ff69b4.svg" alt="Made with love and paws" />
  </p>

</div>

---

## 📑 Table of Contents

- [About](#-about)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgements / In Loving Memory](#-acknowledgements--in-loving-memory)

---

<a id="about"></a>
## 🐾 About

**Mimi** is a cross-platform mobile application for iOS and Android built as a heartfelt tribute to a beloved kitten named Mimi who has passed away. 

While Mimi is no longer here with us, this project gently brings her spirit back as an AI-powered companion that stays close throughout your day. Residing directly on your home screen as an interactive widget, Mimi acts as a warm, comforting, and playful personal assistant, offering quiet companionship, affectionate check-ins, and lighthearted moments right when you need them most.

---

<a id="tech-stack"></a>
## 🛠️ Tech Stack

| Layer | Technologies | Purpose |
| :--- | :--- | :--- |
| **Mobile Client** | `Flutter`, `Dart` | Cross-platform mobile application (iOS & Android) and home screen widgets |
| **Backend Service** | `Python`, `FastAPI` | Asynchronous API server handling companion logic and assistant interactions |
| **AI / Intelligence** | <!-- TODO: Model Provider / Framework --> | Powers Mimi's warm and responsive conversational abilities |
| **Storage / Cache** | <!-- TODO: Database / Cache solution --> | Manages conversation memory and user preferences |

---

<a id="getting-started"></a>
## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed on your development machine:

- [Flutter SDK](https://docs.flutter.dev/get-started/install) (`^3.x`)
- [Dart SDK](https://dart.dev/get-dart)
- [Python](https://www.python.org/downloads/) (`3.10+`)
- iOS (Xcode) and/or Android (Android Studio) build toolchains

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/heyisula/mimi.git
   cd mimi
   ```

2. **Configure environment variables:**
   ```bash
   # Copy sample environment configuration for the backend
   cp server/.env.example server/.env
   # <!-- TODO: Fill in required API keys and settings in server/.env -->
   ```

3. **Install backend dependencies:**
   ```bash
   cd server
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   cd ..
   ```

4. **Install mobile dependencies:**
   ```bash
   cd client
   flutter pub get
   cd ..
   ```

### Running Locally

- **Start the backend server:**
  ```bash
  cd server
  uvicorn app.main:app --reload --port 8000
  ```

- **Run the mobile app:**
  ```bash
  cd client
  flutter run
  ```

---

<a id="project-structure"></a>
## 📁 Project Structure

```text
mimi/
├── assets/                 # App logos, banners, and static media
│   └── banner.png          # <!-- TODO: Add project banner -->
├── client/                 # Flutter mobile application (iOS & Android)
│   ├── android/            # Android platform configuration & widget host
│   ├── ios/                # iOS platform configuration & WidgetKit extension
│   └── lib/                # Flutter source code & UI components
├── server/                 # FastAPI backend service
│   ├── app/                # Application modules & AI assistant endpoints
│   ├── requirements.txt    # Python dependencies
│   └── .env.example        # Environment variable template
├── .gitignore
├── LICENSE
└── README.md
```

---

<a id="roadmap"></a>
## 🗺️ Roadmap

- [ ] Complete core home screen widget integration for iOS (WidgetKit) and Android (Glance / AppWidget)
- [ ] Connect FastAPI backend with conversational memory for Mimi
- [ ] Implement gentle reminder and cheerful daily check-in routines
- [ ] Add customizable appearance and widget styles

---

<a id="contributing"></a>
## 🤝 Contributing

Contributions, ideas, and suggestions are warmly welcomed!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- TODO: Add link to CONTRIBUTING.md or Code of Conduct if applicable -->

---

<a id="license"></a>
## 📄 License

Distributed under the Apache 2.0 License. See [`LICENSE`](LICENSE) for more information.

<!-- TODO: Verify license details and attribution -->

---

<a id="acknowledgements--in-loving-memory"></a>
## 🤍 Acknowledgements / In Loving Memory

> *"No amount of time can erase the memory of a good cat, and no amount of masking tape can ever totally remove his fur from your couch."*  
> - Leo Dworken

This project exists because of **Mimi**, a tiny kitten whose gentle presence, quiet purrs, and playful spirit brought endless warmth. 

Although she left us far too early, her memory continues to inspire this space of gentle companionship, care, and comfort. You will always be deeply loved, sweet Mimi. 🐾

<div align="center">
  <sub>Made with gentle care and endless love for Mimi 🐾</sub>
</div>
