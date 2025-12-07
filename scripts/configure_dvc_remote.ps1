<#
Configure a DVC remote and push dataset. This script supports common providers.

Usage (pick one remote and fill credentials or set env vars):

# AWS S3 (recommended: set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY as env vars)
# ./configure_dvc_remote.ps1 -RemoteName myremote -Type s3 -URL s3://my-bucket/path

# Azure Blob
# ./configure_dvc_remote.ps1 -RemoteName myremote -Type azure -URL azure://myaccount.blob.core.windows.net/mycontainer/path

# GCS
# ./configure_dvc_remote.ps1 -RemoteName myremote -Type gcs -URL gcs://my-bucket/path

# SSH (server must be reachable and you must have SSH access)
# ./configure_dvc_remote.ps1 -RemoteName myremote -Type ssh -URL ssh://user@host:/path/to/dvc-storage

Note: This script requires `dvc` to be installed and available on PATH.
#>

param(
    [Parameter(Mandatory=$true)] [string]$RemoteName,
    [Parameter(Mandatory=$true)] [ValidateSet('s3','azure','gcs','ssh','local')] [string]$Type,
    [Parameter(Mandatory=$true)] [string]$URL
)

function Ensure-Dvc {
    $cmd = Get-Command dvc -ErrorAction SilentlyContinue
    if (-not $cmd) {
        Write-Error "`dvc` not found on PATH. Install DVC: `pip install dvc` or see https://dvc.org/doc/install`
        exit 2
    }
}

Ensure-Dvc

Write-Output "Configuring DVC remote '$RemoteName' of type '$Type' -> $URL"
 & dvc remote remove $RemoteName 2>$null | Out-Null
 & dvc remote add -d $RemoteName $URL

switch ($Type) {
    's3' {
        Write-Output "Using S3 remote. Ensure AWS credentials are set in environment or config."
        # Optionally: configure endpoint or profile here
    }
    'azure' {
        Write-Output "Using Azure Blob remote. Ensure AZURE_STORAGE_ACCOUNT and AZURE_STORAGE_KEY are set."
    }
    'gcs' {
        Write-Output "Using GCS remote. Ensure GOOGLE_APPLICATION_CREDENTIALS env var points to JSON key."
    }
    'ssh' {
        Write-Output "Using SSH remote. Ensure SSH keys / access configured."
    }
    'local' {
        Write-Output "Using local filesystem remote. URL should be a path like /path/to/remote or C:/path/to/remote"
    }
}

Write-Output "Verifying DVC status for tracked files..."
& dvc status

Write-Output "Attempting to push DVC-tracked data to remote '$RemoteName'..."
try {
    & dvc push
    if ($LASTEXITCODE -eq 0) {
        Write-Output "dvc push succeeded."
    } else {
        Write-Warning "dvc push exited with code $LASTEXITCODE. Check credentials and remote availability."
    }
} catch {
    Write-Error "dvc push failed: $_"
}
