# Node.js & npm Commands Reference

**Project**: GenAI Email & Report Drafting System  
**Date**: January 15, 2026  
**Purpose**: Node.js, npm, and Vite commands for frontend development

---

## 📦 Package Management (npm)

### Install Dependencies

```powershell
# Navigate to frontend directory
cd src/frontend

# Install all dependencies
npm install

# Install specific package
npm install axios

# Install dev dependency
npm install --save-dev @types/node

# Install package with exact version
npm install react@19.2.0

# Install from package-lock.json (exact versions - recommended for CI)
npm ci

# Clean/Quiet Install (useful for scripts)
npm install --no-audit --no-fund --quiet
```

### Current Package Versions (package.json)

```json
{
  "dependencies": {
    "@reduxjs/toolkit": "^2.11.2",
    "react": "^19.2.0",
    "react-dom": "^19.2.0",
    "react-redux": "^9.2.0",
    "react-router-dom": "^7.12.0"
  },
  "devDependencies": {
    "@eslint/js": "^9.39.1",
    "@tailwindcss/postcss": "^4.1.18",
    "@types/node": "^24.10.1",
    "@types/react": "^19.2.5",
    "@types/react-dom": "^19.2.3",
    "@vitejs/plugin-react": "^5.1.1",
    "autoprefixer": "^10.4.23",
    "eslint": "^9.39.1",
    "postcss": "^8.5.6",
    "tailwindcss": "^4.1.18",
    "typescript": "~5.9.3",
    "vite": "npm:rolldown-vite@7.2.5"
  }
}
```

**Note:** npm uses `^` (caret) versioning which allows minor/patch updates. Exact versions are locked in `package-lock.json`. Use `npm ci` in CI pipelines for reproducible builds.

### Update & Remove Packages

```powershell
# Update all packages
npm update

# Update specific package
npm update axios

# Check for outdated packages
npm outdated

# Remove package
npm uninstall axios

# Remove dev dependency
npm uninstall --save-dev @types/node
```

### List & Inspect Packages

```powershell
# List installed packages
npm list

# List top-level packages only
npm list --depth=0

# Show package details
npm show react

# Check for vulnerabilities
npm audit

# Fix vulnerabilities (where possible)
npm audit fix
```

---

## 🚀 Development Server (Vite)

### Start Development Server

```powershell
# Navigate to frontend directory
cd src/frontend

# Start dev server
npm run dev

# Start on specific port
npm run dev -- --port 3000

# Start and open browser
npm run dev -- --open

# Start with host access (for network)
npm run dev -- --host
```

### Build & Preview

```powershell
# Build for production
npm run build

# Preview production build
npm run preview

# Build with specific mode
npm run build -- --mode production
```

---

## 🔍 Code Quality (ESLint)

### Run Linter

```powershell
# Run ESLint
npm run lint

# Run ESLint and fix auto-fixable issues
npm run lint -- --fix

# Lint specific file
npx eslint src/App.tsx

# Lint specific directory
npx eslint src/components/

# Check ESLint config
npx eslint --print-config src/App.tsx
```

### ESLint Configuration

Location: `eslint.config.js`

```javascript
export default [
  {
    files: ['**/*.{ts,tsx}'],
    languageOptions: {
      parser: tsParser,
      parserOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module',
      },
    },
    rules: {
      // Custom rules
    },
  },
];
```

---

## 📝 TypeScript

### Type Checking

```powershell
# Run TypeScript compiler (check only)
npx tsc --noEmit

# Run with specific config
npx tsc --noEmit -p tsconfig.json

# Watch mode
npx tsc --noEmit --watch

# Generate declaration files
npx tsc --declaration --emitDeclarationOnly
```

### TypeScript Configuration

Location: `tsconfig.app.json` (referenced by `tsconfig.json`)

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "useDefineForClassFields": true,
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "moduleResolution": "bundler",
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "skipLibCheck": true,
    "noEmit": true
  },
  "include": ["src"]
}
```

---

## 🧪 Testing

### Run Tests

```powershell
# Run tests
npm test

# Run tests in watch mode
npm test -- --watch

