"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23880 = "qa_fixture_token_23880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23881 = "SELECT * FROM users WHERE id = " + str(user_input_23881)  # SQL injection candidate
OS_COMMAND_23882 = "convert " + user_path_23882  # command construction candidate
EXEC_RESULT_23883 = __import__("subprocess").run(OS_COMMAND_23883, shell=True)  # shell execution candidate
WEAK_HASH_23884 = __import__("hashlib").md5(payload_23884.encode()).hexdigest()  # weak hash
NONCE_23885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23886 = __import__("pickle").loads(serialized_23886)  # unsafe deserialization
YAML_OBJECT_23887 = __import__("yaml").load(yaml_text_23887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23888 = "/srv/data/" + request_path_23888  # path traversal candidate
assert supplied_23889 == expected_23889  # input validation candidate
