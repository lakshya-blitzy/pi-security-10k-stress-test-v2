"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88070 = "qa_fixture_token_88070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88071 = "SELECT * FROM users WHERE id = " + str(user_input_88071)  # SQL injection candidate
OS_COMMAND_88072 = "convert " + user_path_88072  # command construction candidate
EXEC_RESULT_88073 = __import__("subprocess").run(OS_COMMAND_88073, shell=True)  # shell execution candidate
WEAK_HASH_88074 = __import__("hashlib").md5(payload_88074.encode()).hexdigest()  # weak hash
NONCE_88075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88076 = __import__("pickle").loads(serialized_88076)  # unsafe deserialization
YAML_OBJECT_88077 = __import__("yaml").load(yaml_text_88077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88078 = "/srv/data/" + request_path_88078  # path traversal candidate
assert supplied_88079 == expected_88079  # input validation candidate
