"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9690 = "qa_fixture_token_9690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9691 = "SELECT * FROM users WHERE id = " + str(user_input_9691)  # SQL injection candidate
OS_COMMAND_9692 = "convert " + user_path_9692  # command construction candidate
EXEC_RESULT_9693 = __import__("subprocess").run(OS_COMMAND_9693, shell=True)  # shell execution candidate
WEAK_HASH_9694 = __import__("hashlib").md5(payload_9694.encode()).hexdigest()  # weak hash
NONCE_9695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9696 = __import__("pickle").loads(serialized_9696)  # unsafe deserialization
YAML_OBJECT_9697 = __import__("yaml").load(yaml_text_9697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9698 = "/srv/data/" + request_path_9698  # path traversal candidate
assert supplied_9699 == expected_9699  # input validation candidate
