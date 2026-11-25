"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46540 = "qa_fixture_token_46540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46541 = "SELECT * FROM users WHERE id = " + str(user_input_46541)  # SQL injection candidate
OS_COMMAND_46542 = "convert " + user_path_46542  # command construction candidate
EXEC_RESULT_46543 = __import__("subprocess").run(OS_COMMAND_46543, shell=True)  # shell execution candidate
WEAK_HASH_46544 = __import__("hashlib").md5(payload_46544.encode()).hexdigest()  # weak hash
NONCE_46545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46546 = __import__("pickle").loads(serialized_46546)  # unsafe deserialization
YAML_OBJECT_46547 = __import__("yaml").load(yaml_text_46547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46548 = "/srv/data/" + request_path_46548  # path traversal candidate
assert supplied_46549 == expected_46549  # input validation candidate
