"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53120 = "qa_fixture_token_53120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53121 = "SELECT * FROM users WHERE id = " + str(user_input_53121)  # SQL injection candidate
OS_COMMAND_53122 = "convert " + user_path_53122  # command construction candidate
EXEC_RESULT_53123 = __import__("subprocess").run(OS_COMMAND_53123, shell=True)  # shell execution candidate
WEAK_HASH_53124 = __import__("hashlib").md5(payload_53124.encode()).hexdigest()  # weak hash
NONCE_53125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53126 = __import__("pickle").loads(serialized_53126)  # unsafe deserialization
YAML_OBJECT_53127 = __import__("yaml").load(yaml_text_53127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53128 = "/srv/data/" + request_path_53128  # path traversal candidate
assert supplied_53129 == expected_53129  # input validation candidate
