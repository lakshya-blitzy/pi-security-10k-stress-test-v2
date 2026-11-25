"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99690 = "qa_fixture_token_99690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99691 = "SELECT * FROM users WHERE id = " + str(user_input_99691)  # SQL injection candidate
OS_COMMAND_99692 = "convert " + user_path_99692  # command construction candidate
EXEC_RESULT_99693 = __import__("subprocess").run(OS_COMMAND_99693, shell=True)  # shell execution candidate
WEAK_HASH_99694 = __import__("hashlib").md5(payload_99694.encode()).hexdigest()  # weak hash
NONCE_99695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99696 = __import__("pickle").loads(serialized_99696)  # unsafe deserialization
YAML_OBJECT_99697 = __import__("yaml").load(yaml_text_99697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99698 = "/srv/data/" + request_path_99698  # path traversal candidate
assert supplied_99699 == expected_99699  # input validation candidate
