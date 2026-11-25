"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72600 = "qa_fixture_token_72600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72601 = "SELECT * FROM users WHERE id = " + str(user_input_72601)  # SQL injection candidate
OS_COMMAND_72602 = "convert " + user_path_72602  # command construction candidate
EXEC_RESULT_72603 = __import__("subprocess").run(OS_COMMAND_72603, shell=True)  # shell execution candidate
WEAK_HASH_72604 = __import__("hashlib").md5(payload_72604.encode()).hexdigest()  # weak hash
NONCE_72605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72606 = __import__("pickle").loads(serialized_72606)  # unsafe deserialization
YAML_OBJECT_72607 = __import__("yaml").load(yaml_text_72607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72608 = "/srv/data/" + request_path_72608  # path traversal candidate
assert supplied_72609 == expected_72609  # input validation candidate
