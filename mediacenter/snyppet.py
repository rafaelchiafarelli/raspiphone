    def get_full_status(self):
        position_string = self._player_interface.VideoPos(ObjectPath('/not/used'))
        VideoPosition = list(map(int, position_string.split(" ")))
        ret = {
            'FileName':self._source,
            'Previous':self._player_interface.Previous(),
            'next':self._player_interface.Next(),
            'is_playing':self.is_playing,
            'VideoPos':VideoPosition,
            'duration':self._player_interface_property('Duration') / (1000.0 * 1000.0),
            'duration_us':self._player_interface_property('Duration'),
            'height':self._player_interface_property('ResWidth'),
            'AspectRatio':self._player_interface_property('Aspect'),
            'Metadata':self._player_interface_property('Metadata'),
            'Rate':self._rate,
            'MaximumRate':self._player_interface_property('MaximumRate'),
            'MinimumRate':self._player_interface_property('MinimumRate'),
            'Position': self._player_interface_property('Position') / (1000.0 * 1000.0),
            'Position_us':self._player_interface_property('Position'),
            'Volume':self._player_interface_property('Volume'),
            'PlayBack_status':self._player_interface_property('PlaybackStatus'),
            'CanPause':self._player_interface_property('CanPause'),
            'CanPlay':self._player_interface_property('CanPlay'),
            'CanControl':self._player_interface_property('CanControl'),
            'CanSeek':self._player_interface_property('CanSeek'),
            'CanGoNext':self._player_interface_property('CanGoNext'),
            'SupportedUriSchemes':self._root_interface_property('SupportedUriSchemes'),
            'Identity':self._root_interface_property('Identity'),
            'HasTrackList':self._root_interface_property('HasTrackList'),
            'CanRaise':self._root_interface_property('CanRaise'),
            'CanSetFullScreen':self._root_interface_property('CanSetFullScreen'),
            'FullScreen':self._root_interface_property('FullScreen'),
            'CanQuit':self._root_interface_property('CanQuit')
            }
        return ret