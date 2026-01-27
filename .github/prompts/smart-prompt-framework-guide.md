# S.M.A.R.T. Prompt Framework for GitHub Copilot Coding Agents

**LLMs From Scratch Practice Edition** - Framework for creating high-quality coding agent instructions aligned with this repo’s educational goals.

> **Note**: This guide is for the LLM-from-scratch learning workspace. Any references to other stacks or products below are legacy and should be ignored when working in this repository.

---

## 🎯 **The S.M.A.R.T. Framework**

Use this framework to create highly effective coding agent instructions:

```text
S - Specific Role Definition (Senior Python Developer, Frontend Engineer, AI Integration Specialist, etc.)
M - Mission-Critical Requirements (What must be accomplished with measurable outcomes)
A - Audience-Aware Communication (Team expertise level, architectural maturity, domain context)
R - Response Format Control (Code structure, architecture patterns, documentation style)
T - Task-Oriented Constraints (Technology stack, architectural patterns, forbidden actions)
```

---

## 🏛️ **GenAI System Alignment**

When creating prompts, consider:

- **Prompt Pattern**: Is this instruction-based, role-based, chain-of-thought, or evaluation?
- **Use Case Context**: What task type (email generation, report generation, document history, authentication)?
- **Google Gemini Integration**: Which integration pattern (Python SDK, REST API, or prompt engineering)?
- **Template Reusability**: Can this prompt be templated for reuse across similar use cases?

## 🏗️ **Advanced Problem Statement Template**

Use this enhanced template for coding agent tasks:

```markdown
## ROLE DEFINITION

You are a [Specific Role] specializing in [Technology Stack] with expertise in [Domain Areas]

## MISSION

[Clear, specific objective with measurable outcomes]

## CONTEXT

[Brief overview of current situation and progress made]

## CURRENT STATUS

- **Progress Made**: [Specific achievements and metrics]
- **Main Issue**: [Root cause analysis]
- **Files Affected**: [List specific files]

## REMAINING WORK

### 1. [Priority Task Name] (Priority N)

- **Problem**: [Specific technical issue]
- **Current Error**: [Exact error messages]
- **Solution Approach**: [Concrete implementation steps]
- **Files to Modify**: [Specific file paths]

## TECHNICAL CONSTRAINTS

- **🚨 CRITICAL**: [Non-negotiable requirements]
- **Framework**: [Technology stack requirements]
- **Dependencies**: [Package/version constraints]

## RESPONSE FORMAT REQUIREMENTS

- [Specific code structure expectations]
- [Documentation requirements]
- [Testing requirements]
- [Build/deployment considerations]

## WHAT NOT TO DO

- ❌ [Explicit forbidden actions with reasoning]

## WHAT TO DO

- ✅ [Explicit required actions with priority]

## SUCCESS CRITERIA

[Measurable outcomes with acceptance criteria]

## QUALITY STANDARDS

- [Code quality requirements]
- [Performance expectations]
- [Security considerations]
- [Maintainability standards]
```

## 🎭 **Role-Based Specialization Examples**

### **For Backend (Python/Flask) Development:**

```markdown
ROLE: You are a Senior Python Developer specializing in Flask REST API development, Google Gemini API integration, and PostgreSQL database design

EXPERTISE FOCUS: Flask route handlers, JWT authentication, prompt engineering, SQLAlchemy ORM, error handling patterns

OUTPUT REQUIREMENTS: Production-ready Python code with comprehensive error handling, unit tests with proper mocking, and enterprise-grade documentation

MANDATORY VALIDATION:
- ✅ `pytest tests/` succeeds with 0 failures
- ✅ `flask run` starts without errors
- ✅ All API endpoints return proper HTTP status codes
- ✅ JWT authentication works correctly
```

### **For Frontend (TypeScript/React) Development:**

```markdown
ROLE: You are a Frontend Engineer specializing in React with TypeScript, component architecture, and API integration

EXPERTISE FOCUS: TypeScript type safety, React hooks, component composition, API client patterns, state management

OUTPUT REQUIREMENTS: Type-safe React components with proper error handling, unit tests, and comprehensive TypeScript interfaces

MANDATORY VALIDATION:
- ✅ `npm run build` succeeds with 0 TypeScript errors
- ✅ `npm test` passes with 0 failures
- ✅ ESLint passes with 0 errors
- ✅ All components are properly typed
```

