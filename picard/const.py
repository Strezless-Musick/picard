# -*- coding: utf-8 -*-
#
# Picard, the next-generation MusicBrainz tagger
# Copyright (C) 2007 Lukáš Lalinský
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

# Install gettext "noop" function in case const.py gets imported directly.
import __builtin__
__builtin__.__dict__['N_'] = lambda a: a

# Host for PUID submissions
PUID_SUBMIT_HOST = "musicbrainz.org"
PUID_SUBMIT_PORT = 80

# Amazon associate and developer ids
AMAZON_STORE_ASSOCIATE_IDS = {
    u'amazon.ca': u'musicbrainz01-20',
    u'amazon.co.jp': u'musicbrainz-22',
    u'amazon.co.uk': u'musicbrainz0c-21',
    u'amazon.com': u'musicbrainz0d-20',
    u'amazon.de': u'musicbrainz00-21',
    u'amazon.fr': u'musicbrainz0e-21',
}

# MusicDNS client ID
MUSICDNS_KEY = "0736ac2cd889ef77f26f6b5e3fb8a09c"

# AcoustID client API key
ACOUSTID_KEY = '0zClDiGo'

# Various Artists MBID
VARIOUS_ARTISTS_ID = '89ad4ac3-39f7-470e-963a-56509c546377'

# Release formats
RELEASE_FORMATS = {
    u'CD': N_('CD'),
    u'CD-R': N_('CD-R'),
    u'HDCD': N_('HDCD'),
    u'8cm CD': N_('8cm CD'),
    u'Vinyl': N_('Vinyl'),
    u'7" Vinyl': N_('7" Vinyl'),
    u'10" Vinyl': N_('10" Vinyl'),
    u'12" Vinyl': N_('12" Vinyl'),
    u'Digital Media': N_('Digital Media'),
    u'USB Flash Drive': N_('USB Flash Drive'),
    u'slotMusic': N_('slotMusic'),
    u'Cassette': N_('Cassette'),
    u'DVD': N_('DVD'),
    u'DVD-Audio': N_('DVD-Audio'),
    u'DVD-Video': N_('DVD-Video'),
    u'SACD': N_('SACD'),
    u'DualDisc': N_('DualDisc'),
    u'MiniDisc': N_('MiniDisc'),
    u'Blu-ray': N_('Blu-ray'),
    u'HD-DVD': N_('HD-DVD'),
    u'Videotape': N_('Videotape'),
    u'VHS': N_('VHS'),
    u'Betamax': N_('Betamax'),
    u'VCD': N_('VCD'),
    u'SVCD': N_('SVCD'),
    u'UMD': N_('UMD'),
    u'Other': N_('Other'),
    u'LaserDisc': N_('LaserDisc'),
    u'Cartridge': N_('Cartridge'),
    u'Reel-to-reel': N_('Reel-to-reel'),
    u'DAT': N_('DAT'),
    u'Wax Cylinder': N_('Wax Cylinder'),
    u'Piano Roll': N_('Piano Roll'),
    u'DCC': N_('DCC')
}

