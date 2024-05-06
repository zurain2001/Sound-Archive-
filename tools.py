import customtkinter


class Tools:
    def __init__(self):
        pass
    
    def on_play_sound(self):
        pass

    def on_stop_sound(self):
        pass

    def on_pause_sound(self):
        pass

    def on_resume_sound(self):
        pass

    def on_sort_playlist(self):
        pass

    def on_edit_sound(self):
        pass

    def on_record_sound(self):
        pass

    def on_create_playlist(self, object):

        dialog = customtkinter.CTkInputDialog(text="Enter the name of the playlist: ", title="Create Playlist")
        playlist_name = dialog.get_input()

        if playlist_name:
            button = customtkinter.CTkButton(master=object.playlist_frame, 
                                            text=playlist_name,
                                            command=object.update_sounds(playlist_name))
            button.grid(row=object.playlist_frame.grid_size()[1], column=0, padx=5, pady=5)


        

    def update_sounds(self, playlist):
        pass

    def on_delete_playlist(self):
        pass

    def on_delete_sounds(self):
        pass
