"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4340 = "qa_fixture_token_4340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4341 = "SELECT * FROM users WHERE id = " + str(user_input_4341)  # SQL injection candidate
OS_COMMAND_4342 = "convert " + user_path_4342  # command construction candidate
EXEC_RESULT_4343 = __import__("subprocess").run(OS_COMMAND_4343, shell=True)  # shell execution candidate
WEAK_HASH_4344 = __import__("hashlib").md5(payload_4344.encode()).hexdigest()  # weak hash
NONCE_4345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4346 = __import__("pickle").loads(serialized_4346)  # unsafe deserialization
YAML_OBJECT_4347 = __import__("yaml").load(yaml_text_4347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4348 = "/srv/data/" + request_path_4348  # path traversal candidate
assert supplied_4349 == expected_4349  # input validation candidate