# Release countries
RELEASE_COUNTRIES = {
    u'BD': N_('Bangladesh'),
    u'BE': N_('Belgium'),
    u'BF': N_('Burkina Faso'),
    u'BG': N_('Bulgaria'),
    u'BB': N_('Barbados'),
    u'WF': N_('Wallis and Futuna Islands'),
    u'BM': N_('Bermuda'),
    u'BN': N_('Brunei Darussalam'),
    u'BO': N_('Bolivia'),
    u'BH': N_('Bahrain'),
    u'BI': N_('Burundi'),
    u'BJ': N_('Benin'),
    u'BT': N_('Bhutan'),
    u'JM': N_('Jamaica'),
    u'BV': N_('Bouvet Island'),
    u'BW': N_('Botswana'),
    u'WS': N_('Samoa'),
    u'BR': N_('Brazil'),
    u'BS': N_('Bahamas'),
    u'BY': N_('Belarus'),
    u'BZ': N_('Belize'),
    u'RU': N_('Russian Federation'),
    u'RW': N_('Rwanda'),
    u'RE': N_('Reunion'),
    u'TM': N_('Turkmenistan'),
    u'TJ': N_('Tajikistan'),
    u'RO': N_('Romania'),
    u'TK': N_('Tokelau'),
    u'GW': N_('Guinea-Bissa'),
    u'GU': N_('Guam'),
    u'GT': N_('Guatemala'),
    u'GR': N_('Greece'),
    u'GQ': N_('Equatorial Guinea'),
    u'GP': N_('Guadeloupe'),
    u'JP': N_('Japan'),
    u'GY': N_('Guyana'),
    u'GF': N_('French Guiana'),
    u'GE': N_('Georgia'),
    u'GD': N_('Grenada'),
    u'GB': N_('United Kingdom'),
    u'GA': N_('Gabon'),
    u'SV': N_('El Salvador'),
    u'GN': N_('Guinea'),
    u'GM': N_('Gambia'),
    u'GL': N_('Greenland'),
    u'GI': N_('Gibraltar'),
    u'GH': N_('Ghana'),
    u'OM': N_('Oman'),
    u'TN': N_('Tunisia'),
    u'JO': N_('Jordan'),
    u'HT': N_('Haiti'),
    u'HU': N_('Hungary'),
    u'HK': N_('Hong Kong'),
    u'HN': N_('Honduras'),
    u'HM': N_('Heard and Mc Donald Islands'),
    u'VE': N_('Venezuela'),
    u'PR': N_('Puerto Rico'),
    u'PW': N_('Palau'),
    u'PT': N_('Portugal'),
    u'SJ': N_('Svalbard and Jan Mayen Islands'),
    u'PY': N_('Paraguay'),
    u'IQ': N_('Iraq'),
    u'PA': N_('Panama'),
    u'PF': N_('French Polynesia'),
    u'PG': N_('Papua New Guinea'),
    u'PE': N_('Peru'),
    u'PK': N_('Pakistan'),
    u'PH': N_('Philippines'),
    u'PN': N_('Pitcairn'),
    u'PL': N_('Poland'),
    u'PM': N_('St. Pierre and Miquelon'),
    u'ZM': N_('Zambia'),
    u'EH': N_('Western Sahara'),
    u'EE': N_('Estonia'),
    u'EG': N_('Egypt'),
    u'ZA': N_('South Africa'),
    u'EC': N_('Ecuador'),
    u'IT': N_('Italy'),
    u'VN': N_('Viet Nam'),
    u'SB': N_('Solomon Islands'),
    u'ET': N_('Ethiopia'),
    u'SO': N_('Somalia'),
    u'ZW': N_('Zimbabwe'),
    u'SA': N_('Saudi Arabia'),
    u'ES': N_('Spain'),
    u'ER': N_('Eritrea'),
    u'MD': N_('Moldova, Republic of'),
    u'MG': N_('Madagascar'),
    u'MA': N_('Morocco'),
    u'MC': N_('Monaco'),
    u'UZ': N_('Uzbekistan'),
    u'MM': N_('Myanmar'),
    u'ML': N_('Mali'),
    u'MO': N_('Macau'),
    u'MN': N_('Mongolia'),
    u'MH': N_('Marshall Islands'),
    u'MK': N_('Macedonia, The Former Yugoslav Republic of'),
    u'MU': N_('Mauritius'),
    u'MT': N_('Malta'),
    u'MW': N_('Malawi'),
    u'MV': N_('Maldives'),
    u'MQ': N_('Martinique'),
    u'MP': N_('Northern Mariana Islands'),
    u'MS': N_('Montserrat'),
    u'MR': N_('Mauritania'),
    u'UG': N_('Uganda'),
    u'MY': N_('Malaysia'),
    u'MX': N_('Mexico'),
    u'IL': N_('Israel'),
    u'FR': N_('France'),
    u'IO': N_('British Indian Ocean Territory'),
    u'SH': N_('St. Helena'),
    u'FI': N_('Finland'),
    u'FJ': N_('Fiji'),
    u'FK': N_('Falkland Islands (Malvinas)'),
    u'FM': N_('Micronesia, Federated States of'),
    u'FO': N_('Faroe Islands'),
    u'NI': N_('Nicaragua'),
    u'NL': N_('Netherlands'),
    u'NO': N_('Norway'),
    u'NA': N_('Namibia'),
    u'VU': N_('Vanuatu'),
    u'NC': N_('New Caledonia'),
    u'NE': N_('Niger'),
    u'NF': N_('Norfolk Island'),
    u'NG': N_('Nigeria'),
    u'NZ': N_('New Zealand'),
    u'ZR': N_('Zaire'),
    u'NP': N_('Nepal'),
    u'NR': N_('Nauru'),
    u'NU': N_('Niue'),
    u'CK': N_('Cook Islands'),
    u'CI': N_('Cote d\'Ivoire'),
    u'CH': N_('Switzerland'),
    u'CO': N_('Colombia'),
    u'CN': N_('China'),
    u'CM': N_('Cameroon'),
    u'CL': N_('Chile'),
    u'CC': N_('Cocos (Keeling) Islands'),
    u'CA': N_('Canada'),
    u'CG': N_('Congo'),
    u'CF': N_('Central African Republic'),
    u'CZ': N_('Czech Republic'),
    u'CY': N_('Cyprus'),
    u'CX': N_('Christmas Island'),
    u'CR': N_('Costa Rica'),
    u'CV': N_('Cape Verde'),
    u'CU': N_('Cuba'),
    u'SZ': N_('Swaziland'),
    u'SY': N_('Syrian Arab Republic'),
    u'KG': N_('Kyrgyzstan'),
    u'KE': N_('Kenya'),
    u'SR': N_('Suriname'),
    u'KI': N_('Kiribati'),
    u'KH': N_('Cambodia'),
    u'KN': N_('Saint Kitts and Nevis'),
    u'KM': N_('Comoros'),
    u'ST': N_('Sao Tome and Principe'),
    u'SI': N_('Slovenia'),
    u'KW': N_('Kuwait'),
    u'SN': N_('Senegal'),
    u'SM': N_('San Marino'),
    u'SL': N_('Sierra Leone'),
    u'SC': N_('Seychelles'),
    u'KZ': N_('Kazakhstan'),
    u'KY': N_('Cayman Islands'),
    u'SG': N_('Singapore'),
    u'SE': N_('Sweden'),
    u'SD': N_('Sudan'),
    u'DO': N_('Dominican Republic'),
    u'DM': N_('Dominica'),
    u'DJ': N_('Djibouti'),
    u'DK': N_('Denmark'),
    u'VG': N_('Virgin Islands (British)'),
    u'DE': N_('Germany'),
    u'YE': N_('Yemen'),
    u'DZ': N_('Algeria'),
    u'US': N_('United States'),
    u'UY': N_('Uruguay'),
    u'YT': N_('Mayotte'),
    u'UM': N_('United States Minor Outlying Islands'),
    u'LB': N_('Lebanon'),
    u'LC': N_('Saint Lucia'),
    u'LA': N_('Lao People\'s Democratic Republic'),
    u'TV': N_('Tuvalu'),
    u'TW': N_('Taiwan'),
    u'TT': N_('Trinidad and Tobago'),
    u'TR': N_('Turkey'),
    u'LK': N_('Sri Lanka'),
    u'LI': N_('Liechtenstein'),
    u'LV': N_('Latvia'),
    u'TO': N_('Tonga'),
    u'LT': N_('Lithuania'),
    u'LU': N_('Luxembourg'),
    u'LR': N_('Liberia'),
    u'LS': N_('Lesotho'),
    u'TH': N_('Thailand'),
    u'TF': N_('French Southern Territories'),
    u'TG': N_('Togo'),
    u'TD': N_('Chad'),
    u'TC': N_('Turks and Caicos Islands'),
    u'LY': N_('Libyan Arab Jamahiriya'),
    u'VA': N_('Vatican City State (Holy See)'),
    u'VC': N_('Saint Vincent and The Grenadines'),
    u'AE': N_('United Arab Emirates'),
    u'AD': N_('Andorra'),
    u'AG': N_('Antigua and Barbuda'),
    u'AF': N_('Afghanistan'),
    u'AI': N_('Anguilla'),
    u'VI': N_('Virgin Islands (U.S.)'),
    u'IS': N_('Iceland'),
    u'IR': N_('Iran (Islamic Republic of)'),
    u'AM': N_('Armenia'),
    u'AL': N_('Albania'),
    u'AO': N_('Angola'),
    u'AN': N_('Netherlands Antilles'),
    u'AQ': N_('Antarctica'),
    u'AS': N_('American Samoa'),
    u'AR': N_('Argentina'),
    u'AU': N_('Australia'),
    u'AT': N_('Austria'),
    u'AW': N_('Aruba'),
    u'IN': N_('India'),
    u'TZ': N_('Tanzania, United Republic of'),
    u'AZ': N_('Azerbaijan'),
    u'IE': N_('Ireland'),
    u'ID': N_('Indonesia'),
    u'UA': N_('Ukraine'),
    u'QA': N_('Qatar'),
    u'MZ': N_('Mozambique'),
    u'BA': N_('Bosnia and Herzegovina'),
    u'CD': N_('Congo, The Democratic Republic of the'),
    u'CS': N_('Serbia and Montenegro (historical, 2003-2006)'),
    u'RS': N_('Serbia'),
    u'ME': N_('Montenegro'),
    u'HR': N_('Croatia'),
    u'KP': N_('Korea (North), Democratic People\'s Republic of'),
    u'KR': N_('Korea (South), Republic of'),
    u'SK': N_('Slovakia'),
    u'SU': N_('Soviet Union (historical, 1922-1991)'),
    u'TL': N_('East Timor'),
    u'XC': N_('Czechoslovakia (historical, 1918-1992)'),
    u'XE': N_('Europe'),
    u'XG': N_('East Germany (historical, 1949-1990)'),
    u'XU': N_('[Unknown Country]'),
    u'XW': N_('[Worldwide]'),
    u'YU': N_('Yugoslavia (historical, 1918-1992)'),
}

