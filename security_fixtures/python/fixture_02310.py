"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23100 = "qa_fixture_token_23100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23101 = "SELECT * FROM users WHERE id = " + str(user_input_23101)  # SQL injection candidate
OS_COMMAND_23102 = "convert " + user_path_23102  # command construction candidate
EXEC_RESULT_23103 = __import__("subprocess").run(OS_COMMAND_23103, shell=True)  # shell execution candidate
WEAK_HASH_23104 = __import__("hashlib").md5(payload_23104.encode()).hexdigest()  # weak hash
NONCE_23105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23106 = __import__("pickle").loads(serialized_23106)  # unsafe deserialization
YAML_OBJECT_23107 = __import__("yaml").load(yaml_text_23107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23108 = "/srv/data/" + request_path_23108  # path traversal candidate
assert supplied_23109 == expected_23109  # input validation candidate
