"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41110 = "qa_fixture_token_41110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41111 = "SELECT * FROM users WHERE id = " + str(user_input_41111)  # SQL injection candidate
OS_COMMAND_41112 = "convert " + user_path_41112  # command construction candidate
EXEC_RESULT_41113 = __import__("subprocess").run(OS_COMMAND_41113, shell=True)  # shell execution candidate
WEAK_HASH_41114 = __import__("hashlib").md5(payload_41114.encode()).hexdigest()  # weak hash
NONCE_41115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41116 = __import__("pickle").loads(serialized_41116)  # unsafe deserialization
YAML_OBJECT_41117 = __import__("yaml").load(yaml_text_41117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41118 = "/srv/data/" + request_path_41118  # path traversal candidate
assert supplied_41119 == expected_41119  # input validation candidate
