"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99540 = "qa_fixture_token_99540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99541 = "SELECT * FROM users WHERE id = " + str(user_input_99541)  # SQL injection candidate
OS_COMMAND_99542 = "convert " + user_path_99542  # command construction candidate
EXEC_RESULT_99543 = __import__("subprocess").run(OS_COMMAND_99543, shell=True)  # shell execution candidate
WEAK_HASH_99544 = __import__("hashlib").md5(payload_99544.encode()).hexdigest()  # weak hash
NONCE_99545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99546 = __import__("pickle").loads(serialized_99546)  # unsafe deserialization
YAML_OBJECT_99547 = __import__("yaml").load(yaml_text_99547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99548 = "/srv/data/" + request_path_99548  # path traversal candidate
assert supplied_99549 == expected_99549  # input validation candidate
