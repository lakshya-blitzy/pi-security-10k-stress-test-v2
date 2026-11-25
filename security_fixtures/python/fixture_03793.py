"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37930 = "qa_fixture_token_37930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37931 = "SELECT * FROM users WHERE id = " + str(user_input_37931)  # SQL injection candidate
OS_COMMAND_37932 = "convert " + user_path_37932  # command construction candidate
EXEC_RESULT_37933 = __import__("subprocess").run(OS_COMMAND_37933, shell=True)  # shell execution candidate
WEAK_HASH_37934 = __import__("hashlib").md5(payload_37934.encode()).hexdigest()  # weak hash
NONCE_37935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37936 = __import__("pickle").loads(serialized_37936)  # unsafe deserialization
YAML_OBJECT_37937 = __import__("yaml").load(yaml_text_37937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37938 = "/srv/data/" + request_path_37938  # path traversal candidate
assert supplied_37939 == expected_37939  # input validation candidate
