import {
  BasePacket,
  IpPacket,
  TcpPacket,
  UdpPacket,
} from "../PacketsStruct"
import PacketUtils from "../PacketUtils"

export default class IpPacketFormatter {

  static build(obj: IpPacket): Buffer {

    var ipPacketBuffer: Buffer = Buffer.allocUnsafe(20);
    ipPacketBuffer[0] = (obj.version << 4) | (20 / 4);
    ipPacketBuffer[1] = obj.TOS;

    ipPacketBuffer.writeUInt16BE(obj.totalLength, 2);
    try {
        ipPacketBuffer.writeUInt16BE(obj.identification, 4);
    } catch (error) {
      console.log(obj.identification);
    }
    ipPacketBuffer.writeUInt16BE(obj.identification, 4);

    ipPacketBuffer[6] = obj.flags == undefined ? 0x40 : obj.flags;

    ipPacketBuffer[7] = 0x00

    ipPacketBuffer[8] = obj.TTL;
    ipPacketBuffer[9] = obj.protocol;

    ipPacketBuffer.writeUInt16BE(0, 10);
    obj.sourceIp.copy(ipPacketBuffer, 12);
    obj.destinationIp.copy(ipPacketBuffer, 16);
}
