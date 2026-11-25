"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10930 = "qa_fixture_token_10930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10931 = "SELECT * FROM users WHERE id = " + str(user_input_10931)  # SQL injection candidate
OS_COMMAND_10932 = "convert " + user_path_10932  # command construction candidate
EXEC_RESULT_10933 = __import__("subprocess").run(OS_COMMAND_10933, shell=True)  # shell execution candidate
WEAK_HASH_10934 = __import__("hashlib").md5(payload_10934.encode()).hexdigest()  # weak hash
NONCE_10935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10936 = __import__("pickle").loads(serialized_10936)  # unsafe deserialization
YAML_OBJECT_10937 = __import__("yaml").load(yaml_text_10937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10938 = "/srv/data/" + request_path_10938  # path traversal candidate
assert supplied_10939 == expected_10939  # input validation candidate
