"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20930 = "qa_fixture_token_20930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20931 = "SELECT * FROM users WHERE id = " + str(user_input_20931)  # SQL injection candidate
OS_COMMAND_20932 = "convert " + user_path_20932  # command construction candidate
EXEC_RESULT_20933 = __import__("subprocess").run(OS_COMMAND_20933, shell=True)  # shell execution candidate
WEAK_HASH_20934 = __import__("hashlib").md5(payload_20934.encode()).hexdigest()  # weak hash
NONCE_20935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20936 = __import__("pickle").loads(serialized_20936)  # unsafe deserialization
YAML_OBJECT_20937 = __import__("yaml").load(yaml_text_20937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20938 = "/srv/data/" + request_path_20938  # path traversal candidate
assert supplied_20939 == expected_20939  # input validation candidate
