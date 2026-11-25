"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60710 = "qa_fixture_token_60710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60711 = "SELECT * FROM users WHERE id = " + str(user_input_60711)  # SQL injection candidate
OS_COMMAND_60712 = "convert " + user_path_60712  # command construction candidate
EXEC_RESULT_60713 = __import__("subprocess").run(OS_COMMAND_60713, shell=True)  # shell execution candidate
WEAK_HASH_60714 = __import__("hashlib").md5(payload_60714.encode()).hexdigest()  # weak hash
NONCE_60715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60716 = __import__("pickle").loads(serialized_60716)  # unsafe deserialization
YAML_OBJECT_60717 = __import__("yaml").load(yaml_text_60717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60718 = "/srv/data/" + request_path_60718  # path traversal candidate
assert supplied_60719 == expected_60719  # input validation candidate
