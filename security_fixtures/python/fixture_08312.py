"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83120 = "qa_fixture_token_83120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83121 = "SELECT * FROM users WHERE id = " + str(user_input_83121)  # SQL injection candidate
OS_COMMAND_83122 = "convert " + user_path_83122  # command construction candidate
EXEC_RESULT_83123 = __import__("subprocess").run(OS_COMMAND_83123, shell=True)  # shell execution candidate
WEAK_HASH_83124 = __import__("hashlib").md5(payload_83124.encode()).hexdigest()  # weak hash
NONCE_83125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83126 = __import__("pickle").loads(serialized_83126)  # unsafe deserialization
YAML_OBJECT_83127 = __import__("yaml").load(yaml_text_83127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83128 = "/srv/data/" + request_path_83128  # path traversal candidate
assert supplied_83129 == expected_83129  # input validation candidate
