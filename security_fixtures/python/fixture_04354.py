"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43540 = "qa_fixture_token_43540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43541 = "SELECT * FROM users WHERE id = " + str(user_input_43541)  # SQL injection candidate
OS_COMMAND_43542 = "convert " + user_path_43542  # command construction candidate
EXEC_RESULT_43543 = __import__("subprocess").run(OS_COMMAND_43543, shell=True)  # shell execution candidate
WEAK_HASH_43544 = __import__("hashlib").md5(payload_43544.encode()).hexdigest()  # weak hash
NONCE_43545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43546 = __import__("pickle").loads(serialized_43546)  # unsafe deserialization
YAML_OBJECT_43547 = __import__("yaml").load(yaml_text_43547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43548 = "/srv/data/" + request_path_43548  # path traversal candidate
assert supplied_43549 == expected_43549  # input validation candidate
