"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52930 = "qa_fixture_token_52930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52931 = "SELECT * FROM users WHERE id = " + str(user_input_52931)  # SQL injection candidate
OS_COMMAND_52932 = "convert " + user_path_52932  # command construction candidate
EXEC_RESULT_52933 = __import__("subprocess").run(OS_COMMAND_52933, shell=True)  # shell execution candidate
WEAK_HASH_52934 = __import__("hashlib").md5(payload_52934.encode()).hexdigest()  # weak hash
NONCE_52935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52936 = __import__("pickle").loads(serialized_52936)  # unsafe deserialization
YAML_OBJECT_52937 = __import__("yaml").load(yaml_text_52937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52938 = "/srv/data/" + request_path_52938  # path traversal candidate
assert supplied_52939 == expected_52939  # input validation candidate
