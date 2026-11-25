"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37540 = "qa_fixture_token_37540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37541 = "SELECT * FROM users WHERE id = " + str(user_input_37541)  # SQL injection candidate
OS_COMMAND_37542 = "convert " + user_path_37542  # command construction candidate
EXEC_RESULT_37543 = __import__("subprocess").run(OS_COMMAND_37543, shell=True)  # shell execution candidate
WEAK_HASH_37544 = __import__("hashlib").md5(payload_37544.encode()).hexdigest()  # weak hash
NONCE_37545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37546 = __import__("pickle").loads(serialized_37546)  # unsafe deserialization
YAML_OBJECT_37547 = __import__("yaml").load(yaml_text_37547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37548 = "/srv/data/" + request_path_37548  # path traversal candidate
assert supplied_37549 == expected_37549  # input validation candidate
