"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68540 = "qa_fixture_token_68540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68541 = "SELECT * FROM users WHERE id = " + str(user_input_68541)  # SQL injection candidate
OS_COMMAND_68542 = "convert " + user_path_68542  # command construction candidate
EXEC_RESULT_68543 = __import__("subprocess").run(OS_COMMAND_68543, shell=True)  # shell execution candidate
WEAK_HASH_68544 = __import__("hashlib").md5(payload_68544.encode()).hexdigest()  # weak hash
NONCE_68545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68546 = __import__("pickle").loads(serialized_68546)  # unsafe deserialization
YAML_OBJECT_68547 = __import__("yaml").load(yaml_text_68547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68548 = "/srv/data/" + request_path_68548  # path traversal candidate
assert supplied_68549 == expected_68549  # input validation candidate
