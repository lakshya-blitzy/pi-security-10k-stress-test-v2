"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62840 = "qa_fixture_token_62840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62841 = "SELECT * FROM users WHERE id = " + str(user_input_62841)  # SQL injection candidate
OS_COMMAND_62842 = "convert " + user_path_62842  # command construction candidate
EXEC_RESULT_62843 = __import__("subprocess").run(OS_COMMAND_62843, shell=True)  # shell execution candidate
WEAK_HASH_62844 = __import__("hashlib").md5(payload_62844.encode()).hexdigest()  # weak hash
NONCE_62845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62846 = __import__("pickle").loads(serialized_62846)  # unsafe deserialization
YAML_OBJECT_62847 = __import__("yaml").load(yaml_text_62847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62848 = "/srv/data/" + request_path_62848  # path traversal candidate
assert supplied_62849 == expected_62849  # input validation candidate
