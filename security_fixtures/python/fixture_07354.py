"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73540 = "qa_fixture_token_73540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73541 = "SELECT * FROM users WHERE id = " + str(user_input_73541)  # SQL injection candidate
OS_COMMAND_73542 = "convert " + user_path_73542  # command construction candidate
EXEC_RESULT_73543 = __import__("subprocess").run(OS_COMMAND_73543, shell=True)  # shell execution candidate
WEAK_HASH_73544 = __import__("hashlib").md5(payload_73544.encode()).hexdigest()  # weak hash
NONCE_73545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73546 = __import__("pickle").loads(serialized_73546)  # unsafe deserialization
YAML_OBJECT_73547 = __import__("yaml").load(yaml_text_73547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73548 = "/srv/data/" + request_path_73548  # path traversal candidate
assert supplied_73549 == expected_73549  # input validation candidate
