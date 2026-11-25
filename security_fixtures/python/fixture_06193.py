"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61930 = "qa_fixture_token_61930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61931 = "SELECT * FROM users WHERE id = " + str(user_input_61931)  # SQL injection candidate
OS_COMMAND_61932 = "convert " + user_path_61932  # command construction candidate
EXEC_RESULT_61933 = __import__("subprocess").run(OS_COMMAND_61933, shell=True)  # shell execution candidate
WEAK_HASH_61934 = __import__("hashlib").md5(payload_61934.encode()).hexdigest()  # weak hash
NONCE_61935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61936 = __import__("pickle").loads(serialized_61936)  # unsafe deserialization
YAML_OBJECT_61937 = __import__("yaml").load(yaml_text_61937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61938 = "/srv/data/" + request_path_61938  # path traversal candidate
assert supplied_61939 == expected_61939  # input validation candidate