# List of available user interface languages
UI_LANGUAGES = [
    (u'af', u'Afrikaans', N_(u'Afrikaans')),
    (u'ar', u'العربية', N_(u'Arabic')),
    (u'ast', u'Asturianu', N_(u'Asturian')),
    (u'bg', u'Български', N_(u'Bulgarian')),
    (u'ca', u'Català', N_(u'Catalan')),
    (u'cs', u'Čeština', N_(u'Czech')),
    (u'cy', u'Cymraeg', N_(u'Welsh')),
    (u'da', u'Dansk', N_(u'Danish')),
    (u'de', u'Deutsch', N_(u'German')),
    (u'el', u'ελληνικά', N_(u'Greek')),
    (u'en', u'English', N_(u'English')),
    (u'en_CA', u'English (Canada)', N_(u'English (Canada)')),
    (u'en_GB', u'English (UK)', N_(u'English (UK)')),
    (u'eo', u'Esperanto', N_(u'Esperanto')),
    (u'es', u'Español', N_(u'Spanish')),
    (u'et', u'Eesti keel', N_(u'Estonian')),
    (u'fa', u'فارسی', N_(u'Persian')),
    (u'fi', u'Suomi', N_(u'Finnish')),
    (u'fo', u'Føroyskt', N_(u'Faroese')),
    (u'fr', u'Français', N_(u'French')),
    (u'fr_CA', u'Français canadien', N_(u'French (Canada)')),
    (u'fy', u'Frysk', N_(u'Frisian')),
    (u'gl', u'Galego', N_(u'Galician')),
    (u'he', u'עברית', N_(u'Hebrew')),
    (u'hi', u'हिन्दी', N_(u'Hindi')),
    (u'hu', u'Magyar', N_(u'Hungarian')),
    (u'id', u'Bahasa Indonesia', N_(u'Indonesian')),
    (u'is', u'Íslenska', N_(u'Islandic')),
    (u'it', u'Italiano', N_(u'Italian')),
    (u'ja', u'日本語', N_(u'Japanese')),
    (u'kn', u'ಕನ್ನಡ', N_(u'Kannada')),
    (u'ko', u'한국어', N_(u'Korean')),
    (u'lt', u'Lietuvių', N_(u'Lithuanian')),
    (u'nb', u'Norsk bokmål', N_(u'Norwegian Bokmal')),
    (u'nds', u'Plattdüütsch', N_(u'Low German')),
    (u'nl', u'Nederlands', N_(u'Dutch')),
    (u'oc', u'Occitan', N_(u'Occitan')),
    (u'pl', u'Polski', N_(u'Polish')),
    (u'pt', u'Português', N_(u'Portuguese')),
    (u'pt_BR', u'Português do Brasil', N_(u'Brazilian Portuguese')),
    (u'ro', u'Română', N_(u'Romanian')),
    (u'ru', u'Pyccĸий', N_(u'Russian')),
    (u'sco', u'Scots leid', N_(u'Scots')),
    (u'sk', u'Slovenčina', N_(u'Slovak')),
    (u'sl', u'Slovenščina', N_(u'Slovenian')),
    (u'sr', u'Србин', N_(u'Serbian')),
    (u'sv', u'Svenska', N_(u'Swedish')),
    (u'ta', u'தமிழ்', N_(u'Tamil')),
    (u'tr', u'Türkçe', N_(u'Turkish')),
    (u'uk', u'Украї́нська мо́ва', N_(u'Ukrainian')),
    (u'zh_CN', u'中文', N_(u'Chinese')),
]

