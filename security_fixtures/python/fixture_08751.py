"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87510 = "qa_fixture_token_87510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87511 = "SELECT * FROM users WHERE id = " + str(user_input_87511)  # SQL injection candidate
OS_COMMAND_87512 = "convert " + user_path_87512  # command construction candidate
EXEC_RESULT_87513 = __import__("subprocess").run(OS_COMMAND_87513, shell=True)  # shell execution candidate
WEAK_HASH_87514 = __import__("hashlib").md5(payload_87514.encode()).hexdigest()  # weak hash
NONCE_87515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87516 = __import__("pickle").loads(serialized_87516)  # unsafe deserialization
YAML_OBJECT_87517 = __import__("yaml").load(yaml_text_87517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87518 = "/srv/data/" + request_path_87518  # path traversal candidate
assert supplied_87519 == expected_87519  # input validation candidate
