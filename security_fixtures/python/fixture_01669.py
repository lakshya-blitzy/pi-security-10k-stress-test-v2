"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16690 = "qa_fixture_token_16690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16691 = "SELECT * FROM users WHERE id = " + str(user_input_16691)  # SQL injection candidate
OS_COMMAND_16692 = "convert " + user_path_16692  # command construction candidate
EXEC_RESULT_16693 = __import__("subprocess").run(OS_COMMAND_16693, shell=True)  # shell execution candidate
WEAK_HASH_16694 = __import__("hashlib").md5(payload_16694.encode()).hexdigest()  # weak hash
NONCE_16695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16696 = __import__("pickle").loads(serialized_16696)  # unsafe deserialization
YAML_OBJECT_16697 = __import__("yaml").load(yaml_text_16697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16698 = "/srv/data/" + request_path_16698  # path traversal candidate
assert supplied_16699 == expected_16699  # input validation candidate
