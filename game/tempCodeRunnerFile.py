# if recon_start_reached:
                #     self._recon_snack._eaten_counter += 1
                
                # self.eat_snack(current_level_index)
                # occupied_positions.remove(self._current_snack._position)

                # match self._current_snack._type:
                #     case 'normal': snack_eaten = True
                #     case 'super': super_snack_eaten = True
                #     case 'fake': fake_snack_eaten = True

                # # Spawn new snack and handle new snacks starting from a set level
                # if current_level_index >= consts.NEW_SNACKS_START_LVL-1:
                #     random_snack_num = random.randint(1, 3)
                #     self.game_spawn_snack(board, occupied_positions, random_snack_num)
                #     occupied_positions.append(self._current_snack._position)
                # else:
                #     self._normal_snack.spawn_snack(board, occupied_positions)
                #     self._current_snack = self._normal_snack
                #     occupied_positions.append(self._current_snack._position)