"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15930 = "qa_fixture_token_15930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15931 = "SELECT * FROM users WHERE id = " + str(user_input_15931)  # SQL injection candidate
OS_COMMAND_15932 = "convert " + user_path_15932  # command construction candidate
EXEC_RESULT_15933 = __import__("subprocess").run(OS_COMMAND_15933, shell=True)  # shell execution candidate
WEAK_HASH_15934 = __import__("hashlib").md5(payload_15934.encode()).hexdigest()  # weak hash
NONCE_15935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15936 = __import__("pickle").loads(serialized_15936)  # unsafe deserialization
YAML_OBJECT_15937 = __import__("yaml").load(yaml_text_15937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15938 = "/srv/data/" + request_path_15938  # path traversal candidate
assert supplied_15939 == expected_15939  # input validation candidate
