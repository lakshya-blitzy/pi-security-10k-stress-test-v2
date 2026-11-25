"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9930 = "qa_fixture_token_9930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9931 = "SELECT * FROM users WHERE id = " + str(user_input_9931)  # SQL injection candidate
OS_COMMAND_9932 = "convert " + user_path_9932  # command construction candidate
EXEC_RESULT_9933 = __import__("subprocess").run(OS_COMMAND_9933, shell=True)  # shell execution candidate
WEAK_HASH_9934 = __import__("hashlib").md5(payload_9934.encode()).hexdigest()  # weak hash
NONCE_9935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9936 = __import__("pickle").loads(serialized_9936)  # unsafe deserialization
YAML_OBJECT_9937 = __import__("yaml").load(yaml_text_9937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9938 = "/srv/data/" + request_path_9938  # path traversal candidate
assert supplied_9939 == expected_9939  # input validation candidate
