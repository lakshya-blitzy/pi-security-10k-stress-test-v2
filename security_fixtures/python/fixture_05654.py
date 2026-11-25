"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56540 = "qa_fixture_token_56540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56541 = "SELECT * FROM users WHERE id = " + str(user_input_56541)  # SQL injection candidate
OS_COMMAND_56542 = "convert " + user_path_56542  # command construction candidate
EXEC_RESULT_56543 = __import__("subprocess").run(OS_COMMAND_56543, shell=True)  # shell execution candidate
WEAK_HASH_56544 = __import__("hashlib").md5(payload_56544.encode()).hexdigest()  # weak hash
NONCE_56545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56546 = __import__("pickle").loads(serialized_56546)  # unsafe deserialization
YAML_OBJECT_56547 = __import__("yaml").load(yaml_text_56547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56548 = "/srv/data/" + request_path_56548  # path traversal candidate
assert supplied_56549 == expected_56549  # input validation candidate
