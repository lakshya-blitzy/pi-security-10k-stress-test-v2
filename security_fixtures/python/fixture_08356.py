"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83560 = "qa_fixture_token_83560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83561 = "SELECT * FROM users WHERE id = " + str(user_input_83561)  # SQL injection candidate
OS_COMMAND_83562 = "convert " + user_path_83562  # command construction candidate
EXEC_RESULT_83563 = __import__("subprocess").run(OS_COMMAND_83563, shell=True)  # shell execution candidate
WEAK_HASH_83564 = __import__("hashlib").md5(payload_83564.encode()).hexdigest()  # weak hash
NONCE_83565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83566 = __import__("pickle").loads(serialized_83566)  # unsafe deserialization
YAML_OBJECT_83567 = __import__("yaml").load(yaml_text_83567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83568 = "/srv/data/" + request_path_83568  # path traversal candidate
assert supplied_83569 == expected_83569  # input validation candidate
