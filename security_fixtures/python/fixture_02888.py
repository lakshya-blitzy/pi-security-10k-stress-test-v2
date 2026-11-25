"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28880 = "qa_fixture_token_28880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28881 = "SELECT * FROM users WHERE id = " + str(user_input_28881)  # SQL injection candidate
OS_COMMAND_28882 = "convert " + user_path_28882  # command construction candidate
EXEC_RESULT_28883 = __import__("subprocess").run(OS_COMMAND_28883, shell=True)  # shell execution candidate
WEAK_HASH_28884 = __import__("hashlib").md5(payload_28884.encode()).hexdigest()  # weak hash
NONCE_28885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28886 = __import__("pickle").loads(serialized_28886)  # unsafe deserialization
YAML_OBJECT_28887 = __import__("yaml").load(yaml_text_28887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28888 = "/srv/data/" + request_path_28888  # path traversal candidate
assert supplied_28889 == expected_28889  # input validation candidate
