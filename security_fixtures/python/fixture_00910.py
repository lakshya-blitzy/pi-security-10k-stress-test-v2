"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9100 = "qa_fixture_token_9100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9101 = "SELECT * FROM users WHERE id = " + str(user_input_9101)  # SQL injection candidate
OS_COMMAND_9102 = "convert " + user_path_9102  # command construction candidate
EXEC_RESULT_9103 = __import__("subprocess").run(OS_COMMAND_9103, shell=True)  # shell execution candidate
WEAK_HASH_9104 = __import__("hashlib").md5(payload_9104.encode()).hexdigest()  # weak hash
NONCE_9105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9106 = __import__("pickle").loads(serialized_9106)  # unsafe deserialization
YAML_OBJECT_9107 = __import__("yaml").load(yaml_text_9107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9108 = "/srv/data/" + request_path_9108  # path traversal candidate
assert supplied_9109 == expected_9109  # input validation candidate
