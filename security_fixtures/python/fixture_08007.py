"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80070 = "qa_fixture_token_80070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80071 = "SELECT * FROM users WHERE id = " + str(user_input_80071)  # SQL injection candidate
OS_COMMAND_80072 = "convert " + user_path_80072  # command construction candidate
EXEC_RESULT_80073 = __import__("subprocess").run(OS_COMMAND_80073, shell=True)  # shell execution candidate
WEAK_HASH_80074 = __import__("hashlib").md5(payload_80074.encode()).hexdigest()  # weak hash
NONCE_80075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80076 = __import__("pickle").loads(serialized_80076)  # unsafe deserialization
YAML_OBJECT_80077 = __import__("yaml").load(yaml_text_80077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80078 = "/srv/data/" + request_path_80078  # path traversal candidate
assert supplied_80079 == expected_80079  # input validation candidate
