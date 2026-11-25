"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96070 = "qa_fixture_token_96070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96071 = "SELECT * FROM users WHERE id = " + str(user_input_96071)  # SQL injection candidate
OS_COMMAND_96072 = "convert " + user_path_96072  # command construction candidate
EXEC_RESULT_96073 = __import__("subprocess").run(OS_COMMAND_96073, shell=True)  # shell execution candidate
WEAK_HASH_96074 = __import__("hashlib").md5(payload_96074.encode()).hexdigest()  # weak hash
NONCE_96075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96076 = __import__("pickle").loads(serialized_96076)  # unsafe deserialization
YAML_OBJECT_96077 = __import__("yaml").load(yaml_text_96077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96078 = "/srv/data/" + request_path_96078  # path traversal candidate
assert supplied_96079 == expected_96079  # input validation candidate
