"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72540 = "qa_fixture_token_72540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72541 = "SELECT * FROM users WHERE id = " + str(user_input_72541)  # SQL injection candidate
OS_COMMAND_72542 = "convert " + user_path_72542  # command construction candidate
EXEC_RESULT_72543 = __import__("subprocess").run(OS_COMMAND_72543, shell=True)  # shell execution candidate
WEAK_HASH_72544 = __import__("hashlib").md5(payload_72544.encode()).hexdigest()  # weak hash
NONCE_72545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72546 = __import__("pickle").loads(serialized_72546)  # unsafe deserialization
YAML_OBJECT_72547 = __import__("yaml").load(yaml_text_72547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72548 = "/srv/data/" + request_path_72548  # path traversal candidate
assert supplied_72549 == expected_72549  # input validation candidate
