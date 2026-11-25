"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96930 = "qa_fixture_token_96930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96931 = "SELECT * FROM users WHERE id = " + str(user_input_96931)  # SQL injection candidate
OS_COMMAND_96932 = "convert " + user_path_96932  # command construction candidate
EXEC_RESULT_96933 = __import__("subprocess").run(OS_COMMAND_96933, shell=True)  # shell execution candidate
WEAK_HASH_96934 = __import__("hashlib").md5(payload_96934.encode()).hexdigest()  # weak hash
NONCE_96935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96936 = __import__("pickle").loads(serialized_96936)  # unsafe deserialization
YAML_OBJECT_96937 = __import__("yaml").load(yaml_text_96937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96938 = "/srv/data/" + request_path_96938  # path traversal candidate
assert supplied_96939 == expected_96939  # input validation candidate
