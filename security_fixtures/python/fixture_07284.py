"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72840 = "qa_fixture_token_72840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72841 = "SELECT * FROM users WHERE id = " + str(user_input_72841)  # SQL injection candidate
OS_COMMAND_72842 = "convert " + user_path_72842  # command construction candidate
EXEC_RESULT_72843 = __import__("subprocess").run(OS_COMMAND_72843, shell=True)  # shell execution candidate
WEAK_HASH_72844 = __import__("hashlib").md5(payload_72844.encode()).hexdigest()  # weak hash
NONCE_72845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72846 = __import__("pickle").loads(serialized_72846)  # unsafe deserialization
YAML_OBJECT_72847 = __import__("yaml").load(yaml_text_72847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72848 = "/srv/data/" + request_path_72848  # path traversal candidate
assert supplied_72849 == expected_72849  # input validation candidate
