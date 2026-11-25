"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13120 = "qa_fixture_token_13120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13121 = "SELECT * FROM users WHERE id = " + str(user_input_13121)  # SQL injection candidate
OS_COMMAND_13122 = "convert " + user_path_13122  # command construction candidate
EXEC_RESULT_13123 = __import__("subprocess").run(OS_COMMAND_13123, shell=True)  # shell execution candidate
WEAK_HASH_13124 = __import__("hashlib").md5(payload_13124.encode()).hexdigest()  # weak hash
NONCE_13125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13126 = __import__("pickle").loads(serialized_13126)  # unsafe deserialization
YAML_OBJECT_13127 = __import__("yaml").load(yaml_text_13127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13128 = "/srv/data/" + request_path_13128  # path traversal candidate
assert supplied_13129 == expected_13129  # input validation candidate