### **For AI Integration & Prompt Engineering:**

```markdown
ROLE: You are an AI Integration Specialist specializing in Google Gemini API integration, prompt engineering, and GenAI content generation

EXPERTISE FOCUS: 
- Prompt engineering and structured prompt construction
- Google Gemini API integration patterns
- Content generation quality and consistency
- Error handling for API failures
- Input validation and security

OUTPUT REQUIREMENTS:
- Production-ready prompt engineering code with comprehensive error handling
- Structured prompts optimized for Google Gemini
- Input validation and sanitization
- Security guardrails and API key protection
- Documentation with prompt strategies and limitations

ARCHITECTURAL PATTERNS:
- Instruction-based prompts for email/report generation
- Role-based prompts for tone and style control
- Chain-of-Thought for complex content generation
- Error handling with graceful degradation

MANDATORY VALIDATION:
- ✅ Prompt engineering tests pass with defined quality metrics
- ✅ API error handling works correctly
- ✅ No API keys exposed in code
- ✅ Generated content meets quality standards
```

### **For N-Tier Architecture Implementation:**

```markdown
ROLE: You are a Lead Enterprise Architect specializing in N-Tier web application architecture, microservices design, and scalable system architecture

EXPERTISE FOCUS:
- N-Tier architecture separation (Presentation, Application, Data, AI Service layers)
- RESTful API design and best practices
- Database schema design and migrations
- Security patterns (JWT, RBAC, input validation)
- System resilience, scalability, and observability

OUTPUT REQUIREMENTS:
- Architecture Decision Records (ADRs) documenting trade-offs
- System design diagrams with components and integration points
- Reference implementations following N-Tier patterns
- Security considerations and best practices
- Database schema with proper relationships

SUCCESS CRITERIA:
- ✅ Architecture maintains clear layer separation
- ✅ Trade-offs clearly documented with reasoning
- ✅ Scalability and resilience characteristics defined
- ✅ Implementation examples demonstrate pattern application
```

## 🚨 **Critical Constraint Guidelines**

### **Framework/Package Versions:**

```markdown
- 🚨 CRITICAL: Use Python 3.9+ ONLY - DO NOT downgrade
- 🚨 CRITICAL: Use React 18+ with TypeScript 5+ - DO NOT downgrade
- ❌ DO NOT modify requirements.txt to downgrade packages
- ❌ DO NOT modify package.json to downgrade dependencies
```

### **File Modification Boundaries:**

```markdown
- ❌ DO NOT modify [specific files]
- ✅ ONLY modify [allowed areas]
```

### **Build Requirements:**

```markdown
When building backend, use: cd src/backend && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt
When building frontend, use: cd src/frontend && npm install && npm run build
Ensure all code follows project standards (PEP 8 for Python, ESLint for TypeScript)
```

## ✅ **Effective Instruction Patterns**

### **DO - Be Specific and Explicit:**

- ✅ "Create prompt_engine.py to construct structured prompts for Google Gemini API"
- ✅ "Update EmailGenerator.tsx to handle API errors gracefully with user-friendly messages"
- ✅ "Fix JWT token validation in auth.py - check token expiration and signature"

### **DON'T - Be Vague:**

- ❌ "Fix the authentication"
- ❌ "Make it work"
- ❌ "Update the code"

## 📝 **Constraint Language Examples**

### **Strong Constraint Language That Works:**

```markdown
🚨 ABSOLUTELY DO NOT modify .env.example or commit API keys to repository.

The following packages MUST remain at their current versions:
- google-generativeai: Latest stable version
- flask-jwt-extended: Latest stable version
- react: ^18.0.0
- typescript: ^5.0.0

CRITICAL: Any attempt to commit API keys or downgrade versions will require task restart.
```

### **Weak Language That Doesn't Work:**

```markdown
Please try to maintain Python 3.9+ compatibility
Prefer keeping current package versions
```

## 🎯 **Advanced Prompt Design Patterns**

### **Multi-Layered Prompt Architecture:**

```markdown
SYSTEM LAYER:
You are a [Specialist Role] with expertise in [Technology Stack] and [Domain Expertise].

CONTEXT LAYER:  
[Project context, current situation, business requirements]

TASK LAYER:
[Specific implementation task with clear deliverables]

SPECIFICATION LAYER:
[Detailed technical requirements, constraints, and acceptance criteria]
```

