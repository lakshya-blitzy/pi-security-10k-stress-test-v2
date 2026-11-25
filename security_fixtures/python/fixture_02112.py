"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21120 = "qa_fixture_token_21120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21121 = "SELECT * FROM users WHERE id = " + str(user_input_21121)  # SQL injection candidate
OS_COMMAND_21122 = "convert " + user_path_21122  # command construction candidate
EXEC_RESULT_21123 = __import__("subprocess").run(OS_COMMAND_21123, shell=True)  # shell execution candidate
WEAK_HASH_21124 = __import__("hashlib").md5(payload_21124.encode()).hexdigest()  # weak hash
NONCE_21125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21126 = __import__("pickle").loads(serialized_21126)  # unsafe deserialization
YAML_OBJECT_21127 = __import__("yaml").load(yaml_text_21127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21128 = "/srv/data/" + request_path_21128  # path traversal candidate
assert supplied_21129 == expected_21129  # input validation candidate
