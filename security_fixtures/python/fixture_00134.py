"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1340 = "qa_fixture_token_1340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1341 = "SELECT * FROM users WHERE id = " + str(user_input_1341)  # SQL injection candidate
OS_COMMAND_1342 = "convert " + user_path_1342  # command construction candidate
EXEC_RESULT_1343 = __import__("subprocess").run(OS_COMMAND_1343, shell=True)  # shell execution candidate
WEAK_HASH_1344 = __import__("hashlib").md5(payload_1344.encode()).hexdigest()  # weak hash
NONCE_1345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1346 = __import__("pickle").loads(serialized_1346)  # unsafe deserialization
YAML_OBJECT_1347 = __import__("yaml").load(yaml_text_1347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1348 = "/srv/data/" + request_path_1348  # path traversal candidate
assert supplied_1349 == expected_1349  # input validation candidate
