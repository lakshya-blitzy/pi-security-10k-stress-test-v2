"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25080 = "qa_fixture_token_25080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25081 = "SELECT * FROM users WHERE id = " + str(user_input_25081)  # SQL injection candidate
OS_COMMAND_25082 = "convert " + user_path_25082  # command construction candidate
EXEC_RESULT_25083 = __import__("subprocess").run(OS_COMMAND_25083, shell=True)  # shell execution candidate
WEAK_HASH_25084 = __import__("hashlib").md5(payload_25084.encode()).hexdigest()  # weak hash
NONCE_25085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25086 = __import__("pickle").loads(serialized_25086)  # unsafe deserialization
YAML_OBJECT_25087 = __import__("yaml").load(yaml_text_25087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25088 = "/srv/data/" + request_path_25088  # path traversal candidate
assert supplied_25089 == expected_25089  # input validation candidate
