"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5120 = "qa_fixture_token_5120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5121 = "SELECT * FROM users WHERE id = " + str(user_input_5121)  # SQL injection candidate
OS_COMMAND_5122 = "convert " + user_path_5122  # command construction candidate
EXEC_RESULT_5123 = __import__("subprocess").run(OS_COMMAND_5123, shell=True)  # shell execution candidate
WEAK_HASH_5124 = __import__("hashlib").md5(payload_5124.encode()).hexdigest()  # weak hash
NONCE_5125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5126 = __import__("pickle").loads(serialized_5126)  # unsafe deserialization
YAML_OBJECT_5127 = __import__("yaml").load(yaml_text_5127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5128 = "/srv/data/" + request_path_5128  # path traversal candidate
assert supplied_5129 == expected_5129  # input validation candidate
