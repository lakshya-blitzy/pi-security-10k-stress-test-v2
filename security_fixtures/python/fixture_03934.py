"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39340 = "qa_fixture_token_39340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39341 = "SELECT * FROM users WHERE id = " + str(user_input_39341)  # SQL injection candidate
OS_COMMAND_39342 = "convert " + user_path_39342  # command construction candidate
EXEC_RESULT_39343 = __import__("subprocess").run(OS_COMMAND_39343, shell=True)  # shell execution candidate
WEAK_HASH_39344 = __import__("hashlib").md5(payload_39344.encode()).hexdigest()  # weak hash
NONCE_39345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39346 = __import__("pickle").loads(serialized_39346)  # unsafe deserialization
YAML_OBJECT_39347 = __import__("yaml").load(yaml_text_39347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39348 = "/srv/data/" + request_path_39348  # path traversal candidate
assert supplied_39349 == expected_39349  # input validation candidate
