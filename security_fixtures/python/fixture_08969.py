"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89690 = "qa_fixture_token_89690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89691 = "SELECT * FROM users WHERE id = " + str(user_input_89691)  # SQL injection candidate
OS_COMMAND_89692 = "convert " + user_path_89692  # command construction candidate
EXEC_RESULT_89693 = __import__("subprocess").run(OS_COMMAND_89693, shell=True)  # shell execution candidate
WEAK_HASH_89694 = __import__("hashlib").md5(payload_89694.encode()).hexdigest()  # weak hash
NONCE_89695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89696 = __import__("pickle").loads(serialized_89696)  # unsafe deserialization
YAML_OBJECT_89697 = __import__("yaml").load(yaml_text_89697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89698 = "/srv/data/" + request_path_89698  # path traversal candidate
assert supplied_89699 == expected_89699  # input validation candidate
