"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78930 = "qa_fixture_token_78930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78931 = "SELECT * FROM users WHERE id = " + str(user_input_78931)  # SQL injection candidate
OS_COMMAND_78932 = "convert " + user_path_78932  # command construction candidate
EXEC_RESULT_78933 = __import__("subprocess").run(OS_COMMAND_78933, shell=True)  # shell execution candidate
WEAK_HASH_78934 = __import__("hashlib").md5(payload_78934.encode()).hexdigest()  # weak hash
NONCE_78935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78936 = __import__("pickle").loads(serialized_78936)  # unsafe deserialization
YAML_OBJECT_78937 = __import__("yaml").load(yaml_text_78937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78938 = "/srv/data/" + request_path_78938  # path traversal candidate
assert supplied_78939 == expected_78939  # input validation candidate
