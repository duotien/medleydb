import unittest
import os
import yaml
from medleydb import multitrack
from medleydb import AUDIO_PATH
from medleydb import MIXING_COEFFICIENTS


class TestMultitrack(unittest.TestCase):
    def setUp(self):
        self.mtrack = multitrack.MultiTrack("NightPanther_Fire")
        self.mtrack2 = multitrack.MultiTrack("Phoenix_ScotchMorris")
        self.stem = self.mtrack.stems[8]
        self.raw = self.mtrack.raw_audio[8][1]

    def test_dataset_version_v1(self):
        actual = self.mtrack.dataset_version
        expected = 'V1'
        self.assertEqual(expected, actual)

    def test_dataset_version_v2(self):
        mtrack = multitrack.MultiTrack("FennelCartwright_DearTessie")
        actual = mtrack.dataset_version
        expected = 'V2'
        self.assertEqual(expected, actual)

    def test_dataset_version_extra(self):
        mtrack = multitrack.MultiTrack("AHa_TakeOnMe")
        actual = mtrack.dataset_version
        expected = 'EXTRA'
        self.assertEqual(expected, actual)

    def test_invalid_trackid(self):
        with self.assertRaises(IOError):
            multitrack.MultiTrack("RickAstley_NeverGonnaGiveYouUp")

    def test_audio_path(self):
        actual = self.mtrack.audio_path
        expected = os.path.join(AUDIO_PATH, "NightPanther_Fire")
        self.assertEqual(actual, expected)

    def test_artist(self):
        actual = self.mtrack.artist
        expected = "NightPanther"
        self.assertEqual(actual, expected)

    def test_title(self):
        actual = self.mtrack.title
        expected = "Fire"
        self.assertEqual(actual, expected)

    def test_trackid(self):
        actual = self.mtrack.track_id
        expected = "NightPanther_Fire"
        self.assertEqual(actual, expected)

    def test_stem_length(self):
        actual = len(self.mtrack.stems)
        expected = 12
        self.assertEqual(actual, expected)

    def test_stem_type(self):
        actual = type(self.stem)
        expected = multitrack.Track
        self.assertEqual(actual, expected)

    def test_stem_component(self):
        actual = self.stem.component
        expected = ''
        self.assertEqual(actual, expected)

    def test_stem_duration(self):
        actual = self.stem.duration
        expected = None
        self.assertEqual(actual, expected)

    def test_stem_fname(self):
        actual = os.path.basename(self.stem.audio_path)
        expected = "NightPanther_Fire_STEM_08.wav"
        self.assertEqual(actual, expected)

    def test_stem_instrument(self):
        actual = self.stem.instrument
        expected = ["auxiliary percussion"]
        self.assertEqual(actual, expected)

    def test_stem_f0_type(self):
        actual = self.stem.f0_type
        expected = ["u"]
        self.assertEqual(actual, expected)

    def test_stem_mixpath(self):
        actual = os.path.basename(self.stem.mix_path)
        expected = "NightPanther_Fire_MIX.wav"
        self.assertEqual(actual, expected)

    def test_stem_pitch_annot_none(self):
        actual = self.stem.pitch_annotation
        expected = None
        self.assertEqual(actual, expected)

    def test_stem_pitch_pyin_none(self):
        actual = self.stem.pitch_estimate_pyin
        expected = None
        self.assertEqual(actual, expected)

    def test_stem_pitch_annot_exists(self):
        actual = self.mtrack.stems[7].pitch_annotation
        expected_len = 18268
        self.assertEqual(len(actual), expected_len)

    def test_stem_pitch_pyin_exists(self):
        actual = self.mtrack.stems[7].pitch_estimate_pyin
        expected_len = 25175
        self.assertEqual(len(actual), expected_len)

    def test_stem_raw_idx(self):
        actual = self.stem.raw_idx
        expected = None
        self.assertEqual(actual, expected)

    def test_stem_stem_idx(self):
        actual = self.stem.stem_idx
        expected = 8
        self.assertEqual(actual, expected)

    def test_raw_length1(self):
        actual = len(self.mtrack.raw_audio)
        expected = 12
        self.assertEqual(actual, expected)

    def test_raw_length2(self):
        actual = len(multitrack.get_dict_leaves(self.mtrack.raw_audio))
        expected = 55
        self.assertEqual(actual, expected)

    def test_raw_type(self):
        actual = type(self.raw)
        expected = multitrack.Track
        self.assertEqual(actual, expected)

    def test_raw_component(self):
        actual = self.raw.component
        expected = ''
        self.assertEqual(actual, expected)

    def test_raw_duration(self):
        actual = self.raw.duration
        expected = None
        self.assertEqual(actual, expected)

    def test_raw_fname(self):
        actual = os.path.basename(self.raw.audio_path)
        expected = "NightPanther_Fire_RAW_08_01.wav"
        self.assertEqual(actual, expected)

    def test_raw_instrument(self):
        actual = self.raw.instrument
        expected = ["cymbal"]
        self.assertEqual(actual, expected)

    def test_raw_f0type(self):
        actual = self.raw.f0_type
        expected = ["u"]
        self.assertEqual(actual, expected)

    def test_raw_mixpath(self):
        actual = os.path.basename(self.raw.mix_path)
        expected = "NightPanther_Fire_MIX.wav"
        self.assertEqual(actual, expected)

    def test_raw_pitch_annotation(self):
        actual = self.raw.pitch_annotation
        expected = None
        self.assertEqual(actual, expected)

    def test_raw_raw_idx(self):
        actual = self.raw.raw_idx
        expected = 1
        self.assertEqual(actual, expected)

    def test_raw_stem_idx(self):
        actual = self.raw.stem_idx
        expected = 8
        self.assertEqual(actual, expected)

    def test_stem_instruments(self):
        actual = self.mtrack.stem_instruments
        expected = [
            'auxiliary percussion',
            'brass section',
            'drum machine',
            'drum set',
            'electric bass',
            'male singer',
            'string section',
            'synthesizer',
            'synthesizer',
            'synthesizer',
            'vocalists',
            'vocalists',
        ]
        print(actual)
        self.assertEqual(actual, expected)

    def test_raw_instruments_length(self):
        actual = len(self.mtrack.raw_instruments)
        expected = 55
        self.assertEqual(actual, expected)

    def test_raw_instruments(self):
        actual = self.mtrack.raw_instruments[0:5]
        expected = [
            'brass section',
            'brass section',
            'brass section',
            'brass section',
            'cello'
        ]
        self.assertEqual(actual, expected)

    def test_has_melody(self):
        actual = self.mtrack.has_melody
        expected = True
        self.assertEqual(actual, expected)

    def test_predominant_stem_type(self):
        actual = type(self.mtrack.predominant_stem)
        expected = multitrack.Track
        self.assertEqual(actual, expected)

    def test_predominant_stem_component(self):
        actual = self.mtrack.predominant_stem.component
        expected = 'melody'
        self.assertEqual(actual, expected)

    def test_predominant_stem_stem_idx(self):
        actual = self.mtrack.predominant_stem.stem_idx
        expected = 7
        self.assertEqual(actual, expected)

    def test_melody_annotations(self):
        actual_mel1 = self.mtrack.melody1_annotation
        actual_mel2 = self.mtrack.melody2_annotation
        actual_mel3 = self.mtrack.melody3_annotation

        self.assertEqual(len(actual_mel1), 36692)
        self.assertEqual(len(actual_mel2), 36692)
        self.assertEqual(len(actual_mel3), 36692)

        self.assertEqual(len(actual_mel1[0]), 2)
        self.assertEqual(len(actual_mel2[0]), 2)
        self.assertEqual(len(actual_mel3[0]), 3)

    def test_melody_tracks(self):
        mel_tracks = self.mtrack.melody_stems()
        self.assertEqual(len(mel_tracks), 2)
        self.assertEqual(mel_tracks[0].component, 'melody')
        self.assertEqual(mel_tracks[0].stem_idx, 6)
        self.assertEqual(len(mel_tracks[0].pitch_annotation), 6591)

    def test_bass_tracks(self):
        bass_tracks = self.mtrack.bass_stems()
        self.assertEqual(len(bass_tracks), 1)
        self.assertEqual(bass_tracks[0].component, 'bass')
        self.assertEqual(bass_tracks[0].stem_idx, 1)

    def test_num_stems(self):
        actual = self.mtrack.num_stems()
        expected = 12
        self.assertEqual(actual, expected)

    def test_num_raw(self):
        actual = self.mtrack.num_raw()
        expected = 55
        self.assertEqual(actual, expected)

    def test_stem_filepaths(self):
        actual = len(self.mtrack.stem_filepaths())
        expected = 12
        self.assertEqual(actual, expected)

    def test_raw_filepaths(self):
        actual = len(self.mtrack.raw_filepaths())
        expected = 55
        self.assertEqual(actual, expected)

    def test_stem_activations(self):
        actual = self.mtrack.stem_activations
        self.assertEqual(type(actual), list)

    def test_stem_activations_v2(self):
        actual = self.mtrack.stem_activations_v2
        self.assertEqual(type(actual), list)

    def test_activation_conf_from_stem1(self):
        actual = self.mtrack.activation_conf_from_stem(3)[0]
        expected = [0.0, 0.0474]
        self.assertEqual(actual, expected)

    def test_activation_conf_from_stem_v2(self):
        actual = self.mtrack.activation_conf_from_stem(3, version='v2')[0]
        expected = [0.0, 0.0474]
        self.assertEqual(actual, expected)

    def test_activation_conf_from_stem2(self):
        actual = self.mtrack.activation_conf_from_stem(50)
        expected = None
        self.assertEqual(actual, expected)

    def test_get_mixing_coefficient(self):
        mtrack = multitrack.MultiTrack('AClassicEducation_NightOwl')
        actual = mtrack._get_mixing_coefficient(3)
        expected = 0.2
        self.assertEqual(actual, expected)

    def test_get_mixing_coefficient2(self):
        actual = self.mtrack2._get_mixing_coefficient(3)
        expected = 0.585016969071061
        self.assertAlmostEqual(actual, expected)


