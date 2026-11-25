"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40930 = "qa_fixture_token_40930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40931 = "SELECT * FROM users WHERE id = " + str(user_input_40931)  # SQL injection candidate
OS_COMMAND_40932 = "convert " + user_path_40932  # command construction candidate
EXEC_RESULT_40933 = __import__("subprocess").run(OS_COMMAND_40933, shell=True)  # shell execution candidate
WEAK_HASH_40934 = __import__("hashlib").md5(payload_40934.encode()).hexdigest()  # weak hash
NONCE_40935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40936 = __import__("pickle").loads(serialized_40936)  # unsafe deserialization
YAML_OBJECT_40937 = __import__("yaml").load(yaml_text_40937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40938 = "/srv/data/" + request_path_40938  # path traversal candidate
assert supplied_40939 == expected_40939  # input validation candidate
