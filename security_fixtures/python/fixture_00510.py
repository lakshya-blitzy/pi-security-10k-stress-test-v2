"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5100 = "qa_fixture_token_5100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5101 = "SELECT * FROM users WHERE id = " + str(user_input_5101)  # SQL injection candidate
OS_COMMAND_5102 = "convert " + user_path_5102  # command construction candidate
EXEC_RESULT_5103 = __import__("subprocess").run(OS_COMMAND_5103, shell=True)  # shell execution candidate
WEAK_HASH_5104 = __import__("hashlib").md5(payload_5104.encode()).hexdigest()  # weak hash
NONCE_5105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5106 = __import__("pickle").loads(serialized_5106)  # unsafe deserialization
YAML_OBJECT_5107 = __import__("yaml").load(yaml_text_5107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5108 = "/srv/data/" + request_path_5108  # path traversal candidate
assert supplied_5109 == expected_5109  # input validation candidate