class TestTrack(unittest.TestCase):
    def test_track(self):
        track = multitrack.Track(
            'blurbophone', 'fake/path1', 'S12', 'fake/path2',
            component='melody'
        )
        self.assertEqual(track.instrument, ['blurbophone'])
        self.assertEqual(track.audio_path, 'fake/path1')
        self.assertEqual(track.component, 'melody')
        self.assertEqual(track.stem_idx, 12)
        self.assertEqual(track.raw_idx, None)
        self.assertEqual(track.mix_path, 'fake/path2')
        self.assertEqual(track.pitch_path, None)

    def test_track2(self):
        track = multitrack.Track(
            'kazoo', 'fake/path1', 50, 'fake/path2',
            raw_idx='R07'
        )
        self.assertEqual(track.instrument, ['kazoo'])
        self.assertEqual(track.audio_path, 'fake/path1')
        self.assertEqual(track.component, '')
        self.assertEqual(track.stem_idx, 50)
        self.assertEqual(track.raw_idx, 7)
        self.assertEqual(track.mix_path, 'fake/path2')

    def test_track_equality(self):
        track1 = multitrack.Track(
            'blurbophone', 'fake/path1', 'S12', 'fake/path2',
            component='melody'
        )
        track2 = multitrack.Track(
            'blurbophone', 'fake/path1', 'S12', 'fake/path2',
            component='melody'
        )
        actual = track1 == track2
        expected = True
        self.assertEqual(expected, actual)

    def test_track_inequality(self):
        track1 = multitrack.Track(
            'blurbophone', 'fake/path1', 'S12', 'fake/path2',
            component='melody'
        )
        track2 = multitrack.Track(
            'kazoo', 'fake/path1', 50, 'fake/path2',
            raw_idx='R07'
        )
        actual = track1 != track2
        expected = True
        self.assertEqual(expected, actual)


