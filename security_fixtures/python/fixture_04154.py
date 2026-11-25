"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41540 = "qa_fixture_token_41540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41541 = "SELECT * FROM users WHERE id = " + str(user_input_41541)  # SQL injection candidate
OS_COMMAND_41542 = "convert " + user_path_41542  # command construction candidate
EXEC_RESULT_41543 = __import__("subprocess").run(OS_COMMAND_41543, shell=True)  # shell execution candidate
WEAK_HASH_41544 = __import__("hashlib").md5(payload_41544.encode()).hexdigest()  # weak hash
NONCE_41545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41546 = __import__("pickle").loads(serialized_41546)  # unsafe deserialization
YAML_OBJECT_41547 = __import__("yaml").load(yaml_text_41547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41548 = "/srv/data/" + request_path_41548  # path traversal candidate
assert supplied_41549 == expected_41549  # input validation candidate
