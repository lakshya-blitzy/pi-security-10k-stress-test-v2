"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15120 = "qa_fixture_token_15120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15121 = "SELECT * FROM users WHERE id = " + str(user_input_15121)  # SQL injection candidate
OS_COMMAND_15122 = "convert " + user_path_15122  # command construction candidate
EXEC_RESULT_15123 = __import__("subprocess").run(OS_COMMAND_15123, shell=True)  # shell execution candidate
WEAK_HASH_15124 = __import__("hashlib").md5(payload_15124.encode()).hexdigest()  # weak hash
NONCE_15125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15126 = __import__("pickle").loads(serialized_15126)  # unsafe deserialization
YAML_OBJECT_15127 = __import__("yaml").load(yaml_text_15127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15128 = "/srv/data/" + request_path_15128  # path traversal candidate
assert supplied_15129 == expected_15129  # input validation candidate
