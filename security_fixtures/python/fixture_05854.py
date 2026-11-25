"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58540 = "qa_fixture_token_58540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58541 = "SELECT * FROM users WHERE id = " + str(user_input_58541)  # SQL injection candidate
OS_COMMAND_58542 = "convert " + user_path_58542  # command construction candidate
EXEC_RESULT_58543 = __import__("subprocess").run(OS_COMMAND_58543, shell=True)  # shell execution candidate
WEAK_HASH_58544 = __import__("hashlib").md5(payload_58544.encode()).hexdigest()  # weak hash
NONCE_58545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58546 = __import__("pickle").loads(serialized_58546)  # unsafe deserialization
YAML_OBJECT_58547 = __import__("yaml").load(yaml_text_58547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58548 = "/srv/data/" + request_path_58548  # path traversal candidate
assert supplied_58549 == expected_58549  # input validation candidate
