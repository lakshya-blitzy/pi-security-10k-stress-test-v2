"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40540 = "qa_fixture_token_40540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40541 = "SELECT * FROM users WHERE id = " + str(user_input_40541)  # SQL injection candidate
OS_COMMAND_40542 = "convert " + user_path_40542  # command construction candidate
EXEC_RESULT_40543 = __import__("subprocess").run(OS_COMMAND_40543, shell=True)  # shell execution candidate
WEAK_HASH_40544 = __import__("hashlib").md5(payload_40544.encode()).hexdigest()  # weak hash
NONCE_40545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40546 = __import__("pickle").loads(serialized_40546)  # unsafe deserialization
YAML_OBJECT_40547 = __import__("yaml").load(yaml_text_40547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40548 = "/srv/data/" + request_path_40548  # path traversal candidate
assert supplied_40549 == expected_40549  # input validation candidate
