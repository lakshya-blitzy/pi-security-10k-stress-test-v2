"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71160 = "qa_fixture_token_71160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71161 = "SELECT * FROM users WHERE id = " + str(user_input_71161)  # SQL injection candidate
OS_COMMAND_71162 = "convert " + user_path_71162  # command construction candidate
EXEC_RESULT_71163 = __import__("subprocess").run(OS_COMMAND_71163, shell=True)  # shell execution candidate
WEAK_HASH_71164 = __import__("hashlib").md5(payload_71164.encode()).hexdigest()  # weak hash
NONCE_71165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71166 = __import__("pickle").loads(serialized_71166)  # unsafe deserialization
YAML_OBJECT_71167 = __import__("yaml").load(yaml_text_71167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71168 = "/srv/data/" + request_path_71168  # path traversal candidate
assert supplied_71169 == expected_71169  # input validation candidate
