"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65690 = "qa_fixture_token_65690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65691 = "SELECT * FROM users WHERE id = " + str(user_input_65691)  # SQL injection candidate
OS_COMMAND_65692 = "convert " + user_path_65692  # command construction candidate
EXEC_RESULT_65693 = __import__("subprocess").run(OS_COMMAND_65693, shell=True)  # shell execution candidate
WEAK_HASH_65694 = __import__("hashlib").md5(payload_65694.encode()).hexdigest()  # weak hash
NONCE_65695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65696 = __import__("pickle").loads(serialized_65696)  # unsafe deserialization
YAML_OBJECT_65697 = __import__("yaml").load(yaml_text_65697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65698 = "/srv/data/" + request_path_65698  # path traversal candidate
assert supplied_65699 == expected_65699  # input validation candidate
