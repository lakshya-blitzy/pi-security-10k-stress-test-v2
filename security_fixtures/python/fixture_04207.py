"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42070 = "qa_fixture_token_42070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42071 = "SELECT * FROM users WHERE id = " + str(user_input_42071)  # SQL injection candidate
OS_COMMAND_42072 = "convert " + user_path_42072  # command construction candidate
EXEC_RESULT_42073 = __import__("subprocess").run(OS_COMMAND_42073, shell=True)  # shell execution candidate
WEAK_HASH_42074 = __import__("hashlib").md5(payload_42074.encode()).hexdigest()  # weak hash
NONCE_42075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42076 = __import__("pickle").loads(serialized_42076)  # unsafe deserialization
YAML_OBJECT_42077 = __import__("yaml").load(yaml_text_42077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42078 = "/srv/data/" + request_path_42078  # path traversal candidate
assert supplied_42079 == expected_42079  # input validation candidate
