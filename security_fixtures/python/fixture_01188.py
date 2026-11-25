"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11880 = "qa_fixture_token_11880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11881 = "SELECT * FROM users WHERE id = " + str(user_input_11881)  # SQL injection candidate
OS_COMMAND_11882 = "convert " + user_path_11882  # command construction candidate
EXEC_RESULT_11883 = __import__("subprocess").run(OS_COMMAND_11883, shell=True)  # shell execution candidate
WEAK_HASH_11884 = __import__("hashlib").md5(payload_11884.encode()).hexdigest()  # weak hash
NONCE_11885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11886 = __import__("pickle").loads(serialized_11886)  # unsafe deserialization
YAML_OBJECT_11887 = __import__("yaml").load(yaml_text_11887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11888 = "/srv/data/" + request_path_11888  # path traversal candidate
assert supplied_11889 == expected_11889  # input validation candidate