class TestPathBasedir(unittest.TestCase):
    def test_basedir(self):
        path = 'this/is/a/path'
        actual = multitrack._path_basedir(path)
        expected = 'path'
        self.assertEqual(actual, expected)

    def test_basedir2(self):
        path = 'this/is/a/second/path/'
        actual = multitrack._path_basedir(path)
        expected = 'path'
        self.assertEqual(actual, expected)

    def test_basedir3(self):
        path = 'this/is/a/path/with/an/ending/file.txt'
        actual = multitrack._path_basedir(path)
        expected = 'file.txt'
        self.assertEqual(actual, expected)


class TestGetDictLeaves(unittest.TestCase):
    def test_get_leaves(self):
        test_dict = {
            'a': ['z', 'y', 'x'],
            'b': ['w', 't'],
            'c': ['elephant'],
            'd': {'asdf': ['z']},
            'e': {'borg': ['foo']}
        }
        actual = multitrack.get_dict_leaves(test_dict)
        expected = set(['z', 'y', 'x', 'w', 't', 'elephant', 'foo'])
        self.assertEqual(actual, expected)

    def test_get_leaves2(self):
        mtrack = multitrack.MultiTrack('NightPanther_Fire')
        test_dict = {
            'a': mtrack,
            'b': {1: mtrack, 2: mtrack},
            'c': [mtrack],
            'd': {'asdf': mtrack},
            'e': {'borg': [mtrack]}
        }
        actual = multitrack.get_dict_leaves(test_dict)
        expected = set([mtrack, mtrack, mtrack, mtrack, mtrack])
        self.assertEqual(actual, expected)


