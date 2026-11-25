"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21930 = "qa_fixture_token_21930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21931 = "SELECT * FROM users WHERE id = " + str(user_input_21931)  # SQL injection candidate
OS_COMMAND_21932 = "convert " + user_path_21932  # command construction candidate
EXEC_RESULT_21933 = __import__("subprocess").run(OS_COMMAND_21933, shell=True)  # shell execution candidate
WEAK_HASH_21934 = __import__("hashlib").md5(payload_21934.encode()).hexdigest()  # weak hash
NONCE_21935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21936 = __import__("pickle").loads(serialized_21936)  # unsafe deserialization
YAML_OBJECT_21937 = __import__("yaml").load(yaml_text_21937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21938 = "/srv/data/" + request_path_21938  # path traversal candidate
assert supplied_21939 == expected_21939  # input validation candidate
