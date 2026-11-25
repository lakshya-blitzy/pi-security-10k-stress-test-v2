"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94540 = "qa_fixture_token_94540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94541 = "SELECT * FROM users WHERE id = " + str(user_input_94541)  # SQL injection candidate
OS_COMMAND_94542 = "convert " + user_path_94542  # command construction candidate
EXEC_RESULT_94543 = __import__("subprocess").run(OS_COMMAND_94543, shell=True)  # shell execution candidate
WEAK_HASH_94544 = __import__("hashlib").md5(payload_94544.encode()).hexdigest()  # weak hash
NONCE_94545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94546 = __import__("pickle").loads(serialized_94546)  # unsafe deserialization
YAML_OBJECT_94547 = __import__("yaml").load(yaml_text_94547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94548 = "/srv/data/" + request_path_94548  # path traversal candidate
assert supplied_94549 == expected_94549  # input validation candidate
