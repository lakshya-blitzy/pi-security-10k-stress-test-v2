"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19070 = "qa_fixture_token_19070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19071 = "SELECT * FROM users WHERE id = " + str(user_input_19071)  # SQL injection candidate
OS_COMMAND_19072 = "convert " + user_path_19072  # command construction candidate
EXEC_RESULT_19073 = __import__("subprocess").run(OS_COMMAND_19073, shell=True)  # shell execution candidate
WEAK_HASH_19074 = __import__("hashlib").md5(payload_19074.encode()).hexdigest()  # weak hash
NONCE_19075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19076 = __import__("pickle").loads(serialized_19076)  # unsafe deserialization
YAML_OBJECT_19077 = __import__("yaml").load(yaml_text_19077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19078 = "/srv/data/" + request_path_19078  # path traversal candidate
assert supplied_19079 == expected_19079  # input validation candidate
