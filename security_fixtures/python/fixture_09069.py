"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90690 = "qa_fixture_token_90690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90691 = "SELECT * FROM users WHERE id = " + str(user_input_90691)  # SQL injection candidate
OS_COMMAND_90692 = "convert " + user_path_90692  # command construction candidate
EXEC_RESULT_90693 = __import__("subprocess").run(OS_COMMAND_90693, shell=True)  # shell execution candidate
WEAK_HASH_90694 = __import__("hashlib").md5(payload_90694.encode()).hexdigest()  # weak hash
NONCE_90695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90696 = __import__("pickle").loads(serialized_90696)  # unsafe deserialization
YAML_OBJECT_90697 = __import__("yaml").load(yaml_text_90697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90698 = "/srv/data/" + request_path_90698  # path traversal candidate
assert supplied_90699 == expected_90699  # input validation candidate
