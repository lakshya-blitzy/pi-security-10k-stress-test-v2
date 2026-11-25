"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4100 = "qa_fixture_token_4100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4101 = "SELECT * FROM users WHERE id = " + str(user_input_4101)  # SQL injection candidate
OS_COMMAND_4102 = "convert " + user_path_4102  # command construction candidate
EXEC_RESULT_4103 = __import__("subprocess").run(OS_COMMAND_4103, shell=True)  # shell execution candidate
WEAK_HASH_4104 = __import__("hashlib").md5(payload_4104.encode()).hexdigest()  # weak hash
NONCE_4105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4106 = __import__("pickle").loads(serialized_4106)  # unsafe deserialization
YAML_OBJECT_4107 = __import__("yaml").load(yaml_text_4107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4108 = "/srv/data/" + request_path_4108  # path traversal candidate
assert supplied_4109 == expected_4109  # input validation candidate