# Run tests without watch mode (for CI/Scripts)
npm test -- --watch=false

# Run tests with coverage
npm test -- --coverage

# Run specific test file
npm test -- src/components/Login.test.tsx

# Run tests matching pattern
npm test -- --testNamePattern="login"
```

---

## 📊 Scripts Reference

### package.json Scripts

```json
{
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "lint": "eslint .",
    "test": "echo \"Error: no test specified\" && exit 1",
    "preview": "vite preview"
  }
}
```

### Common npm Scripts

```powershell
# Development
npm run dev              # Start dev server
npm run build            # Build for production
npm run preview          # Preview production build

# Code Quality
npm run lint             # Run ESLint
npm run lint -- --fix    # Fix ESLint issues

# Testing
npm test                 # Run tests
npm test -- --coverage   # With coverage
```

---

## 🔧 Environment Variables

### Vite Environment Variables

Create `.env` files in `src/frontend/`:

```env
# .env.development
VITE_API_BASE_URL=http://localhost:5000/api

# .env.production
VITE_API_BASE_URL=/api

# .env.local (not committed)
VITE_API_BASE_URL=http://localhost:5000/api
```

### Access in Code

```typescript
// Access environment variable
const apiUrl = import.meta.env.VITE_API_BASE_URL;

// Check mode
if (import.meta.env.DEV) {
  console.log('Development mode');
}
```

---

## 🛠️ Node.js Version Management

### Check Versions

```powershell
# Check Node.js version
node --version

# Check npm version
npm --version

# Check package.json engines
npm pkg get engines
```

### Using nvm (Node Version Manager)

```powershell
# List installed versions
nvm list

# Install specific version
nvm install 18.17.0

# Use specific version
nvm use 18.17.0

# Set default version
nvm alias default 18.17.0
```

---

## 🚀 Production Build

### Build Process

```powershell
# 1. Clean previous build
Remove-Item -Recurse -Force dist -ErrorAction SilentlyContinue

# 2. Install dependencies (clean)
npm ci

# 3. Run linter
npm run lint

# 4. Build for production
npm run build

# 5. Preview build locally
npm run preview
```

### Build Output

```powershell
# Check build output
Get-ChildItem dist

# Check bundle sizes
Get-ChildItem dist/assets | Select-Object Name, @{N='Size(KB)';E={[math]::Round($_.Length/1KB,2)}}
```

---

## 🔄 Complete CI Workflow

### Frontend CI Checks

```powershell
# Navigate to frontend
cd src/frontend

# 1. Install dependencies
npm ci

# 2. Run linter
npm run lint

# 3. Type check
npx tsc --noEmit

# 4. Build
npm run build
```

### One-Liner Check

```powershell
# All checks in one command
npm ci && npm run lint && npx tsc --noEmit && npm run build
```

---

## 🔍 Troubleshooting

### Clear Cache

```powershell
# Clear npm cache
npm cache clean --force

# Clear Vite cache
Remove-Item -Recurse -Force node_modules/.vite -ErrorAction SilentlyContinue

# Full reinstall
Remove-Item -Recurse -Force node_modules
Remove-Item package-lock.json
npm install
```

### Common Issues

```powershell
# Module not found
npm install

# TypeScript errors
npx tsc --noEmit

# ESLint errors
npm run lint -- --fix

# Port already in use
npm run dev -- --port 3001
```

---

## 📊 Quick Reference Card

```powershell
# Package Management
npm install                       # Install all
npm install <package>             # Install package
npm uninstall <package>           # Remove package
npm outdated                      # Check outdated
npm audit                         # Security check

# Development
npm run dev                       # Start dev server
npm run build                     # Build production
npm run preview                   # Preview build
npm run lint                      # Run ESLint

# TypeScript
npx tsc --noEmit                  # Type check

# Testing
npm test                          # Run tests
npm test -- --coverage            # With coverage

# Cleanup
npm cache clean --force           # Clear cache
rm -rf node_modules && npm install # Reinstall
```

---

**Last Updated**: January 15, 2026  
**Repository**: genai-email-report-drafting
