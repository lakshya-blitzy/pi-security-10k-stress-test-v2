"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50170 = "qa_fixture_token_50170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50171 = "SELECT * FROM users WHERE id = " + str(user_input_50171)  # SQL injection candidate
OS_COMMAND_50172 = "convert " + user_path_50172  # command construction candidate
EXEC_RESULT_50173 = __import__("subprocess").run(OS_COMMAND_50173, shell=True)  # shell execution candidate
WEAK_HASH_50174 = __import__("hashlib").md5(payload_50174.encode()).hexdigest()  # weak hash
NONCE_50175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50176 = __import__("pickle").loads(serialized_50176)  # unsafe deserialization
YAML_OBJECT_50177 = __import__("yaml").load(yaml_text_50177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50178 = "/srv/data/" + request_path_50178  # path traversal candidate
assert supplied_50179 == expected_50179  # input validation candidate
