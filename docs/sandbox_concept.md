# Sandbox Concept for AI Agents

## Sandbox concept

A sandbox restricts what a process can see and do. Linux provides the primitives:

| Primitive | What it isolates |
|---|---|
| **Network namespace** | Agent gets its own network stack; no access to host/intranet by default. Punch holes via explicit routing rules. |
| **Mount namespace + tmpfs** | Agent sees only mounted paths you choose. Writable scratch space is ephemeral. |
| **cgroups** | Caps CPU, memory, and I/O so a runaway agent can't starve the host. |
| **seccomp profile** | Allowlist of permitted syscalls. Blocks `fork`, `exec`, raw sockets, etc. |
| **User namespace** | Agent process runs as root inside the sandbox but as an unprivileged UID on the host. |
| **Inter-agent channel** | Agents communicate only through a controlled endpoint (message queue or local HTTP). The channel enforces message shape and rate limits. |

On macOS the equivalent is `sandbox-exec` with a Seatbelt policy profile (same idea, different API).

---

## Managed Sandboxes

But you don't need to manage everything yourself, there are tools.

| Tool | Best for | What it handles |
|---|---|---|
| **Anthropic Managed Agents** | Claude-based agents with minimal ops overhead | Network + filesystem isolation, credential scoping, managed runtime |
| **E2B** | AI coding/tool-use agents needing a real filesystem and shell | Full isolated VM per session, simple SDK, persistent or ephemeral |
| **Modal** | Short-lived agent tasks, GPU workloads | Container isolation, network policies, secret injection, auto-scaling |
| **Fly.io Machines** | Long-running agents needing geographic placement | VM-level isolation, private networking, firewall rules in config |
| **Docker + seccomp** | Self-hosted, need fine-grained control | Container isolation, configurable network, seccomp profiles via Compose |

---

### Dev (Mac M2 ARM)

Use `sandbox-exec` (Seatbelt) natively — no Docker layer, no VM overhead, full native performance.

- Define filesystem and network restrictions in a `.sb` policy file per agent.
- No resource caps (cgroups unavailable on macOS) — acceptable for controlled dev agents.
- Fast iteration: run agents as plain processes, policy enforced by the OS.

### Prod (Linux server)

The same isolation concepts translate directly — swap the tool, keep the mental model.

| What you defined in `.sb` | Linux equivalent |
|---|---|
| Allowed file paths | Mount namespaces + volume mounts |
| Allowed network hosts | Network namespace + iptables / CNI policy |
| Blocked process spawning | seccomp profile |
| Resource caps (now available) | cgroups (CPU, memory, I/O) |

**Docker Compose** wraps all of the above in a few lines of YAML — the natural first step when moving to Linux.

**Kubernetes** is the next step when you need scaling, rolling deploys, or multi-node distribution. Each agent becomes a Pod; network policies and resource limits are first-class config.

```
Mac M2 (dev)          →   sandbox-exec (.sb policy)
Linux server (prod)   →   Docker Compose  →  Kubernetes (if scale needed)
         ↑                       ↑
   same concepts,          same concepts,
   native tool              managed by the orchestrator
```

The agent logic does not change between environments — only the sandbox wrapper does.