### **Conditional Logic for Complex Scenarios:**

```markdown
LOGIC FRAMEWORK:
IF issue_type == "gemini_api_error":
THEN approach: Implement retry logic with exponential backoff
AND include: Proper error handling and user notification

ELIF issue_type == "jwt_authentication":  
THEN approach: Verify token signature and expiration
AND include: Refresh token mechanism

ELIF issue_type == "database_connection":
THEN approach: Check connection string and PostgreSQL service
AND include: Connection pooling and error recovery
```

### **Progressive Refinement Pattern:**

```markdown
BASE PROMPT: [Core role and task definition]

REFINEMENT 1: Add specific technical constraints
REFINEMENT 2: Define output format requirements  
REFINEMENT 3: Include quality standards and acceptance criteria
REFINEMENT 4: Add monitoring and validation requirements

FINAL VALIDATION: Ensure all constraints are explicitly stated
```

## 📊 **Output Format Control**

### **For Code Generation Tasks:**

```markdown
OUTPUT REQUIREMENTS:
- Production-ready code with comprehensive error handling
- Unit tests with proper mocking patterns
- Type hints for Python, TypeScript types for React
- Comprehensive docstrings for Python, JSDoc for TypeScript
- Consistent code style following project conventions (PEP 8, ESLint)
- No hardcoded API keys or secrets
- Include integration points and dependency injection setup
```

### **For API Development Tasks:**

```markdown
OUTPUT REQUIREMENTS:
- RESTful API endpoints with proper HTTP methods
- Request/response validation
- Error handling with appropriate status codes
- JWT authentication middleware
- Database transaction management
- API documentation with examples
```

### **For Frontend Component Tasks:**

```markdown
OUTPUT REQUIREMENTS:
- Type-safe React components with TypeScript
- Proper error boundaries and loading states
- API client integration with error handling
- Responsive design considerations
- Accessibility (a11y) compliance
- Unit tests with React Testing Library
```

## 🤖 **Google Gemini Integration Framework**

When designing AI integration tasks, include evaluation and observability requirements:

### **Gemini API Integration Template:**

```markdown
## GEMINI API INTEGRATION FRAMEWORK

### Integration Requirements
- **API Key Management**: Environment variables only, never hardcoded
- **Error Handling**: Retry logic with exponential backoff
- **Rate Limiting**: Respect API rate limits and implement throttling
- **Input Validation**: Validate and sanitize all user inputs before API calls

### Prompt Engineering
- **Structure**: Role definition, task description, tone, formatting
- **Context**: User-provided context integration
- **Output Control**: Length, format, and style constraints
- **Testing**: Test prompts with diverse inputs

### Success Criteria
- API calls succeed with proper error handling
- Generated content meets quality standards
- No API keys exposed in code or logs
- Response times within acceptable range
- Cost tracking and monitoring implemented
```

### **Prompt Engineering Observability Template:**

```markdown
## PROMPT ENGINEERING OBSERVABILITY

### Metrics to Track
- Prompt construction time
- API response latency
- Token usage and costs
- Content quality scores
- Error rates and types

### Logging Implementation
- Structured logging with correlation IDs
- Prompt and response logging (sanitized)
- Error tracking and analysis
- Performance metrics collection

### Observable Signals
- API call success/failure rates
- Content generation quality trends
- User satisfaction metrics
- Cost per generation tracking

### Analysis & Improvement
- Identify prompt optimization opportunities
- Detect quality degradation patterns
- Measure business impact of improvements
- Plan optimizations based on observed patterns
```

## 🎯 **Success Indicators**

### **Agent is working correctly when:**

- ✅ It acknowledges constraints explicitly
- ✅ It asks clarifying questions about boundaries
- ✅ It maintains N-Tier architecture separation
- ✅ It focuses on code changes, not configuration changes
- ✅ It provides detailed progress updates
- ✅ It never commits API keys or secrets

### **Agent needs restart when:**

- ❌ It immediately modifies forbidden files
- ❌ It commits API keys or secrets
- ❌ It ignores explicit constraints
- ❌ It breaks N-Tier architecture separation
- ❌ It takes overly broad approach to simple problems

## 🔄 **Agent Restart Protocol**

### **When to restart the coding agent:**

