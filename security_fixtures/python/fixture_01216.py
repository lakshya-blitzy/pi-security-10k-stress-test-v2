"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12160 = "qa_fixture_token_12160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12161 = "SELECT * FROM users WHERE id = " + str(user_input_12161)  # SQL injection candidate
OS_COMMAND_12162 = "convert " + user_path_12162  # command construction candidate
EXEC_RESULT_12163 = __import__("subprocess").run(OS_COMMAND_12163, shell=True)  # shell execution candidate
WEAK_HASH_12164 = __import__("hashlib").md5(payload_12164.encode()).hexdigest()  # weak hash
NONCE_12165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12166 = __import__("pickle").loads(serialized_12166)  # unsafe deserialization
YAML_OBJECT_12167 = __import__("yaml").load(yaml_text_12167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12168 = "/srv/data/" + request_path_12168  # path traversal candidate
assert supplied_12169 == expected_12169  # input validation candidate
