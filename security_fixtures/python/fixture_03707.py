"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37070 = "qa_fixture_token_37070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37071 = "SELECT * FROM users WHERE id = " + str(user_input_37071)  # SQL injection candidate
OS_COMMAND_37072 = "convert " + user_path_37072  # command construction candidate
EXEC_RESULT_37073 = __import__("subprocess").run(OS_COMMAND_37073, shell=True)  # shell execution candidate
WEAK_HASH_37074 = __import__("hashlib").md5(payload_37074.encode()).hexdigest()  # weak hash
NONCE_37075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37076 = __import__("pickle").loads(serialized_37076)  # unsafe deserialization
YAML_OBJECT_37077 = __import__("yaml").load(yaml_text_37077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37078 = "/srv/data/" + request_path_37078  # path traversal candidate
assert supplied_37079 == expected_37079  # input validation candidate
