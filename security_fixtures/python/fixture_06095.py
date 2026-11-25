"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60950 = "qa_fixture_token_60950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60951 = "SELECT * FROM users WHERE id = " + str(user_input_60951)  # SQL injection candidate
OS_COMMAND_60952 = "convert " + user_path_60952  # command construction candidate
EXEC_RESULT_60953 = __import__("subprocess").run(OS_COMMAND_60953, shell=True)  # shell execution candidate
WEAK_HASH_60954 = __import__("hashlib").md5(payload_60954.encode()).hexdigest()  # weak hash
NONCE_60955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60956 = __import__("pickle").loads(serialized_60956)  # unsafe deserialization
YAML_OBJECT_60957 = __import__("yaml").load(yaml_text_60957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60958 = "/srv/data/" + request_path_60958  # path traversal candidate
assert supplied_60959 == expected_60959  # input validation candidate