- Agent commits API keys or secrets
- Agent breaks N-Tier architecture separation
- Agent modifies forbidden files
- Agent ignores explicit constraints
- Agent takes wrong architectural approach

### **How to restart:**

1. Close current pull request
2. Create new pull request with more explicit constraints
3. Include specific examples of what went wrong
4. Add stronger constraint language

## 🏗️ **N-Tier Architecture Patterns**

When tasks span multiple architectural layers, apply these patterns:

### **Pattern: N-Tier Architecture Separation**

```markdown
ARCHITECTURAL PATTERN: N-Tier Architecture with Clear Layer Separation

LAYERS INVOLVED:
- Presentation Layer: React.js with TypeScript (Frontend)
- Application Layer: Flask REST API (Backend)
- Data Layer: PostgreSQL Database
- AI Service Layer: Google Gemini API

IMPLEMENTATION REQUIREMENTS:
- Clear separation between frontend and backend
- RESTful API design with proper HTTP methods
- Database models with SQLAlchemy ORM
- Service layer for business logic
- Prompt engine for AI integration
- Proper error handling at each layer

QUALITY GATES:
✅ Frontend and backend are decoupled
✅ API endpoints follow RESTful conventions
✅ Database models properly defined
✅ Services handle business logic
✅ No direct database access from frontend
✅ Integration tests validate layer boundaries
```

### **Pattern: JWT Authentication & RBAC**

```markdown
ARCHITECTURAL PATTERN: JWT-based Authentication with Role-Based Access Control

CHARACTERISTICS:
- Stateless authentication with JWT tokens
- Role-based access control (Admin, User)
- Token refresh mechanism
- Secure token storage (localStorage with expiration)

IMPLEMENTATION REQUIREMENTS:
- JWT token generation and validation
- Role-based route protection
- Token refresh endpoint
- Secure password hashing (bcrypt)
- Input validation and sanitization

QUALITY GATES:
✅ Tokens are properly signed and validated
✅ Roles are enforced at API level
✅ Passwords are hashed, never stored plaintext
✅ Token expiration is handled gracefully
✅ Security best practices followed
```

## 📋 **Universal PR Success Template**

Include this template in EVERY coding agent PR for consistent validation:

```markdown
## 🎯 MANDATORY SUCCESS CRITERIA (NON-NEGOTIABLE)

### Backend Build Requirements
```powershell
# MUST PASS: Backend tests with zero failures
cd src/backend
python -m pytest tests/ -v
# Expected Result: "passed" with 0 failures
```

### Frontend Build Requirements

```powershell
# MUST PASS: Frontend build with zero TypeScript errors
cd src/frontend
npm run build
# Expected Result: Build succeeds with 0 errors
```

### Test Requirements

```powershell
# MUST PASS: All existing unit tests
cd src/backend && python -m pytest tests/ -v
cd src/frontend && npm test
# Expected Result: All tests pass with 0 failures
```

## 📋 FINAL CHECKLIST

Before marking this PR ready for review:

- [ ] ✅ Backend tests pass with 0 failures
- [ ] ✅ Frontend build succeeds with 0 TypeScript errors
- [ ] ✅ All original issues resolved completely
- [ ] ✅ No API keys or secrets committed
- [ ] ✅ N-Tier architecture separation maintained
- [ ] ✅ All existing functionality preserved
- [ ] ✅ Production-ready error handling implemented

**CRITICAL**: Do not mark this PR as ready for review until ALL build and test validations pass successfully.

```text

## 🚀 **GenAI Email & Report Drafting System-Specific S.M.A.R.T. Example**

```markdown
ROLE: You are a Senior Full-Stack Developer specializing in N-Tier web applications, Google Gemini AI integration, and enterprise-grade authentication systems

MISSION: Implement email generation feature in the GenAI Email & Report Drafting System - an enterprise-grade, N-Tier web application for AI-powered content generation using React.js with TypeScript, Flask REST API, PostgreSQL, and Google Gemini API

AUDIENCE: Development team with expertise in:
- React.js with TypeScript and modern React patterns
- Flask REST API development and JWT authentication
- PostgreSQL database design and SQLAlchemy ORM
- Google Gemini API integration and prompt engineering
- N-Tier architecture patterns

RESPONSE FORMAT:
- Production-ready code with comprehensive error handling
- Type-safe TypeScript components and Python type hints
- Unit tests for both frontend and backend
- Enterprise-grade documentation with API examples
- Proper N-Tier architecture separation

TASK CONSTRAINTS:
- 🚨 CRITICAL: Maintain N-Tier architecture separation
- 🚨 CRITICAL: Never commit API keys or secrets
- Architecture: Frontend (React/TypeScript) → Backend (Flask) → Database (PostgreSQL) → AI Service (Google Gemini)
- Quality Standards: Zero build errors, 100% test pass rate
- Technology Stack: React 18+, TypeScript 5+, Python 3.9+, Flask, PostgreSQL, Google Gemini API
```

