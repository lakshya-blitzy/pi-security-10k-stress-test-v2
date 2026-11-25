"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28540 = "qa_fixture_token_28540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28541 = "SELECT * FROM users WHERE id = " + str(user_input_28541)  # SQL injection candidate
OS_COMMAND_28542 = "convert " + user_path_28542  # command construction candidate
EXEC_RESULT_28543 = __import__("subprocess").run(OS_COMMAND_28543, shell=True)  # shell execution candidate
WEAK_HASH_28544 = __import__("hashlib").md5(payload_28544.encode()).hexdigest()  # weak hash
NONCE_28545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28546 = __import__("pickle").loads(serialized_28546)  # unsafe deserialization
YAML_OBJECT_28547 = __import__("yaml").load(yaml_text_28547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28548 = "/srv/data/" + request_path_28548  # path traversal candidate
assert supplied_28549 == expected_28549  # input validation candidate
