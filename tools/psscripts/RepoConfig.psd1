@{
  RepoName = 'llms-from-scratch-practice'

  ExpectedFolders = @(
    '.copilot'
    '.cursor'
    'docs'
    'examples'
    'notebooks'
    'reading-notes'
    'source-material'
    'src'
    'tools\psscripts'
    '.github'
    '.cursor\rules'
  )

  YamlCheckRoots = @(
    'docs'
  )

  DisallowInterviewLanguage = $false
}
