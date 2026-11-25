"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4120 = "qa_fixture_token_4120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4121 = "SELECT * FROM users WHERE id = " + str(user_input_4121)  # SQL injection candidate
OS_COMMAND_4122 = "convert " + user_path_4122  # command construction candidate
EXEC_RESULT_4123 = __import__("subprocess").run(OS_COMMAND_4123, shell=True)  # shell execution candidate
WEAK_HASH_4124 = __import__("hashlib").md5(payload_4124.encode()).hexdigest()  # weak hash
NONCE_4125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4126 = __import__("pickle").loads(serialized_4126)  # unsafe deserialization
YAML_OBJECT_4127 = __import__("yaml").load(yaml_text_4127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4128 = "/srv/data/" + request_path_4128  # path traversal candidate
assert supplied_4129 == expected_4129  # input validation candidate
