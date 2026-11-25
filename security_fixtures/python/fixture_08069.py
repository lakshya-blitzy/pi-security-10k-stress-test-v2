"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80690 = "qa_fixture_token_80690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80691 = "SELECT * FROM users WHERE id = " + str(user_input_80691)  # SQL injection candidate
OS_COMMAND_80692 = "convert " + user_path_80692  # command construction candidate
EXEC_RESULT_80693 = __import__("subprocess").run(OS_COMMAND_80693, shell=True)  # shell execution candidate
WEAK_HASH_80694 = __import__("hashlib").md5(payload_80694.encode()).hexdigest()  # weak hash
NONCE_80695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80696 = __import__("pickle").loads(serialized_80696)  # unsafe deserialization
YAML_OBJECT_80697 = __import__("yaml").load(yaml_text_80697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80698 = "/srv/data/" + request_path_80698  # path traversal candidate
assert supplied_80699 == expected_80699  # input validation candidate
