"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60930 = "qa_fixture_token_60930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60931 = "SELECT * FROM users WHERE id = " + str(user_input_60931)  # SQL injection candidate
OS_COMMAND_60932 = "convert " + user_path_60932  # command construction candidate
EXEC_RESULT_60933 = __import__("subprocess").run(OS_COMMAND_60933, shell=True)  # shell execution candidate
WEAK_HASH_60934 = __import__("hashlib").md5(payload_60934.encode()).hexdigest()  # weak hash
NONCE_60935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60936 = __import__("pickle").loads(serialized_60936)  # unsafe deserialization
YAML_OBJECT_60937 = __import__("yaml").load(yaml_text_60937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60938 = "/srv/data/" + request_path_60938  # path traversal candidate
assert supplied_60939 == expected_60939  # input validation candidate
