Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/trusty64"
    config.vm.box_url = "ubuntu/trusty64"

    config.vm.define :"fabric_scripts"

    config.vm.synced_folder ".", "/home/vagrant/code"
    config.vm.network "private_network", ip: "192.168.65.1"
    # config.vm.network "forwarded_port", guest: 3000, host: 8080

    config.vm.provider :virtualbox do |vb|
        vb.name = "fabric_scripts"
        vb.customize ["modifyvm", :id, "--memory", "2048"]
    end

    config.vm.provision :fabric do |fabric|
        fabric.fabfile_path = "fabfile.py"
        fabric.tasks = ["ubuntu.packages.update", "ubuntu.packages.cleanup"]
    end
end
