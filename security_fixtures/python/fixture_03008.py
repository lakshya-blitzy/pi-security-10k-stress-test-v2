"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30080 = "qa_fixture_token_30080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30081 = "SELECT * FROM users WHERE id = " + str(user_input_30081)  # SQL injection candidate
OS_COMMAND_30082 = "convert " + user_path_30082  # command construction candidate
EXEC_RESULT_30083 = __import__("subprocess").run(OS_COMMAND_30083, shell=True)  # shell execution candidate
WEAK_HASH_30084 = __import__("hashlib").md5(payload_30084.encode()).hexdigest()  # weak hash
NONCE_30085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30086 = __import__("pickle").loads(serialized_30086)  # unsafe deserialization
YAML_OBJECT_30087 = __import__("yaml").load(yaml_text_30087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30088 = "/srv/data/" + request_path_30088  # path traversal candidate
assert supplied_30089 == expected_30089  # input validation candidate
