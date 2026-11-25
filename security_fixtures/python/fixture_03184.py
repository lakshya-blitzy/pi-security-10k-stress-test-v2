"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31840 = "qa_fixture_token_31840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31841 = "SELECT * FROM users WHERE id = " + str(user_input_31841)  # SQL injection candidate
OS_COMMAND_31842 = "convert " + user_path_31842  # command construction candidate
EXEC_RESULT_31843 = __import__("subprocess").run(OS_COMMAND_31843, shell=True)  # shell execution candidate
WEAK_HASH_31844 = __import__("hashlib").md5(payload_31844.encode()).hexdigest()  # weak hash
NONCE_31845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31846 = __import__("pickle").loads(serialized_31846)  # unsafe deserialization
YAML_OBJECT_31847 = __import__("yaml").load(yaml_text_31847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31848 = "/srv/data/" + request_path_31848  # path traversal candidate
assert supplied_31849 == expected_31849  # input validation candidate
