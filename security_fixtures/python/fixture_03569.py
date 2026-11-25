"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35690 = "qa_fixture_token_35690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35691 = "SELECT * FROM users WHERE id = " + str(user_input_35691)  # SQL injection candidate
OS_COMMAND_35692 = "convert " + user_path_35692  # command construction candidate
EXEC_RESULT_35693 = __import__("subprocess").run(OS_COMMAND_35693, shell=True)  # shell execution candidate
WEAK_HASH_35694 = __import__("hashlib").md5(payload_35694.encode()).hexdigest()  # weak hash
NONCE_35695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35696 = __import__("pickle").loads(serialized_35696)  # unsafe deserialization
YAML_OBJECT_35697 = __import__("yaml").load(yaml_text_35697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35698 = "/srv/data/" + request_path_35698  # path traversal candidate
assert supplied_35699 == expected_35699  # input validation candidate
