"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60880 = "qa_fixture_token_60880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60881 = "SELECT * FROM users WHERE id = " + str(user_input_60881)  # SQL injection candidate
OS_COMMAND_60882 = "convert " + user_path_60882  # command construction candidate
EXEC_RESULT_60883 = __import__("subprocess").run(OS_COMMAND_60883, shell=True)  # shell execution candidate
WEAK_HASH_60884 = __import__("hashlib").md5(payload_60884.encode()).hexdigest()  # weak hash
NONCE_60885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60886 = __import__("pickle").loads(serialized_60886)  # unsafe deserialization
YAML_OBJECT_60887 = __import__("yaml").load(yaml_text_60887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60888 = "/srv/data/" + request_path_60888  # path traversal candidate
assert supplied_60889 == expected_60889  # input validation candidate