## 📚 **Best Practices Summary**

1. **Be Specific**: Define exact roles, technologies, and constraints
2. **Set Clear Boundaries**: Use strong constraint language
3. **Define Success**: Include measurable outcomes and validation steps
4. **Control Output**: Specify exactly what format and quality you expect
5. **Plan for Failure**: Include restart protocols and troubleshooting
6. **Validate Everything**: Always include build and test requirements
7. **Document Thoroughly**: Ensure all decisions and constraints are recorded
8. **Align with Architecture**: Reference N-Tier architecture patterns
9. **Enable Observability**: Include tracing and evaluation requirements
10. **Progressive Complexity**: Scale scope to team's architectural maturity level

---

## ⚡ **Quick Reference Checklist**

Use this checklist before submitting any coding agent task:

### **Role Definition**

- [ ] Specific role/expertise clearly stated
- [ ] Technology stack and frameworks identified
- [ ] Expected audience knowledge level documented
- [ ] Domain context provided

### **Task Clarity**

- [ ] Mission and objectives clearly defined
- [ ] Success criteria are measurable
- [ ] Scope is appropriately sized
- [ ] Priority and sequencing defined

### **Technical Requirements**

- [ ] Framework and version constraints specified
- [ ] Architectural patterns identified (N-Tier)
- [ ] Dependencies listed explicitly
- [ ] Integration points documented

### **Constraints & Boundaries**

- [ ] Forbidden actions explicitly listed (❌)
- [ ] Required actions explicitly listed (✅)
- [ ] File modification boundaries defined
- [ ] Architectural decision constraints included

### **Quality & Validation**

- [ ] Code quality standards specified (PEP 8, ESLint)
- [ ] Build/test requirements included
- [ ] Performance expectations defined
- [ ] Security considerations addressed (API keys, JWT)

### **AI Integration Specifics** (if applicable)

- [ ] Google Gemini API integration patterns defined
- [ ] Prompt engineering requirements specified
- [ ] Error handling for API failures included
- [ ] Security guardrails documented

### **Output Expectations**

- [ ] Code format and style specified
- [ ] Documentation requirements defined
- [ ] Testing approach specified
- [ ] Deployment considerations included

---

## 📋 **FINAL VALIDATION CHECKLIST**

Before submitting ANY coding agent PR or task completion:

- [ ] ✅ All technical constraints acknowledged
- [ ] ✅ Success criteria clearly measurable
- [ ] ✅ Backend tests pass without errors/failures
- [ ] ✅ Frontend build succeeds without TypeScript errors
- [ ] ✅ No forbidden files modified
- [ ] ✅ N-Tier architectural patterns applied correctly
- [ ] ✅ No API keys or secrets committed
- [ ] ✅ Documentation is complete and accurate
- [ ] ✅ Code review readiness criteria met

---

## 🎓 **GenAI System Integration**

Align your coding agent tasks with GenAI Email & Report Drafting System best practices:

### **For Prompt Engineering Development:**

- Focus on structured prompt construction for Google Gemini
- Demonstrate proper role definition and task description
- Include tone and formatting control
- Show proper error handling and validation

### **For Google Gemini Integration:**

- Use proper SDK patterns (Python google-generativeai)
- Implement retry logic and error handling
- Include configuration management and API key handling
- Demonstrate proper logging and observability

### **For Template Creation:**

- Create reusable prompt templates for email/report generation
- Document use cases and when to apply each template
- Include evaluation criteria and testing approaches
- Provide governance guidelines and review workflows

This framework ensures consistent, high-quality results from GitHub Copilot coding agents while preventing common issues and maintaining enterprise-grade standards aligned with Google Gemini best practices and N-Tier architecture principles.
