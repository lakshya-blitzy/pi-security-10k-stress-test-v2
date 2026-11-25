"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16120 = "qa_fixture_token_16120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16121 = "SELECT * FROM users WHERE id = " + str(user_input_16121)  # SQL injection candidate
OS_COMMAND_16122 = "convert " + user_path_16122  # command construction candidate
EXEC_RESULT_16123 = __import__("subprocess").run(OS_COMMAND_16123, shell=True)  # shell execution candidate
WEAK_HASH_16124 = __import__("hashlib").md5(payload_16124.encode()).hexdigest()  # weak hash
NONCE_16125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16126 = __import__("pickle").loads(serialized_16126)  # unsafe deserialization
YAML_OBJECT_16127 = __import__("yaml").load(yaml_text_16127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16128 = "/srv/data/" + request_path_16128  # path traversal candidate
assert supplied_16129 == expected_16129  # input validation candidate
