# Find file containing Squish API for BDD
source(findFile('scripts', 'python/bdd.py'))

# Set up hooks to perform actions during test execution
setupHooks('../shared/scripts/bdd_hooks.py')

# Scan for and import step definitions found in the directories specified as arguments
collectStepDefinitions('./steps', '../shared/steps')

def main():
    testSettings.throwOnFailure = True
    
    # Run all the Scenarios in the specified Gherkin .feature file, after hooks are set up and steps are collected
    runFeatureFile('test.feature')
