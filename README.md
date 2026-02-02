# ArgoCD Image Updater Examples

This directory contains two examples of ArgoCD Image Updater configurations:

## Example 1: With Write-Back (Git Method)

**File:** `image-updater-with-writeback.yaml`

The `git` write-back method permanently stores image updates in your Git repository by creating commits.

### How it works:
1. Fetches the remote repository from the specified location
2. Checks out the target branch
3. Creates or updates `.argocd-source-<appName>.yaml` (or your specified values file)
4. Commits the changes locally
5. Pushes to the remote repository

### When to use:
- You want persistent storage of image version changes in Git
- Your ArgoCD Applications track branches (not tags or specific revisions)
- You need changes to be tracked in version control
- You want CI/CD workflows to be triggered by image updates

### Key configuration:
```yaml
writeBackConfig:
  method: "git"
  gitConfig:
    repository: "git@github.com:myorg/myrepo.git"
    branch: "main"
    writeBackTarget: "helmvalues:./values.yaml"
```

## Example 2: Without Write-Back (ArgoCD Method)

**File:** `image-updater-without-writeback.yaml`

The `argocd` write-back method directly modifies the ArgoCD `Application` resource in the cluster.

### How it works:
1. Updates the Application resource via Kubernetes API
2. Updates source parameters (like `argocd app set --parameter ...`)
3. ArgoCD re-renders manifests with the new parameters

### When to use:
- You manage Applications imperatively (via Web UI or CLI)
- You don't need persistent storage in Git
- Quick updates without Git overhead
- Temporary or development environments

### Key configuration:
```yaml
writeBackConfig:
  method: "argocd"
```

## Comparison

| Feature | Git Write-Back | ArgoCD Write-Back |
|---------|----------------|-------------------|
| Persistence | Git repository | Cluster only |
| Track changes | Git history | None |
| CI/CD triggers | Yes | No |
| Best for | Production, GitOps | Dev, ad-hoc |
| Default | No | Yes |
| Git required | Yes | No |

## Applying the Examples

Choose the method that fits your workflow:

```bash
# For git write-back (persistent)
kubectl apply -f image-updater-with-writeback.yaml

# For argocd write-back (cluster-only)
kubectl apply -f image-updater-without-writeback.yaml
```

## Notes

- Both examples use Helm with values files
- Update strategy is set to `semver` for semantic versioning
- Images are configured with aliases for easier reference
- Both examples update multiple images (nginx and redis)
# img-updater
