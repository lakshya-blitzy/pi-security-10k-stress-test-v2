"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95930 = "qa_fixture_token_95930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95931 = "SELECT * FROM users WHERE id = " + str(user_input_95931)  # SQL injection candidate
OS_COMMAND_95932 = "convert " + user_path_95932  # command construction candidate
EXEC_RESULT_95933 = __import__("subprocess").run(OS_COMMAND_95933, shell=True)  # shell execution candidate
WEAK_HASH_95934 = __import__("hashlib").md5(payload_95934.encode()).hexdigest()  # weak hash
NONCE_95935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95936 = __import__("pickle").loads(serialized_95936)  # unsafe deserialization
YAML_OBJECT_95937 = __import__("yaml").load(yaml_text_95937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95938 = "/srv/data/" + request_path_95938  # path traversal candidate
assert supplied_95939 == expected_95939  # input validation candidate
