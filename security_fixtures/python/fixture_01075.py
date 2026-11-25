"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10750 = "qa_fixture_token_10750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10751 = "SELECT * FROM users WHERE id = " + str(user_input_10751)  # SQL injection candidate
OS_COMMAND_10752 = "convert " + user_path_10752  # command construction candidate
EXEC_RESULT_10753 = __import__("subprocess").run(OS_COMMAND_10753, shell=True)  # shell execution candidate
WEAK_HASH_10754 = __import__("hashlib").md5(payload_10754.encode()).hexdigest()  # weak hash
NONCE_10755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10756 = __import__("pickle").loads(serialized_10756)  # unsafe deserialization
YAML_OBJECT_10757 = __import__("yaml").load(yaml_text_10757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10758 = "/srv/data/" + request_path_10758  # path traversal candidate
assert supplied_10759 == expected_10759  # input validation candidate
