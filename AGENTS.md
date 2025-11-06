# Repository Guidelines

This guide summarizes how to contribute safely and efficiently to the MyFurdi Flutter workspace. Refer to existing setup docs (such as `FLUTTER_SETUP_GUIDE.md`) for environment details.

## Project Structure & Module Organization
- Core Flutter app lives in `myfurdi_flutter_app/`.
- UI code is split under `lib/` (`screens/`, reusable `widgets/`, shared `theme/`, and domain `models/`).
- Automated tests reside in `test/`; integration or golden tests should mirror the `lib/` hierarchy.
- Android, iOS, web, and desktop platform shells remain under their respective folders; keep platform-specific changes isolated.

## Build, Test & Development Commands
- `flutter pub get` — refresh dependencies after modifying `pubspec.yaml`.
- `flutter run -d <device>` — launch the app against an attached emulator or device.
- `flutter test` — execute unit and widget tests; ensure this passes before opening a PR.
- `flutter analyze` — run static analysis powered by the configured Flutter lints.
- For release artifacts, coordinate with the maintainer before running `flutter build apk` or other platform builds.

## Coding Style & Naming Conventions
- Dart files use two-space indentation and the `flutter_lints` ruleset defined in `analysis_options.yaml`.
- Format code with `dart format .` (or `flutter format`) prior to commit.
- Name files and directories in `snake_case.dart`; classes and enums in `UpperCamelCase`; variables and functions in `lowerCamelCase`.
- Keep widgets small and composable; co-locate supporting models or themes with the screen they serve when practical.

## Testing Guidelines
- Add or update tests in `test/` to cover new behaviors; pair each new screen with at least a widget test that exercises navigation and critical UI states.
- Aim to exercise error paths and asynchronous flows; prefer fakes over live services.
- When adding golden tests, store images under a subfolder that mirrors the widget path and document updates in the PR.

## Commit & Pull Request Guidelines
- Follow the existing history: short, imperative commit titles (e.g., `Add DNA service selector`), optional body for rationale and follow-up tasks.
- Group related changes per commit; avoid mixing refactors with feature work.
- Pull requests must include: a concise summary, testing notes (`flutter test`, device runs), linked issues or task IDs, and screenshots/GIFs for UI changes.
- Request review from a Flutter maintainer and confirm CI (if applicable) before merging.
