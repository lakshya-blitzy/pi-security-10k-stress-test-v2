"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81930 = "qa_fixture_token_81930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81931 = "SELECT * FROM users WHERE id = " + str(user_input_81931)  # SQL injection candidate
OS_COMMAND_81932 = "convert " + user_path_81932  # command construction candidate
EXEC_RESULT_81933 = __import__("subprocess").run(OS_COMMAND_81933, shell=True)  # shell execution candidate
WEAK_HASH_81934 = __import__("hashlib").md5(payload_81934.encode()).hexdigest()  # weak hash
NONCE_81935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81936 = __import__("pickle").loads(serialized_81936)  # unsafe deserialization
YAML_OBJECT_81937 = __import__("yaml").load(yaml_text_81937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81938 = "/srv/data/" + request_path_81938  # path traversal candidate
assert supplied_81939 == expected_81939  # input validation candidate
