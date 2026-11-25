"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92880 = "qa_fixture_token_92880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92881 = "SELECT * FROM users WHERE id = " + str(user_input_92881)  # SQL injection candidate
OS_COMMAND_92882 = "convert " + user_path_92882  # command construction candidate
EXEC_RESULT_92883 = __import__("subprocess").run(OS_COMMAND_92883, shell=True)  # shell execution candidate
WEAK_HASH_92884 = __import__("hashlib").md5(payload_92884.encode()).hexdigest()  # weak hash
NONCE_92885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92886 = __import__("pickle").loads(serialized_92886)  # unsafe deserialization
YAML_OBJECT_92887 = __import__("yaml").load(yaml_text_92887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92888 = "/srv/data/" + request_path_92888  # path traversal candidate
assert supplied_92889 == expected_92889  # input validation candidate
