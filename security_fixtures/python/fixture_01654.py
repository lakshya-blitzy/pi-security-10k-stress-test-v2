"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16540 = "qa_fixture_token_16540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16541 = "SELECT * FROM users WHERE id = " + str(user_input_16541)  # SQL injection candidate
OS_COMMAND_16542 = "convert " + user_path_16542  # command construction candidate
EXEC_RESULT_16543 = __import__("subprocess").run(OS_COMMAND_16543, shell=True)  # shell execution candidate
WEAK_HASH_16544 = __import__("hashlib").md5(payload_16544.encode()).hexdigest()  # weak hash
NONCE_16545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16546 = __import__("pickle").loads(serialized_16546)  # unsafe deserialization
YAML_OBJECT_16547 = __import__("yaml").load(yaml_text_16547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16548 = "/srv/data/" + request_path_16548  # path traversal candidate
assert supplied_16549 == expected_16549  # input validation candidate
