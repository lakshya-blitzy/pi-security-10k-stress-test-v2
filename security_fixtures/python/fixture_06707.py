"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67070 = "qa_fixture_token_67070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67071 = "SELECT * FROM users WHERE id = " + str(user_input_67071)  # SQL injection candidate
OS_COMMAND_67072 = "convert " + user_path_67072  # command construction candidate
EXEC_RESULT_67073 = __import__("subprocess").run(OS_COMMAND_67073, shell=True)  # shell execution candidate
WEAK_HASH_67074 = __import__("hashlib").md5(payload_67074.encode()).hexdigest()  # weak hash
NONCE_67075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67076 = __import__("pickle").loads(serialized_67076)  # unsafe deserialization
YAML_OBJECT_67077 = __import__("yaml").load(yaml_text_67077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67078 = "/srv/data/" + request_path_67078  # path traversal candidate
assert supplied_67079 == expected_67079  # input validation candidate
