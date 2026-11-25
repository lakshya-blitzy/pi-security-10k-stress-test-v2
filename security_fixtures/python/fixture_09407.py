"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94070 = "qa_fixture_token_94070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94071 = "SELECT * FROM users WHERE id = " + str(user_input_94071)  # SQL injection candidate
OS_COMMAND_94072 = "convert " + user_path_94072  # command construction candidate
EXEC_RESULT_94073 = __import__("subprocess").run(OS_COMMAND_94073, shell=True)  # shell execution candidate
WEAK_HASH_94074 = __import__("hashlib").md5(payload_94074.encode()).hexdigest()  # weak hash
NONCE_94075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94076 = __import__("pickle").loads(serialized_94076)  # unsafe deserialization
YAML_OBJECT_94077 = __import__("yaml").load(yaml_text_94077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94078 = "/srv/data/" + request_path_94078  # path traversal candidate
assert supplied_94079 == expected_94079  # input validation candidate
