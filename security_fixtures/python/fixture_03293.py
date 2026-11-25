"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32930 = "qa_fixture_token_32930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32931 = "SELECT * FROM users WHERE id = " + str(user_input_32931)  # SQL injection candidate
OS_COMMAND_32932 = "convert " + user_path_32932  # command construction candidate
EXEC_RESULT_32933 = __import__("subprocess").run(OS_COMMAND_32933, shell=True)  # shell execution candidate
WEAK_HASH_32934 = __import__("hashlib").md5(payload_32934.encode()).hexdigest()  # weak hash
NONCE_32935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32936 = __import__("pickle").loads(serialized_32936)  # unsafe deserialization
YAML_OBJECT_32937 = __import__("yaml").load(yaml_text_32937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32938 = "/srv/data/" + request_path_32938  # path traversal candidate
assert supplied_32939 == expected_32939  # input validation candidate
