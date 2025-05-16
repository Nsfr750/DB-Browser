# Changelog

## [Unreleased]

## [1.3.1-beta.1](https://github.com/Nsfr750/DB-Browser/compare/1.3.0...1.3.1-beta.1) (2025-05-16)

### Features

- **Help System**: Added comprehensive help system with searchable documentation
- **Keyboard Shortcuts**: Added Ctrl+H for help and Ctrl+S for sponsors
- **Documentation**: Updated documentation structure
- **Error Handling**: Improved error handling for database connections
- **Logging**: Added comprehensive logging system
- **UI**: Improved user interface consistency

### Bug Fixes

- **MySQL**: Fixed connection timeout issues
- **SQLite**: Fixed file path handling
- **Access**: Fixed driver detection
- **dBase**: Fixed field type conversion

### Breaking Changes

- **API**: Changed database handler interface
- **Configuration**: Updated configuration file format

### Dependencies

- **mysqlclient**: Updated to 2.2.1
- **psycopg2-binary**: Added for PostgreSQL support
- **pyodbc**: Updated to 4.0.39

### Documentation

- **README**: Updated with new features
- **API**: Updated documentation
- **Installation**: Added PostgreSQL setup guide

### Internal

- **Testing**: Added PostgreSQL tests
- **Linting**: Updated linting rules
- **Build**: Updated build configuration

## [1.3.0] (2025-05-15)

### Added
- Sample database creation tool
  - Create sample SQLite databases
  - Create sample Microsoft Access databases
  - Create sample MVO databases
  - Create sample MySQL databases
  - Create sample PostgreSQL databases
- Sponsor integration system
  - Access sponsor information from application
  - Support through multiple platforms
- Plugin system
  - Modular architecture for extensible functionality
  - Support for database handlers, UI components, and export plugins
- Support for Microsoft Access databases (.mdb, .accdb)
- Support for PostgreSQL database connections
- Enhanced database connection and error handling
- Unified database querying and export interface
- Support for dBase database format
- Support for MySQL database format
- Support for PostgreSQL database format
- Sample database creation menu with all supported database types
- Organized sample databases in dedicated `sample_databases` directory

### Improved
- Logging system for database operations
- Error tracking and reporting
- Modular database handler architecture
- Added support for dBase (.dbf, .db3) database files
- Simplified database connection and table browsing logic
- Updated About dialog to reflect new database support
- Enhanced keyboard shortcuts
- Improved documentation structure
- Better error handling for database connections
- More robust plugin initialization

### Changed
- Improved documentation and README
- Enhanced version tracking
- Updated database file extensions in documentation
- Added sponsor system integration
- Refactored database handler initialization
- Updated plugin manager to accept root window parameter
- Modified SQLiteApp to handle plugin manager integration

## [1.2.0-beta] - 2025-05-15 🚀

### 🆕 Added
- Full MySQL database support
  - Connection management
  - Table listing
  - Data browsing
- Centralized version management system
  - `version.py` module for consistent versioning
- Comprehensive project documentation
  - User guide
  - Development guidelines
  - Changelog
- Enhanced error handling framework

### 🔧 Changed
- Refactored code structure for improved maintainability
  - Modular database handler design
  - Consistent error handling across database types
- Updated README with detailed project information
- Improved UI responsiveness and layout
- Enhanced logging and debugging capabilities

### 🐛 Fixed
- Resolved potential database connection stability issues
- Minor performance optimizations
- UI rendering glitches in table view
- Improved CSV export reliability

### 🔬 Security
- Added input validation for database connections
- Implemented safer error handling mechanisms

## [1.0.0] - 2025-01-01 🎉

### 🌟 Initial Release
- Core features:
  - Support for SQLite databases
  - Basic table browsing functionality
  - CSV export capabilities
- Simple and intuitive user interface
- Basic error handling
- Minimal database connection support

## Versioning Strategy 📊

We follow [Semantic Versioning 2.0.0](https://semver.org/)

- **MAJOR** version: Incompatible API changes
- **MINOR** version: Backwards-compatible features
- **PATCH** version: Backwards-compatible bug fixes

### Version Qualifiers
- `alpha`: Experimental, unstable features
- `beta`: Feature-complete but not fully tested
- `rc`: Release candidate, near-final version
- No qualifier: Stable release

## Future Roadmap 🗺️

- [ ] Expand database format support
- [ ] Implement advanced query capabilities
- [ ] Create comprehensive test suite
- [ ] Improve cross-platform compatibility
