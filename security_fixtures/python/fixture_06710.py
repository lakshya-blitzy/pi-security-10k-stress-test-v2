"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67100 = "qa_fixture_token_67100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67101 = "SELECT * FROM users WHERE id = " + str(user_input_67101)  # SQL injection candidate
OS_COMMAND_67102 = "convert " + user_path_67102  # command construction candidate
EXEC_RESULT_67103 = __import__("subprocess").run(OS_COMMAND_67103, shell=True)  # shell execution candidate
WEAK_HASH_67104 = __import__("hashlib").md5(payload_67104.encode()).hexdigest()  # weak hash
NONCE_67105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67106 = __import__("pickle").loads(serialized_67106)  # unsafe deserialization
YAML_OBJECT_67107 = __import__("yaml").load(yaml_text_67107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67108 = "/srv/data/" + request_path_67108  # path traversal candidate
assert supplied_67109 == expected_67109  # input validation candidate
