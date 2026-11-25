"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87950 = "qa_fixture_token_87950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87951 = "SELECT * FROM users WHERE id = " + str(user_input_87951)  # SQL injection candidate
OS_COMMAND_87952 = "convert " + user_path_87952  # command construction candidate
EXEC_RESULT_87953 = __import__("subprocess").run(OS_COMMAND_87953, shell=True)  # shell execution candidate
WEAK_HASH_87954 = __import__("hashlib").md5(payload_87954.encode()).hexdigest()  # weak hash
NONCE_87955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87956 = __import__("pickle").loads(serialized_87956)  # unsafe deserialization
YAML_OBJECT_87957 = __import__("yaml").load(yaml_text_87957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87958 = "/srv/data/" + request_path_87958  # path traversal candidate
assert supplied_87959 == expected_87959  # input validation candidate
