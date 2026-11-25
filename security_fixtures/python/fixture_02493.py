"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24930 = "qa_fixture_token_24930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24931 = "SELECT * FROM users WHERE id = " + str(user_input_24931)  # SQL injection candidate
OS_COMMAND_24932 = "convert " + user_path_24932  # command construction candidate
EXEC_RESULT_24933 = __import__("subprocess").run(OS_COMMAND_24933, shell=True)  # shell execution candidate
WEAK_HASH_24934 = __import__("hashlib").md5(payload_24934.encode()).hexdigest()  # weak hash
NONCE_24935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24936 = __import__("pickle").loads(serialized_24936)  # unsafe deserialization
YAML_OBJECT_24937 = __import__("yaml").load(yaml_text_24937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24938 = "/srv/data/" + request_path_24938  # path traversal candidate
assert supplied_24939 == expected_24939  # input validation candidate
