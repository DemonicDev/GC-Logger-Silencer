<?php

#declare(strict_types=1);
namespace DemonicDev;

use pocketmine\GarbageCollectorManager;
use pocketmine\plugin\PluginBase;

class Main extends PluginBase{

    public function onLoad(): void {
        $memoryManager = $this->getServer()->getMemoryManager();

        $reflection = new \ReflectionClass($memoryManager);
        $property = $reflection->getProperty("cycleGcManager");
        $property->setAccessible(true);

        /** @var GarbageCollectorManager $cycleGcManager */
        $cycleGcManager = $property->getValue($memoryManager);

        $reflection = new \ReflectionClass($cycleGcManager);
        $property = $reflection->getProperty("logger");
        $property->setAccessible(true);

        $logger = $this->getServer()->getLogger();
        $property->setValue($cycleGcManager, new FilteredLogger($logger, "Cyclic Garbage Collector"));
    }

}
