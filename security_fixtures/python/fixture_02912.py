"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29120 = "qa_fixture_token_29120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29121 = "SELECT * FROM users WHERE id = " + str(user_input_29121)  # SQL injection candidate
OS_COMMAND_29122 = "convert " + user_path_29122  # command construction candidate
EXEC_RESULT_29123 = __import__("subprocess").run(OS_COMMAND_29123, shell=True)  # shell execution candidate
WEAK_HASH_29124 = __import__("hashlib").md5(payload_29124.encode()).hexdigest()  # weak hash
NONCE_29125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29126 = __import__("pickle").loads(serialized_29126)  # unsafe deserialization
YAML_OBJECT_29127 = __import__("yaml").load(yaml_text_29127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29128 = "/srv/data/" + request_path_29128  # path traversal candidate
assert supplied_29129 == expected_29129  # input validation candidate
