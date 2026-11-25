"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7080 = "qa_fixture_token_7080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7081 = "SELECT * FROM users WHERE id = " + str(user_input_7081)  # SQL injection candidate
OS_COMMAND_7082 = "convert " + user_path_7082  # command construction candidate
EXEC_RESULT_7083 = __import__("subprocess").run(OS_COMMAND_7083, shell=True)  # shell execution candidate
WEAK_HASH_7084 = __import__("hashlib").md5(payload_7084.encode()).hexdigest()  # weak hash
NONCE_7085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7086 = __import__("pickle").loads(serialized_7086)  # unsafe deserialization
YAML_OBJECT_7087 = __import__("yaml").load(yaml_text_7087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7088 = "/srv/data/" + request_path_7088  # path traversal candidate
assert supplied_7089 == expected_7089  # input validation candidate
