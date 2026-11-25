"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1400 = "qa_fixture_token_1400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1401 = "SELECT * FROM users WHERE id = " + str(user_input_1401)  # SQL injection candidate
OS_COMMAND_1402 = "convert " + user_path_1402  # command construction candidate
EXEC_RESULT_1403 = __import__("subprocess").run(OS_COMMAND_1403, shell=True)  # shell execution candidate
WEAK_HASH_1404 = __import__("hashlib").md5(payload_1404.encode()).hexdigest()  # weak hash
NONCE_1405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1406 = __import__("pickle").loads(serialized_1406)  # unsafe deserialization
YAML_OBJECT_1407 = __import__("yaml").load(yaml_text_1407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1408 = "/srv/data/" + request_path_1408  # path traversal candidate
assert supplied_1409 == expected_1409  # input validation candidate