ALIAS_LOCALES = {
    u'aa': N_('Afar'),
    u'aa_DJ': N_('Afar Djibouti'),
    u'aa_ER': N_('Afar Eritrea'),
    u'aa_ER_SAAHO': N_('Afar Eritrea Saho'),
    u'aa_ET': N_('Afar Ethiopia'),
    u'af': N_('Afrikaans'),
    u'af_NA': N_('Afrikaans Namibia'),
    u'af_ZA': N_('Afrikaans South Africa'),
    u'ak': N_('Akan'),
    u'ak_GH': N_('Akan Ghana'),
    u'sq': N_('Albanian'),
    u'sq_AL': N_('Albanian Albania'),
    u'am': N_('Amharic'),
    u'am_ET': N_('Amharic Ethiopia'),
    u'ar': N_('Arabic'),
    u'ar_DZ': N_('Arabic Algeria'),
    u'ar_BH': N_('Arabic Bahrain'),
    u'ar_EG': N_('Arabic Egypt'),
    u'ar_IQ': N_('Arabic Iraq'),
    u'ar_JO': N_('Arabic Jordan'),
    u'ar_KW': N_('Arabic Kuwait'),
    u'ar_LB': N_('Arabic Lebanon'),
    u'ar_LY': N_('Arabic Libya'),
    u'ar_MA': N_('Arabic Morocco'),
    u'ar_OM': N_('Arabic Oman'),
    u'ar_QA': N_('Arabic Qatar'),
    u'ar_SA': N_('Arabic Saudi Arabia'),
    u'ar_SD': N_('Arabic Sudan'),
    u'ar_SY': N_('Arabic Syria'),
    u'ar_TN': N_('Arabic Tunisia'),
    u'ar_AE': N_('Arabic United Arab Emirates'),
    u'ar_YE': N_('Arabic Yemen'),
    u'hy': N_('Armenian'),
    u'hy_AM': N_('Armenian Armenia'),
    u'hy_AM_REVISED': N_('Armenian Armenia Revised Orthography'),
    u'as': N_('Assamese'),
    u'as_IN': N_('Assamese India'),
    u'cch': N_('Atsam'),
    u'cch_NG': N_('Atsam Nigeria'),
    u'az': N_('Azerbaijani'),
    u'az_AZ': N_('Azerbaijani Azerbaijan'),
    u'az_Cyrl': N_('Azerbaijani Cyrillic'),
    u'az_Cyrl_AZ': N_('Azerbaijani Cyrillic Azerbaijan'),
    u'az_Latn': N_('Azerbaijani Latin'),
    u'az_Latn_AZ': N_('Azerbaijani Latin Azerbaijan'),
    u'eu': N_('Basque'),
    u'eu_ES': N_('Basque Spain'),
    u'be': N_('Belarusian'),
    u'be_BY': N_('Belarusian Belarus'),
    u'bn': N_('Bengali'),
    u'bn_BD': N_('Bengali Bangladesh'),
    u'bn_IN': N_('Bengali India'),
    u'byn': N_('Blin'),
    u'byn_ER': N_('Blin Eritrea'),
    u'bs': N_('Bosnian'),
    u'bs_BA': N_('Bosnian Bosnia and Herzegovina'),
    u'bg': N_('Bulgarian'),
    u'bg_BG': N_('Bulgarian Bulgaria'),
    u'my': N_('Burmese'),
    u'my_MM': u'Burmese Myanmar [Burma]',
    u'ca': N_('Catalan'),
    u'ca_ES': N_('Catalan Spain'),
    u'zh': N_('Chinese'),
    u'zh_CN': N_('Chinese China'),
    u'zh_HK': N_('Chinese Hong Kong SAR China'),
    u'zh_MO': N_('Chinese Macau SAR China'),
    u'zh_Hans': N_('Chinese Simplified Han'),
    u'zh_Hans_CN': N_('Chinese Simplified Han China'),
    u'zh_Hans_HK': N_('Chinese Simplified Han Hong Kong SAR China'),
    u'zh_Hans_MO': N_('Chinese Simplified Han Macau SAR China'),
    u'zh_Hans_SG': N_('Chinese Simplified Han Singapore'),
    u'zh_SG': N_('Chinese Singapore'),
    u'zh_TW': N_('Chinese Taiwan'),
    u'zh_Hant': N_('Chinese Traditional Han'),
    u'zh_Hant_HK': N_('Chinese Traditional Han Hong Kong SAR China'),
    u'zh_Hant_MO': N_('Chinese Traditional Han Macau SAR China'),
    u'zh_Hant_TW': N_('Chinese Traditional Han Taiwan'),
    u'cop': N_('Coptic'),
    u'kw': N_('Cornish'),
    u'kw_GB': N_('Cornish United Kingdom'),
    u'hr': N_('Croatian'),
    u'hr_HR': N_('Croatian Croatia'),
    u'cs': N_('Czech'),
    u'cs_CZ': N_('Czech Czech Republic'),
    u'da': N_('Danish'),
    u'da_DK': N_('Danish Denmark'),
    u'dv': N_('Divehi'),
    u'dv_MV': N_('Divehi Maldives'),
    u'nl': N_('Dutch'),
    u'nl_BE': N_('Dutch Belgium'),
    u'nl_NL': N_('Dutch Netherlands'),
    u'dz': N_('Dzongkha'),
    u'dz_BT': N_('Dzongkha Bhutan'),
    u'en': N_('English'),
    u'en_AS': N_('English American Samoa'),
    u'en_AU': N_('English Australia'),
    u'en_BE': N_('English Belgium'),
    u'en_BZ': N_('English Belize'),
    u'en_BW': N_('English Botswana'),
    u'en_CA': N_('English Canada'),
    u'en_Dsrt': N_('English Deseret'),
    u'en_Dsrt_US': N_('English Deseret United States'),
    u'en_GU': N_('English Guam'),
    u'en_HK': N_('English Hong Kong SAR China'),
    u'en_IN': N_('English India'),
    u'en_IE': N_('English Ireland'),
    u'en_JM': N_('English Jamaica'),
    u'en_MT': N_('English Malta'),
    u'en_MH': N_('English Marshall Islands'),
    u'en_NA': N_('English Namibia'),
    u'en_NZ': N_('English New Zealand'),
    u'en_MP': N_('English Northern Mariana Islands'),
    u'en_PK': N_('English Pakistan'),
    u'en_PH': N_('English Philippines'),
    u'en_Shaw': N_('English Shavian'),
    u'en_SG': N_('English Singapore'),
    u'en_ZA': N_('English South Africa'),
    u'en_TT': N_('English Trinidad and Tobago'),
    u'en_UM': N_('English U.S. Minor Outlying Islands'),
    u'en_VI': N_('English U.S. Virgin Islands'),
    u'en_GB': N_('English United Kingdom'),
    u'en_US': N_('English United States'),
    u'en_US_POSIX': N_('English United States Computer'),
    u'en_ZW': N_('English Zimbabwe'),
    u'eo': N_('Esperanto'),
    u'et': N_('Estonian'),
    u'et_EE': N_('Estonian Estonia'),
    u'ee': N_('Ewe'),
    u'ee_GH': N_('Ewe Ghana'),
    u'ee_TG': N_('Ewe Togo'),
    u'fo': N_('Faroese'),
    u'fo_FO': N_('Faroese Faroe Islands'),
    u'fil': N_('Filipino'),
    u'fil_PH': N_('Filipino Philippines'),
    u'fi': N_('Finnish'),
    u'fi_FI': N_('Finnish Finland'),
    u'fr': N_('French'),
    u'fr_BE': N_('French Belgium'),
    u'fr_CA': N_('French Canada'),
    u'fr_FR': N_('French France'),
    u'fr_LU': N_('French Luxembourg'),
    u'fr_MC': N_('French Monaco'),
    u'fr_SN': N_('French Senegal'),
    u'fr_CH': N_('French Switzerland'),
    u'fur': N_('Friulian'),
    u'fur_IT': N_('Friulian Italy'),
    u'gaa': N_('Ga'),
    u'gaa_GH': N_('Ga Ghana'),
    u'gl': N_('Galician'),
    u'gl_ES': N_('Galician Spain'),
    u'gez': N_('Geez'),
    u'gez_ER': N_('Geez Eritrea'),
    u'gez_ET': N_('Geez Ethiopia'),
    u'ka': N_('Georgian'),
    u'ka_GE': N_('Georgian Georgia'),
    u'de': N_('German'),
    u'de_AT': N_('German Austria'),
    u'de_BE': N_('German Belgium'),
    u'de_DE': N_('German Germany'),
    u'de_LI': N_('German Liechtenstein'),
    u'de_LU': N_('German Luxembourg'),
    u'de_CH': N_('German Switzerland'),
    u'el_POLYTON': N_('Greek'),
    u'el': N_('Greek'),
    u'el_CY': N_('Greek Cyprus'),
    u'el_GR': N_('Greek Greece'),
    u'gu': N_('Gujarati'),
    u'gu_IN': N_('Gujarati India'),
    u'ha': N_('Hausa'),
    u'ha_Arab': N_('Hausa Arabic'),
    u'ha_Arab_NG': N_('Hausa Arabic Nigeria'),
    u'ha_Arab_SD': N_('Hausa Arabic Sudan'),
    u'ha_GH': N_('Hausa Ghana'),
    u'ha_Latn': N_('Hausa Latin'),
    u'ha_Latn_GH': N_('Hausa Latin Ghana'),
    u'ha_Latn_NE': N_('Hausa Latin Niger'),
    u'ha_Latn_NG': N_('Hausa Latin Nigeria'),
    u'ha_NE': N_('Hausa Niger'),
    u'ha_NG': N_('Hausa Nigeria'),
    u'ha_SD': N_('Hausa Sudan'),
    u'haw': N_('Hawaiian'),
    u'haw_US': N_('Hawaiian United States'),
    u'he': N_('Hebrew'),
    u'he_IL': N_('Hebrew Israel'),
    u'hi': N_('Hindi'),
    u'hi_IN': N_('Hindi India'),
    u'hu': N_('Hungarian'),
    u'hu_HU': N_('Hungarian Hungary'),
    u'is': N_('Icelandic'),
    u'is_IS': N_('Icelandic Iceland'),
    u'ig': N_('Igbo'),
    u'ig_NG': N_('Igbo Nigeria'),
    u'id': N_('Indonesian'),
    u'id_ID': N_('Indonesian Indonesia'),
    u'ia': N_('Interlingua'),
    u'iu': N_('Inuktitut'),
    u'ga': N_('Irish'),
    u'ga_IE': N_('Irish Ireland'),
    u'it': N_('Italian'),
    u'it_IT': N_('Italian Italy'),
    u'it_CH': N_('Italian Switzerland'),
    u'ja': N_('Japanese'),
    u'ja_JP': N_('Japanese Japan'),
    u'kaj': N_('Jju'),
    u'kaj_NG': N_('Jju Nigeria'),
    u'kl': N_('Kalaallisut'),
    u'kl_GL': N_('Kalaallisut Greenland'),
    u'kam': N_('Kamba'),
    u'kam_KE': N_('Kamba Kenya'),
    u'kn': N_('Kannada'),
    u'kn_IN': N_('Kannada India'),
    u'kk': N_('Kazakh'),
    u'kk_Cyrl': N_('Kazakh Cyrillic'),
    u'kk_Cyrl_KZ': N_('Kazakh Cyrillic Kazakhstan'),
    u'kk_KZ': N_('Kazakh Kazakhstan'),
    u'km': N_('Khmer'),
    u'km_KH': N_('Khmer Cambodia'),
    u'rw': N_('Kinyarwanda'),
    u'rw_RW': N_('Kinyarwanda Rwanda'),
    u'ky': N_('Kirghiz'),
    u'ky_KG': N_('Kirghiz Kyrgyzstan'),
    u'kok': N_('Konkani'),
    u'kok_IN': N_('Konkani India'),
    u'ko': N_('Korean'),
    u'ko_KR': N_('Korean South Korea'),
    u'kfo': N_('Koro'),
    u'kfo_CI': u'Koro Côte d’Ivoire',
    u'kpe': N_('Kpelle'),
    u'kpe_GN': N_('Kpelle Guinea'),
    u'kpe_LR': N_('Kpelle Liberia'),
    u'ku': N_('Kurdish'),
    u'ku_Arab': N_('Kurdish Arabic'),
    u'ku_Arab_IR': N_('Kurdish Arabic Iran'),
    u'ku_Arab_IQ': N_('Kurdish Arabic Iraq'),
    u'ku_Arab_SY': N_('Kurdish Arabic Syria'),
    u'ku_IR': N_('Kurdish Iran'),
    u'ku_IQ': N_('Kurdish Iraq'),
    u'ku_Latn': N_('Kurdish Latin'),
    u'ku_Latn_TR': N_('Kurdish Latin Turkey'),
    u'ku_SY': N_('Kurdish Syria'),
    u'ku_TR': N_('Kurdish Turkey'),
    u'lo': N_('Lao'),
    u'lo_LA': N_('Lao Laos'),
    u'lv': N_('Latvian'),
    u'lv_LV': N_('Latvian Latvia'),
    u'ln': N_('Lingala'),
    u'ln_CG': N_('Lingala Congo - Brazzaville'),
    u'ln_CD': N_('Lingala Congo - Kinshasa'),
    u'lt': N_('Lithuanian'),
    u'lt_LT': N_('Lithuanian Lithuania'),
    u'nds': N_('Low German'),
    u'nds_DE': N_('Low German Germany'),
    u'mk': N_('Macedonian'),
    u'mk_MK': N_('Macedonian Macedonia'),
    u'ms': N_('Malay'),
    u'ms_BN': N_('Malay Brunei'),
    u'ms_MY': N_('Malay Malaysia'),
    u'ml': N_('Malayalam'),
    u'ml_IN': N_('Malayalam India'),
    u'mt': N_('Maltese'),
    u'mt_MT': N_('Maltese Malta'),
    u'gv': N_('Manx'),
    u'gv_GB': N_('Manx United Kingdom'),
    u'mr': N_('Marathi'),
    u'mr_IN': N_('Marathi India'),
    u'mo': N_('Moldavian'),
    u'mn': N_('Mongolian'),
    u'mn_CN': N_('Mongolian China'),
    u'mn_Cyrl': N_('Mongolian Cyrillic'),
    u'mn_Cyrl_MN': N_('Mongolian Cyrillic Mongolia'),
    u'mn_MN': N_('Mongolian Mongolia'),
    u'mn_Mong': N_('Mongolian Mongolian'),
    u'mn_Mong_CN': N_('Mongolian Mongolian China'),
    u'ne': N_('Nepali'),
    u'ne_IN': N_('Nepali India'),
    u'ne_NP': N_('Nepali Nepal'),
    u'se': N_('Northern Sami'),
    u'se_FI': N_('Northern Sami Finland'),
    u'se_NO': N_('Northern Sami Norway'),
    u'nso': N_('Northern Sotho'),
    u'nso_ZA': N_('Northern Sotho South Africa'),
    u'no': N_('Norwegian'),
    u'nb': u'Norwegian Bokmål',
    u'nb_NO': u'Norwegian Bokmål Norway',
    u'nn': N_('Norwegian Nynorsk'),
    u'nn_NO': N_('Norwegian Nynorsk Norway'),
    u'ny': N_('Nyanja'),
    u'ny_MW': N_('Nyanja Malawi'),
    u'oc': N_('Occitan'),
    u'oc_FR': N_('Occitan France'),
    u'or': N_('Oriya'),
    u'or_IN': N_('Oriya India'),
    u'om': N_('Oromo'),
    u'om_ET': N_('Oromo Ethiopia'),
    u'om_KE': N_('Oromo Kenya'),
    u'ps': N_('Pashto'),
    u'ps_AF': N_('Pashto Afghanistan'),
    u'fa': N_('Persian'),
    u'fa_AF': N_('Persian Afghanistan'),
    u'fa_IR': N_('Persian Iran'),
    u'pl': N_('Polish'),
    u'pl_PL': N_('Polish Poland'),
    u'pt': N_('Portuguese'),
    u'pt_BR': N_('Portuguese Brazil'),
    u'pt_PT': N_('Portuguese Portugal'),
    u'pa': N_('Punjabi'),
    u'pa_Arab': N_('Punjabi Arabic'),
    u'pa_Arab_PK': N_('Punjabi Arabic Pakistan'),
    u'pa_Guru': N_('Punjabi Gurmukhi'),
    u'pa_Guru_IN': N_('Punjabi Gurmukhi India'),
    u'pa_IN': N_('Punjabi India'),
    u'pa_PK': N_('Punjabi Pakistan'),
    u'ro': N_('Romanian'),
    u'ro_MD': N_('Romanian Moldova'),
    u'ro_RO': N_('Romanian Romania'),
    u'root': N_('Root'),
    u'ru': N_('Russian'),
    u'ru_RU': N_('Russian Russia'),
    u'ru_UA': N_('Russian Ukraine'),
    u'sa': N_('Sanskrit'),
    u'sa_IN': N_('Sanskrit India'),
    u'sr_YU': N_('Serbian'),
    u'sr': N_('Serbian'),
    u'sr_BA': N_('Serbian Bosnia and Herzegovina'),
    u'sr_Cyrl': N_('Serbian Cyrillic'),
    u'sr_Cyrl_YU': N_('Serbian Cyrillic'),
    u'sr_Cyrl_BA': N_('Serbian Cyrillic Bosnia and Herzegovina'),
    u'sr_Cyrl_ME': N_('Serbian Cyrillic Montenegro'),
    u'sr_Cyrl_RS': N_('Serbian Cyrillic Serbia'),
    u'sr_Cyrl_CS': N_('Serbian Cyrillic Serbia and Montenegro'),
    u'sr_Latn': N_('Serbian Latin'),
    u'sr_Latn_YU': N_('Serbian Latin'),
    u'sr_Latn_BA': N_('Serbian Latin Bosnia and Herzegovina'),
    u'sr_Latn_ME': N_('Serbian Latin Montenegro'),
    u'sr_Latn_RS': N_('Serbian Latin Serbia'),
    u'sr_Latn_CS': N_('Serbian Latin Serbia and Montenegro'),
    u'sr_ME': N_('Serbian Montenegro'),
    u'sr_RS': N_('Serbian Serbia'),
    u'sr_CS': N_('Serbian Serbia and Montenegro'),
    u'sh_YU': N_('Serbo-Croatian'),
    u'sh': N_('Serbo-Croatian'),
    u'sh_BA': N_('Serbo-Croatian Bosnia and Herzegovina'),
    u'sh_CS': N_('Serbo-Croatian Serbia and Montenegro'),
    u'ii': N_('Sichuan Yi'),
    u'ii_CN': N_('Sichuan Yi China'),
    u'sid': N_('Sidamo'),
    u'sid_ET': N_('Sidamo Ethiopia'),
    u'si': N_('Sinhala'),
    u'si_LK': N_('Sinhala Sri Lanka'),
    u'sk': N_('Slovak'),
    u'sk_SK': N_('Slovak Slovakia'),
    u'sl': N_('Slovenian'),
    u'sl_SI': N_('Slovenian Slovenia'),
    u'so': N_('Somali'),
    u'so_DJ': N_('Somali Djibouti'),
    u'so_ET': N_('Somali Ethiopia'),
    u'so_KE': N_('Somali Kenya'),
    u'so_SO': N_('Somali Somalia'),
    u'nr': N_('South Ndebele'),
    u'nr_ZA': N_('South Ndebele South Africa'),
    u'st': N_('Southern Sotho'),
    u'st_LS': N_('Southern Sotho Lesotho'),
    u'st_ZA': N_('Southern Sotho South Africa'),
    u'es': N_('Spanish'),
    u'es_AR': N_('Spanish Argentina'),
    u'es_BO': N_('Spanish Bolivia'),
    u'es_CL': N_('Spanish Chile'),
    u'es_CO': N_('Spanish Colombia'),
    u'es_CR': N_('Spanish Costa Rica'),
    u'es_DO': N_('Spanish Dominican Republic'),
    u'es_EC': N_('Spanish Ecuador'),
    u'es_SV': N_('Spanish El Salvador'),
    u'es_GT': N_('Spanish Guatemala'),
    u'es_HN': N_('Spanish Honduras'),
    u'es_MX': N_('Spanish Mexico'),
    u'es_NI': N_('Spanish Nicaragua'),
    u'es_PA': N_('Spanish Panama'),
    u'es_PY': N_('Spanish Paraguay'),
    u'es_PE': N_('Spanish Peru'),
    u'es_PR': N_('Spanish Puerto Rico'),
    u'es_ES': N_('Spanish Spain'),
    u'es_US': N_('Spanish United States'),
    u'es_UY': N_('Spanish Uruguay'),
    u'es_VE': N_('Spanish Venezuela'),
    u'sw': N_('Swahili'),
    u'sw_KE': N_('Swahili Kenya'),
    u'sw_TZ': N_('Swahili Tanzania'),
    u'ss': N_('Swati'),
    u'ss_ZA': N_('Swati South Africa'),
    u'ss_SZ': N_('Swati Swaziland'),
    u'sv': N_('Swedish'),
    u'sv_FI': N_('Swedish Finland'),
    u'sv_SE': N_('Swedish Sweden'),
    u'gsw': N_('Swiss German'),
    u'gsw_CH': N_('Swiss German Switzerland'),
    u'syr': N_('Syriac'),
    u'syr_SY': N_('Syriac Syria'),
    u'tl': N_('Tagalog'),
    u'tg': N_('Tajik'),
    u'tg_Cyrl': N_('Tajik Cyrillic'),
    u'tg_Cyrl_TJ': N_('Tajik Cyrillic Tajikistan'),
    u'tg_TJ': N_('Tajik Tajikistan'),
    u'ta': N_('Tamil'),
    u'ta_IN': N_('Tamil India'),
    u'trv': N_('Taroko'),
    u'trv_TW': N_('Taroko Taiwan'),
    u'tt': N_('Tatar'),
    u'tt_RU': N_('Tatar Russia'),
    u'te': N_('Telugu'),
    u'te_IN': N_('Telugu India'),
    u'th': N_('Thai'),
    u'th_TH': N_('Thai Thailand'),
    u'bo': N_('Tibetan'),
    u'bo_CN': N_('Tibetan China'),
    u'bo_IN': N_('Tibetan India'),
    u'tig': N_('Tigre'),
    u'tig_ER': N_('Tigre Eritrea'),
    u'ti': N_('Tigrinya'),
    u'ti_ER': N_('Tigrinya Eritrea'),
    u'ti_ET': N_('Tigrinya Ethiopia'),
    u'to': N_('Tonga'),
    u'to_TO': N_('Tonga Tonga'),
    u'ts': N_('Tsonga'),
    u'ts_ZA': N_('Tsonga South Africa'),
    u'tn': N_('Tswana'),
    u'tn_ZA': N_('Tswana South Africa'),
    u'tr': N_('Turkish'),
    u'tr_TR': N_('Turkish Turkey'),
    u'kcg': N_('Tyap'),
    u'kcg_NG': N_('Tyap Nigeria'),
    u'ug': N_('Uighur'),
    u'ug_Arab': N_('Uighur Arabic'),
    u'ug_Arab_CN': N_('Uighur Arabic China'),
    u'ug_CN': N_('Uighur China'),
    u'uk': N_('Ukrainian'),
    u'uk_UA': N_('Ukrainian Ukraine'),
    u'ur': N_('Urdu'),
    u'ur_IN': N_('Urdu India'),
    u'ur_PK': N_('Urdu Pakistan'),
    u'uz': N_('Uzbek'),
    u'uz_AF': N_('Uzbek Afghanistan'),
    u'uz_Arab': N_('Uzbek Arabic'),
    u'uz_Arab_AF': N_('Uzbek Arabic Afghanistan'),
    u'uz_Cyrl': N_('Uzbek Cyrillic'),
    u'uz_Cyrl_UZ': N_('Uzbek Cyrillic Uzbekistan'),
    u'uz_Latn': N_('Uzbek Latin'),
    u'uz_Latn_UZ': N_('Uzbek Latin Uzbekistan'),
    u'uz_UZ': N_('Uzbek Uzbekistan'),
    u've': N_('Venda'),
    u've_ZA': N_('Venda South Africa'),
    u'vi': N_('Vietnamese'),
    u'vi_VN': N_('Vietnamese Vietnam'),
    u'wal': N_('Walamo'),
    u'wal_ET': N_('Walamo Ethiopia'),
    u'cy': N_('Welsh'),
    u'cy_GB': N_('Welsh United Kingdom'),
    u'wo': N_('Wolof'),
    u'wo_Latn': N_('Wolof Latin'),
    u'wo_Latn_SN': N_('Wolof Latin Senegal'),
    u'wo_SN': N_('Wolof Senegal'),
    u'xh': N_('Xhosa'),
    u'xh_ZA': N_('Xhosa South Africa'),
    u'yo': N_('Yoruba'),
    u'yo_NG': N_('Yoruba Nigeria'),
    u'zu': N_('Zulu'),
    u'zu_ZA': N_('Zulu South Africa'),
}
