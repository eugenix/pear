<?php

$spec = Pearfarm_PackageSpec::create(array(Pearfarm_PackageSpec::OPT_BASEDIR => dirname(__FILE__)))
             ->setName('dbmigrator')
             ->setChannel('eugenix.github.com/pear')
             ->setSummary('One-line summary of your PEAR package')
             ->setDescription('Longer description of your PEAR package')
             ->setReleaseVersion('0.0.1')
             ->setReleaseStability('stable')
             ->setApiVersion('0.0.1')
             ->setApiStability('stable')
             ->setLicense(Pearfarm_PackageSpec::LICENSE_MIT)
             ->setNotes('Initial release.')
             ->addMaintainer('lead', 'Eugene Kurbatov', 'eugenix', 'ekur@i-loto.ru')
             ->addGitFiles()             			 
             ->addExecutable('dbmigrator.bat')
			 ->addExecutable('dbmigrator')
             ;