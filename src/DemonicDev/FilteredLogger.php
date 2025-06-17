<?php
namespace DemonicDev;

use Logger;
use LogLevel;

class FilteredLogger extends \SimpleLogger
{
    private Logger $delegate;
    private string $prefix;

    public function __construct(Logger $delegate, string $prefix){
        $this->delegate = $delegate;
        $this->prefix = $prefix;
    }

    public function log($level, $message){
        $this->delegate->log($level, "[$this->prefix] $message");
    }

    public function logException(\Throwable $e, $trace = null){
        $this->delegate->logException($e, $trace);
    }

    public function getPrefix() : string{
        return $this->prefix;
    }

    public function setPrefix(string $prefix) : void{
        $this->prefix = $prefix;
    }

    public function info($message){
        $this->log(LogLevel::DEBUG, $message);
    } //Overrides the function of SimpleLogger for the GCManager -> Message isnt send unless Debug level is enabled
}