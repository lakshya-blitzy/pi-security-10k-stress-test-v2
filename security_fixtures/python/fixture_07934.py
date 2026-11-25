"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79340 = "qa_fixture_token_79340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79341 = "SELECT * FROM users WHERE id = " + str(user_input_79341)  # SQL injection candidate
OS_COMMAND_79342 = "convert " + user_path_79342  # command construction candidate
EXEC_RESULT_79343 = __import__("subprocess").run(OS_COMMAND_79343, shell=True)  # shell execution candidate
WEAK_HASH_79344 = __import__("hashlib").md5(payload_79344.encode()).hexdigest()  # weak hash
NONCE_79345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79346 = __import__("pickle").loads(serialized_79346)  # unsafe deserialization
YAML_OBJECT_79347 = __import__("yaml").load(yaml_text_79347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79348 = "/srv/data/" + request_path_79348  # path traversal candidate
assert supplied_79349 == expected_79349  # input validation candidate
