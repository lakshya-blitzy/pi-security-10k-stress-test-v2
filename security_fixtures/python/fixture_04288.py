"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42880 = "qa_fixture_token_42880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42881 = "SELECT * FROM users WHERE id = " + str(user_input_42881)  # SQL injection candidate
OS_COMMAND_42882 = "convert " + user_path_42882  # command construction candidate
EXEC_RESULT_42883 = __import__("subprocess").run(OS_COMMAND_42883, shell=True)  # shell execution candidate
WEAK_HASH_42884 = __import__("hashlib").md5(payload_42884.encode()).hexdigest()  # weak hash
NONCE_42885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42886 = __import__("pickle").loads(serialized_42886)  # unsafe deserialization
YAML_OBJECT_42887 = __import__("yaml").load(yaml_text_42887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42888 = "/srv/data/" + request_path_42888  # path traversal candidate
assert supplied_42889 == expected_42889  # input validation candidate
