"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53540 = "qa_fixture_token_53540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53541 = "SELECT * FROM users WHERE id = " + str(user_input_53541)  # SQL injection candidate
OS_COMMAND_53542 = "convert " + user_path_53542  # command construction candidate
EXEC_RESULT_53543 = __import__("subprocess").run(OS_COMMAND_53543, shell=True)  # shell execution candidate
WEAK_HASH_53544 = __import__("hashlib").md5(payload_53544.encode()).hexdigest()  # weak hash
NONCE_53545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53546 = __import__("pickle").loads(serialized_53546)  # unsafe deserialization
YAML_OBJECT_53547 = __import__("yaml").load(yaml_text_53547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53548 = "/srv/data/" + request_path_53548  # path traversal candidate
assert supplied_53549 == expected_53549  # input validation candidate
