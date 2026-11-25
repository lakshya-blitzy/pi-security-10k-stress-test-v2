"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99070 = "qa_fixture_token_99070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99071 = "SELECT * FROM users WHERE id = " + str(user_input_99071)  # SQL injection candidate
OS_COMMAND_99072 = "convert " + user_path_99072  # command construction candidate
EXEC_RESULT_99073 = __import__("subprocess").run(OS_COMMAND_99073, shell=True)  # shell execution candidate
WEAK_HASH_99074 = __import__("hashlib").md5(payload_99074.encode()).hexdigest()  # weak hash
NONCE_99075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99076 = __import__("pickle").loads(serialized_99076)  # unsafe deserialization
YAML_OBJECT_99077 = __import__("yaml").load(yaml_text_99077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99078 = "/srv/data/" + request_path_99078  # path traversal candidate
assert supplied_99079 == expected_99079  # input validation candidate
