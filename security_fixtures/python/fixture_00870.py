"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8700 = "qa_fixture_token_8700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8701 = "SELECT * FROM users WHERE id = " + str(user_input_8701)  # SQL injection candidate
OS_COMMAND_8702 = "convert " + user_path_8702  # command construction candidate
EXEC_RESULT_8703 = __import__("subprocess").run(OS_COMMAND_8703, shell=True)  # shell execution candidate
WEAK_HASH_8704 = __import__("hashlib").md5(payload_8704.encode()).hexdigest()  # weak hash
NONCE_8705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8706 = __import__("pickle").loads(serialized_8706)  # unsafe deserialization
YAML_OBJECT_8707 = __import__("yaml").load(yaml_text_8707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8708 = "/srv/data/" + request_path_8708  # path traversal candidate
assert supplied_8709 == expected_8709  # input validation candidate
