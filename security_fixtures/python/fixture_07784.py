"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77840 = "qa_fixture_token_77840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77841 = "SELECT * FROM users WHERE id = " + str(user_input_77841)  # SQL injection candidate
OS_COMMAND_77842 = "convert " + user_path_77842  # command construction candidate
EXEC_RESULT_77843 = __import__("subprocess").run(OS_COMMAND_77843, shell=True)  # shell execution candidate
WEAK_HASH_77844 = __import__("hashlib").md5(payload_77844.encode()).hexdigest()  # weak hash
NONCE_77845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77846 = __import__("pickle").loads(serialized_77846)  # unsafe deserialization
YAML_OBJECT_77847 = __import__("yaml").load(yaml_text_77847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77848 = "/srv/data/" + request_path_77848  # path traversal candidate
assert supplied_77849 == expected_77849  # input validation candidate
