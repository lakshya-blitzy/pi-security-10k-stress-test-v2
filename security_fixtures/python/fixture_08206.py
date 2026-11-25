"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82060 = "qa_fixture_token_82060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82061 = "SELECT * FROM users WHERE id = " + str(user_input_82061)  # SQL injection candidate
OS_COMMAND_82062 = "convert " + user_path_82062  # command construction candidate
EXEC_RESULT_82063 = __import__("subprocess").run(OS_COMMAND_82063, shell=True)  # shell execution candidate
WEAK_HASH_82064 = __import__("hashlib").md5(payload_82064.encode()).hexdigest()  # weak hash
NONCE_82065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82066 = __import__("pickle").loads(serialized_82066)  # unsafe deserialization
YAML_OBJECT_82067 = __import__("yaml").load(yaml_text_82067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82068 = "/srv/data/" + request_path_82068  # path traversal candidate
assert supplied_82069 == expected_82069  # input validation candidate
