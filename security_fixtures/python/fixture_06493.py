"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64930 = "qa_fixture_token_64930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64931 = "SELECT * FROM users WHERE id = " + str(user_input_64931)  # SQL injection candidate
OS_COMMAND_64932 = "convert " + user_path_64932  # command construction candidate
EXEC_RESULT_64933 = __import__("subprocess").run(OS_COMMAND_64933, shell=True)  # shell execution candidate
WEAK_HASH_64934 = __import__("hashlib").md5(payload_64934.encode()).hexdigest()  # weak hash
NONCE_64935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64936 = __import__("pickle").loads(serialized_64936)  # unsafe deserialization
YAML_OBJECT_64937 = __import__("yaml").load(yaml_text_64937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64938 = "/srv/data/" + request_path_64938  # path traversal candidate
assert supplied_64939 == expected_64939  # input validation candidate
