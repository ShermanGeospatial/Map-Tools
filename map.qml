import QtQuick 2.4
import QtPositioning 5.4
import QtLocation 5.4


Rectangle {
    id:rectangle
    width: 640
    height: 480
    Plugin {
        id: osmPlugin
        name: "osm"
    }
    property variant locationTC: QtPositioning.coordinate(44.951, -93.192)
    Map {
        id: map
        anchors.fill: parent
        plugin: osmPlugin
        center: locationTC
        zoomLevel: 10
        MapItemView{
            model: markermodel
            delegate: MapQuickItem {
                coordinate: model.position_marker
                anchorPoint.x: image.width
                anchorPoint.y: image.height
                sourceItem:
                    Image { id: image; source: model.source_marker }
            }
        }
    }
}