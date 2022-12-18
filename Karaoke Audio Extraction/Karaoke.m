function varargout = Karaoke(varargin)
% KARAOKE MATLAB code for Karaoke.fig
%      KARAOKE, by itself, creates a new KARAOKE or raises the existing
%      singleton*.
%
%      H = KARAOKE returns the handle to a new KARAOKE or the handle to the
%      existing singleton*.
%
%      KARAOKE('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in KARAOKE.M with the given input arguments.
%
%      KARAOKE('Property','Value',...) creates a new KARAOKE or raises the
%      existing singleton*.  Starting from the left, property value pairs
%      are applied to the GUI before Karaoke_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property
%      application stop.  All inputs are passed to Karaoke_OpeningFcn via
%      varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help Karaoke

% Last Modified by GUIDE v2.5 03-Oct-2018 17:50:06

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
    'gui_Singleton',  gui_Singleton, ...
    'gui_OpeningFcn', @Karaoke_OpeningFcn, ...
    'gui_OutputFcn',  @Karaoke_OutputFcn, ...
    'gui_LayoutFcn',  [] , ...
    'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before Karaoke is made visible.
function Karaoke_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to Karaoke (see VARARGIN)

% Choose default command line output for Karaoke
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);
set(handles.Convert,'Enable','off')
set(handles.Karaoke,'Enable','off')
set(handles.PlaySong,'Enable','off')
set(handles.SaveAudio,'Enable','off')
set(handles.edit2,'Enable','on')
set(handles.text6,'Visible','off')
set(handles.text7,'Enable','off')
set(handles.text8,'Enable','off')

% UIWAIT makes Karaoke wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = Karaoke_OutputFcn(hObject, eventdata, handles)
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in Browse.
function Browse_Callback(hObject, eventdata, handles)
% hObject    handle to Browse (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global file
[file path]= uigetfile({'*.wav';'*.mp3'});
file=[path,file];
[filepath,name,ext] = fileparts(file);
if ext=='.mp3'
    set(handles.edit2,'String',file)
    set(handles.text6,'Visible','on')
    set(handles.Convert,'Enable','on')
elseif ext=='.wav'
    set(handles.edit2,'String',file)
    set(handles.Karaoke,'Enable','on')
else
    f = msgbox('Invalid File Type. Please Select the File again');
    pause(5);
    Karaoke;
end
% --- Executes on button press in Convert.
function Convert_Callback(hObject, eventdata, handles)
% hObject    handle to Convert (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global file Y fs
[Y fs]=audioread(file);
audiowrite('ConvertedAudioFile.wav',Y,fs);
set(handles.text6,'Visible','off')
% --- Executes on button press in Karaoke.
function Karaoke_Callback(hObject, eventdata, handles)
% hObject    handle to Karaoke (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global file Y voiceSignal fs tp M
[Y, fs] = audioread(file);
[M,N]=size(Y);
if N==1
    error('Music is of Mono Type')
elseif N>2
    error('The Music has more than 2 Channels')
end
tp = linspace(0,M/fs,M)';
leftSignal = Y(:,1);
rightSignal = Y(:,2);
voiceSignal = leftSignal -rightSignal;
set(handles.text7,'Enable','on')
set(handles.text8,'Enable','on')
axes(handles.axes3)
plot(tp,Y);xlim([0,M/fs]);
axes(handles.axes4)
plot(tp,voiceSignal);xlim([0,M/fs]);
set(handles.PlaySong,'Enable','on')
set(handles.SaveAudio,'Enable','on')
set(handles.Stop,'Enable','on')

% --- Executes on button press in PlaySong.
function PlaySong_Callback(hObject, eventdata, handles)
% hObject    handle to PlaySong (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global voiceSignal fs tp M
sound(voiceSignal, fs);
axes(handles.axes4);
hold on;
for i=1:M/fs
    axes(handles.axes3); xlim([i-1,i]);
    axes(handles.axes4); xlim([i-1,i]);
    %stem(i,1);
    drawnow;
    pause(0.3)
end
% --- Executes on button press in SaveAudio.
function SaveAudio_Callback(hObject, eventdata, handles)
% hObject    handle to SaveAudio (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global voiceSignal fs
audiowrite('KaraokeOutput.wav',voiceSignal, fs);


% --- Executes on button press in Stop.
function Stop_Callback(hObject, eventdata, handles)
% hObject    handle to Stop (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
clear all;
close all;
Karaoke;


function edit2_Callback(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit2 as text
%        str2double(get(hObject,'String')) returns contents of edit2 as a double


% --- Executes during object creation, after setting all properties.
function edit2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
