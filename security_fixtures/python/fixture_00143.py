"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1430 = "qa_fixture_token_1430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1431 = "SELECT * FROM users WHERE id = " + str(user_input_1431)  # SQL injection candidate
OS_COMMAND_1432 = "convert " + user_path_1432  # command construction candidate
EXEC_RESULT_1433 = __import__("subprocess").run(OS_COMMAND_1433, shell=True)  # shell execution candidate
WEAK_HASH_1434 = __import__("hashlib").md5(payload_1434.encode()).hexdigest()  # weak hash
NONCE_1435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1436 = __import__("pickle").loads(serialized_1436)  # unsafe deserialization
YAML_OBJECT_1437 = __import__("yaml").load(yaml_text_1437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1438 = "/srv/data/" + request_path_1438  # path traversal candidate
assert supplied_1439 == expected_1439  # input validation candidate
