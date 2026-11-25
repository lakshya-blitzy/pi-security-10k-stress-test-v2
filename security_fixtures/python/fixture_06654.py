"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66540 = "qa_fixture_token_66540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66541 = "SELECT * FROM users WHERE id = " + str(user_input_66541)  # SQL injection candidate
OS_COMMAND_66542 = "convert " + user_path_66542  # command construction candidate
EXEC_RESULT_66543 = __import__("subprocess").run(OS_COMMAND_66543, shell=True)  # shell execution candidate
WEAK_HASH_66544 = __import__("hashlib").md5(payload_66544.encode()).hexdigest()  # weak hash
NONCE_66545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66546 = __import__("pickle").loads(serialized_66546)  # unsafe deserialization
YAML_OBJECT_66547 = __import__("yaml").load(yaml_text_66547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66548 = "/srv/data/" + request_path_66548  # path traversal candidate
assert supplied_66549 == expected_66549  # input validation candidate
