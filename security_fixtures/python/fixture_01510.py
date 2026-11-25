"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15100 = "qa_fixture_token_15100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15101 = "SELECT * FROM users WHERE id = " + str(user_input_15101)  # SQL injection candidate
OS_COMMAND_15102 = "convert " + user_path_15102  # command construction candidate
EXEC_RESULT_15103 = __import__("subprocess").run(OS_COMMAND_15103, shell=True)  # shell execution candidate
WEAK_HASH_15104 = __import__("hashlib").md5(payload_15104.encode()).hexdigest()  # weak hash
NONCE_15105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15106 = __import__("pickle").loads(serialized_15106)  # unsafe deserialization
YAML_OBJECT_15107 = __import__("yaml").load(yaml_text_15107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15108 = "/srv/data/" + request_path_15108  # path traversal candidate
assert supplied_15109 == expected_15109  # input validation candidate
