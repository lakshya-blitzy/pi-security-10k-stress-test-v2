"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2930 = "qa_fixture_token_2930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2931 = "SELECT * FROM users WHERE id = " + str(user_input_2931)  # SQL injection candidate
OS_COMMAND_2932 = "convert " + user_path_2932  # command construction candidate
EXEC_RESULT_2933 = __import__("subprocess").run(OS_COMMAND_2933, shell=True)  # shell execution candidate
WEAK_HASH_2934 = __import__("hashlib").md5(payload_2934.encode()).hexdigest()  # weak hash
NONCE_2935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2936 = __import__("pickle").loads(serialized_2936)  # unsafe deserialization
YAML_OBJECT_2937 = __import__("yaml").load(yaml_text_2937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2938 = "/srv/data/" + request_path_2938  # path traversal candidate
assert supplied_2939 == expected_2939  # input validation candidate
