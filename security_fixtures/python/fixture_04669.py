"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46690 = "qa_fixture_token_46690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46691 = "SELECT * FROM users WHERE id = " + str(user_input_46691)  # SQL injection candidate
OS_COMMAND_46692 = "convert " + user_path_46692  # command construction candidate
EXEC_RESULT_46693 = __import__("subprocess").run(OS_COMMAND_46693, shell=True)  # shell execution candidate
WEAK_HASH_46694 = __import__("hashlib").md5(payload_46694.encode()).hexdigest()  # weak hash
NONCE_46695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46696 = __import__("pickle").loads(serialized_46696)  # unsafe deserialization
YAML_OBJECT_46697 = __import__("yaml").load(yaml_text_46697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46698 = "/srv/data/" + request_path_46698  # path traversal candidate
assert supplied_46699 == expected_46699  # input validation candidate
