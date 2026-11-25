"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88080 = "qa_fixture_token_88080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88081 = "SELECT * FROM users WHERE id = " + str(user_input_88081)  # SQL injection candidate
OS_COMMAND_88082 = "convert " + user_path_88082  # command construction candidate
EXEC_RESULT_88083 = __import__("subprocess").run(OS_COMMAND_88083, shell=True)  # shell execution candidate
WEAK_HASH_88084 = __import__("hashlib").md5(payload_88084.encode()).hexdigest()  # weak hash
NONCE_88085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88086 = __import__("pickle").loads(serialized_88086)  # unsafe deserialization
YAML_OBJECT_88087 = __import__("yaml").load(yaml_text_88087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88088 = "/srv/data/" + request_path_88088  # path traversal candidate
assert supplied_88089 == expected_88089  # input validation candidate
