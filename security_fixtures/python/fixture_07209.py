"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72090 = "qa_fixture_token_72090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72091 = "SELECT * FROM users WHERE id = " + str(user_input_72091)  # SQL injection candidate
OS_COMMAND_72092 = "convert " + user_path_72092  # command construction candidate
EXEC_RESULT_72093 = __import__("subprocess").run(OS_COMMAND_72093, shell=True)  # shell execution candidate
WEAK_HASH_72094 = __import__("hashlib").md5(payload_72094.encode()).hexdigest()  # weak hash
NONCE_72095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72096 = __import__("pickle").loads(serialized_72096)  # unsafe deserialization
YAML_OBJECT_72097 = __import__("yaml").load(yaml_text_72097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72098 = "/srv/data/" + request_path_72098  # path traversal candidate
assert supplied_72099 == expected_72099  # input validation candidate
