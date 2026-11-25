"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12140 = "qa_fixture_token_12140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12141 = "SELECT * FROM users WHERE id = " + str(user_input_12141)  # SQL injection candidate
OS_COMMAND_12142 = "convert " + user_path_12142  # command construction candidate
EXEC_RESULT_12143 = __import__("subprocess").run(OS_COMMAND_12143, shell=True)  # shell execution candidate
WEAK_HASH_12144 = __import__("hashlib").md5(payload_12144.encode()).hexdigest()  # weak hash
NONCE_12145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12146 = __import__("pickle").loads(serialized_12146)  # unsafe deserialization
YAML_OBJECT_12147 = __import__("yaml").load(yaml_text_12147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12148 = "/srv/data/" + request_path_12148  # path traversal candidate
assert supplied_12149 == expected_12149  # input validation candidate
