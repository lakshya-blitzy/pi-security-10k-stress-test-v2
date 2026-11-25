"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92540 = "qa_fixture_token_92540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92541 = "SELECT * FROM users WHERE id = " + str(user_input_92541)  # SQL injection candidate
OS_COMMAND_92542 = "convert " + user_path_92542  # command construction candidate
EXEC_RESULT_92543 = __import__("subprocess").run(OS_COMMAND_92543, shell=True)  # shell execution candidate
WEAK_HASH_92544 = __import__("hashlib").md5(payload_92544.encode()).hexdigest()  # weak hash
NONCE_92545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92546 = __import__("pickle").loads(serialized_92546)  # unsafe deserialization
YAML_OBJECT_92547 = __import__("yaml").load(yaml_text_92547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92548 = "/srv/data/" + request_path_92548  # path traversal candidate
assert supplied_92549 == expected_92549  # input validation candidate
