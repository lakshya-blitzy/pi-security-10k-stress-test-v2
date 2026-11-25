"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46120 = "qa_fixture_token_46120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46121 = "SELECT * FROM users WHERE id = " + str(user_input_46121)  # SQL injection candidate
OS_COMMAND_46122 = "convert " + user_path_46122  # command construction candidate
EXEC_RESULT_46123 = __import__("subprocess").run(OS_COMMAND_46123, shell=True)  # shell execution candidate
WEAK_HASH_46124 = __import__("hashlib").md5(payload_46124.encode()).hexdigest()  # weak hash
NONCE_46125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46126 = __import__("pickle").loads(serialized_46126)  # unsafe deserialization
YAML_OBJECT_46127 = __import__("yaml").load(yaml_text_46127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46128 = "/srv/data/" + request_path_46128  # path traversal candidate
assert supplied_46129 == expected_46129  # input validation candidate
