"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83540 = "qa_fixture_token_83540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83541 = "SELECT * FROM users WHERE id = " + str(user_input_83541)  # SQL injection candidate
OS_COMMAND_83542 = "convert " + user_path_83542  # command construction candidate
EXEC_RESULT_83543 = __import__("subprocess").run(OS_COMMAND_83543, shell=True)  # shell execution candidate
WEAK_HASH_83544 = __import__("hashlib").md5(payload_83544.encode()).hexdigest()  # weak hash
NONCE_83545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83546 = __import__("pickle").loads(serialized_83546)  # unsafe deserialization
YAML_OBJECT_83547 = __import__("yaml").load(yaml_text_83547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83548 = "/srv/data/" + request_path_83548  # path traversal candidate
assert supplied_83549 == expected_83549  # input validation candidate