class TestGetDuration(unittest.TestCase):
    def test_get_duration(self):
        actual = multitrack.get_duration(os.path.join(
            os.path.dirname(__file__), 'data/short_audio.wav'))
        expected = 4.0
        self.assertEqual(actual, expected)


class TestReadAnnotationFile(unittest.TestCase):
    def test_readpitch(self):
        actual, header = multitrack.read_annotation_file(
            os.path.join(os.path.dirname(__file__), 'data/pitch.csv')
        )
        expected = [
            [0.023219954, 189.187],
            [0.029024943, 191.782],
            [0.034829931, 200.344]
        ]
        self.assertEqual(actual, expected)
        self.assertEqual(header, [])

    def test_readmelody(self):
        actual, header = multitrack.read_annotation_file(
            os.path.join(os.path.dirname(__file__), 'data/melody.csv')
        )
        expected = [
            [0.0, 0.0],
            [0.0058049886621315194, 0.0],
            [0.011609977324263039, 0.0],
            [0.017414965986394557, 0.0],
            [0.023219954648526078, 189.18700000000001]
        ]
        self.assertEqual(actual, expected)
        self.assertEqual(header, [])

    def test_invalidpath(self):
        actual, header = multitrack.read_annotation_file('blurb/blork/barg')
        expected = None
        self.assertEqual(actual, expected)
        self.assertEqual(header, expected)


class TestGetValidInstrumentLabels(unittest.TestCase):
    def setUp(self):
        self.labels = multitrack.get_valid_instrument_labels()
        test_taxonomy_fpath = os.path.join(
            os.path.dirname(__file__), 'data/test_taxonomy.yaml')
        with open(test_taxonomy_fpath, 'r') as fhandle:
            self.test_taxonomy = yaml.load(fhandle, Loader=yaml.FullLoader)

    def test_inclusion(self):
        self.assertTrue('female singer' in self.labels)

    def test_inclusion2(self):
        self.assertTrue('erhu' in self.labels)

    def test_exclusion(self):
        self.assertFalse('squidward' in self.labels)

    def test_alternate_taxonomy(self):
        actual = multitrack.get_valid_instrument_labels(
            taxonomy=self.test_taxonomy
        )
        expected = set([
            'rick',
            'morty',
            'beth',
            'summer',
            'jerry',
            'mrs pancakes',
            'tiny rick',
            'squanchy',
            'traflorkians',
            'unity'
        ])
        self.assertEqual(actual, expected)


class TestIsValidInstrument(unittest.TestCase):
    def test_valid_instrument(self):
        actual = multitrack.is_valid_instrument('clarinet')
        expected = True
        self.assertEqual(actual, expected)

    def test_invalid_instrument(self):
        actual = multitrack.is_valid_instrument('Clarinet')
        expected = False
        self.assertEqual(actual, expected)

    def test_invalid_instrument2(self):
        actual = multitrack.is_valid_instrument('mayonnaise')
        expected = False
        self.assertEqual(actual, expected)


class TestGetDatasetVersion(unittest.TestCase):
    def test_version_1(self):
        actual = multitrack.get_dataset_version('MusicDelta_Beethoven')
        expected = 'V1'
        self.assertEqual(expected, actual)

    def test_version_v2(self):
        actual = multitrack.get_dataset_version("FennelCartwright_DearTessie")
        expected = 'V2'
        self.assertEqual(expected, actual)

    def test_version_extra(self):
        actual = multitrack.get_dataset_version("AHa_TakeOnMe")
        expected = 'EXTRA'
        self.assertEqual(expected, actual)

    def test_version_bach10(self):
        actual = multitrack.get_dataset_version("Bach10_05DieNacht")
        expected = 'BACH10'
        self.assertEqual(expected, actual)

    def test_version_none(self):
        actual = multitrack.get_dataset_version("ManateeCommune_Blueberry")
        expected = ''
        self.assertEqual(expected, actual)
