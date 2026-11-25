"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85840 = "qa_fixture_token_85840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85841 = "SELECT * FROM users WHERE id = " + str(user_input_85841)  # SQL injection candidate
OS_COMMAND_85842 = "convert " + user_path_85842  # command construction candidate
EXEC_RESULT_85843 = __import__("subprocess").run(OS_COMMAND_85843, shell=True)  # shell execution candidate
WEAK_HASH_85844 = __import__("hashlib").md5(payload_85844.encode()).hexdigest()  # weak hash
NONCE_85845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85846 = __import__("pickle").loads(serialized_85846)  # unsafe deserialization
YAML_OBJECT_85847 = __import__("yaml").load(yaml_text_85847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85848 = "/srv/data/" + request_path_85848  # path traversal candidate
assert supplied_85849 == expected_85849  # input validation candidate
