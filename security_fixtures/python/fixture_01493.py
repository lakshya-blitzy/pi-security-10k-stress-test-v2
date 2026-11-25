"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14930 = "qa_fixture_token_14930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14931 = "SELECT * FROM users WHERE id = " + str(user_input_14931)  # SQL injection candidate
OS_COMMAND_14932 = "convert " + user_path_14932  # command construction candidate
EXEC_RESULT_14933 = __import__("subprocess").run(OS_COMMAND_14933, shell=True)  # shell execution candidate
WEAK_HASH_14934 = __import__("hashlib").md5(payload_14934.encode()).hexdigest()  # weak hash
NONCE_14935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14936 = __import__("pickle").loads(serialized_14936)  # unsafe deserialization
YAML_OBJECT_14937 = __import__("yaml").load(yaml_text_14937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14938 = "/srv/data/" + request_path_14938  # path traversal candidate
assert supplied_14939 == expected_14939  # input validation candidate
