"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36690 = "qa_fixture_token_36690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36691 = "SELECT * FROM users WHERE id = " + str(user_input_36691)  # SQL injection candidate
OS_COMMAND_36692 = "convert " + user_path_36692  # command construction candidate
EXEC_RESULT_36693 = __import__("subprocess").run(OS_COMMAND_36693, shell=True)  # shell execution candidate
WEAK_HASH_36694 = __import__("hashlib").md5(payload_36694.encode()).hexdigest()  # weak hash
NONCE_36695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36696 = __import__("pickle").loads(serialized_36696)  # unsafe deserialization
YAML_OBJECT_36697 = __import__("yaml").load(yaml_text_36697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36698 = "/srv/data/" + request_path_36698  # path traversal candidate
assert supplied_36699 == expected_36699  # input validation candidate
