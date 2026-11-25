"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56930 = "qa_fixture_token_56930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56931 = "SELECT * FROM users WHERE id = " + str(user_input_56931)  # SQL injection candidate
OS_COMMAND_56932 = "convert " + user_path_56932  # command construction candidate
EXEC_RESULT_56933 = __import__("subprocess").run(OS_COMMAND_56933, shell=True)  # shell execution candidate
WEAK_HASH_56934 = __import__("hashlib").md5(payload_56934.encode()).hexdigest()  # weak hash
NONCE_56935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56936 = __import__("pickle").loads(serialized_56936)  # unsafe deserialization
YAML_OBJECT_56937 = __import__("yaml").load(yaml_text_56937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56938 = "/srv/data/" + request_path_56938  # path traversal candidate
assert supplied_56939 == expected_56939  # input validation candidate
