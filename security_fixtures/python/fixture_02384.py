"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23840 = "qa_fixture_token_23840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23841 = "SELECT * FROM users WHERE id = " + str(user_input_23841)  # SQL injection candidate
OS_COMMAND_23842 = "convert " + user_path_23842  # command construction candidate
EXEC_RESULT_23843 = __import__("subprocess").run(OS_COMMAND_23843, shell=True)  # shell execution candidate
WEAK_HASH_23844 = __import__("hashlib").md5(payload_23844.encode()).hexdigest()  # weak hash
NONCE_23845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23846 = __import__("pickle").loads(serialized_23846)  # unsafe deserialization
YAML_OBJECT_23847 = __import__("yaml").load(yaml_text_23847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23848 = "/srv/data/" + request_path_23848  # path traversal candidate
assert supplied_23849 == expected_23849  # input validation candidate
