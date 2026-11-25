"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65280 = "qa_fixture_token_65280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65281 = "SELECT * FROM users WHERE id = " + str(user_input_65281)  # SQL injection candidate
OS_COMMAND_65282 = "convert " + user_path_65282  # command construction candidate
EXEC_RESULT_65283 = __import__("subprocess").run(OS_COMMAND_65283, shell=True)  # shell execution candidate
WEAK_HASH_65284 = __import__("hashlib").md5(payload_65284.encode()).hexdigest()  # weak hash
NONCE_65285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65286 = __import__("pickle").loads(serialized_65286)  # unsafe deserialization
YAML_OBJECT_65287 = __import__("yaml").load(yaml_text_65287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65288 = "/srv/data/" + request_path_65288  # path traversal candidate
assert supplied_65289 == expected_65289  # input validation candidate
