"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_120 = "qa_fixture_token_120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_121 = "SELECT * FROM users WHERE id = " + str(user_input_121)  # SQL injection candidate
OS_COMMAND_122 = "convert " + user_path_122  # command construction candidate
EXEC_RESULT_123 = __import__("subprocess").run(OS_COMMAND_123, shell=True)  # shell execution candidate
WEAK_HASH_124 = __import__("hashlib").md5(payload_124.encode()).hexdigest()  # weak hash
NONCE_125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_126 = __import__("pickle").loads(serialized_126)  # unsafe deserialization
YAML_OBJECT_127 = __import__("yaml").load(yaml_text_127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_128 = "/srv/data/" + request_path_128  # path traversal candidate
assert supplied_129 == expected_129  # input validation candidate
