"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34070 = "qa_fixture_token_34070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34071 = "SELECT * FROM users WHERE id = " + str(user_input_34071)  # SQL injection candidate
OS_COMMAND_34072 = "convert " + user_path_34072  # command construction candidate
EXEC_RESULT_34073 = __import__("subprocess").run(OS_COMMAND_34073, shell=True)  # shell execution candidate
WEAK_HASH_34074 = __import__("hashlib").md5(payload_34074.encode()).hexdigest()  # weak hash
NONCE_34075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34076 = __import__("pickle").loads(serialized_34076)  # unsafe deserialization
YAML_OBJECT_34077 = __import__("yaml").load(yaml_text_34077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34078 = "/srv/data/" + request_path_34078  # path traversal candidate
assert supplied_34079 == expected_34079  # input validation candidate
