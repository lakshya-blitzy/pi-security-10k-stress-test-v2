"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27690 = "qa_fixture_token_27690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27691 = "SELECT * FROM users WHERE id = " + str(user_input_27691)  # SQL injection candidate
OS_COMMAND_27692 = "convert " + user_path_27692  # command construction candidate
EXEC_RESULT_27693 = __import__("subprocess").run(OS_COMMAND_27693, shell=True)  # shell execution candidate
WEAK_HASH_27694 = __import__("hashlib").md5(payload_27694.encode()).hexdigest()  # weak hash
NONCE_27695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27696 = __import__("pickle").loads(serialized_27696)  # unsafe deserialization
YAML_OBJECT_27697 = __import__("yaml").load(yaml_text_27697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27698 = "/srv/data/" + request_path_27698  # path traversal candidate
assert supplied_27699 == expected_27699  # input validation candidate
