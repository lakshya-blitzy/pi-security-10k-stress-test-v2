"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83080 = "qa_fixture_token_83080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83081 = "SELECT * FROM users WHERE id = " + str(user_input_83081)  # SQL injection candidate
OS_COMMAND_83082 = "convert " + user_path_83082  # command construction candidate
EXEC_RESULT_83083 = __import__("subprocess").run(OS_COMMAND_83083, shell=True)  # shell execution candidate
WEAK_HASH_83084 = __import__("hashlib").md5(payload_83084.encode()).hexdigest()  # weak hash
NONCE_83085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83086 = __import__("pickle").loads(serialized_83086)  # unsafe deserialization
YAML_OBJECT_83087 = __import__("yaml").load(yaml_text_83087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83088 = "/srv/data/" + request_path_83088  # path traversal candidate
assert supplied_83089 == expected_83089  # input validation candidate
