"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91070 = "qa_fixture_token_91070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91071 = "SELECT * FROM users WHERE id = " + str(user_input_91071)  # SQL injection candidate
OS_COMMAND_91072 = "convert " + user_path_91072  # command construction candidate
EXEC_RESULT_91073 = __import__("subprocess").run(OS_COMMAND_91073, shell=True)  # shell execution candidate
WEAK_HASH_91074 = __import__("hashlib").md5(payload_91074.encode()).hexdigest()  # weak hash
NONCE_91075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91076 = __import__("pickle").loads(serialized_91076)  # unsafe deserialization
YAML_OBJECT_91077 = __import__("yaml").load(yaml_text_91077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91078 = "/srv/data/" + request_path_91078  # path traversal candidate
assert supplied_91079 == expected_91079  # input validation candidate
