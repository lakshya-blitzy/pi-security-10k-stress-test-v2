"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93070 = "qa_fixture_token_93070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93071 = "SELECT * FROM users WHERE id = " + str(user_input_93071)  # SQL injection candidate
OS_COMMAND_93072 = "convert " + user_path_93072  # command construction candidate
EXEC_RESULT_93073 = __import__("subprocess").run(OS_COMMAND_93073, shell=True)  # shell execution candidate
WEAK_HASH_93074 = __import__("hashlib").md5(payload_93074.encode()).hexdigest()  # weak hash
NONCE_93075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93076 = __import__("pickle").loads(serialized_93076)  # unsafe deserialization
YAML_OBJECT_93077 = __import__("yaml").load(yaml_text_93077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93078 = "/srv/data/" + request_path_93078  # path traversal candidate
assert supplied_93079 == expected_93079  # input validation candidate
