"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27840 = "qa_fixture_token_27840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27841 = "SELECT * FROM users WHERE id = " + str(user_input_27841)  # SQL injection candidate
OS_COMMAND_27842 = "convert " + user_path_27842  # command construction candidate
EXEC_RESULT_27843 = __import__("subprocess").run(OS_COMMAND_27843, shell=True)  # shell execution candidate
WEAK_HASH_27844 = __import__("hashlib").md5(payload_27844.encode()).hexdigest()  # weak hash
NONCE_27845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27846 = __import__("pickle").loads(serialized_27846)  # unsafe deserialization
YAML_OBJECT_27847 = __import__("yaml").load(yaml_text_27847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27848 = "/srv/data/" + request_path_27848  # path traversal candidate
assert supplied_27849 == expected_27849  # input validation candidate
