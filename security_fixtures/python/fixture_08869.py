"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88690 = "qa_fixture_token_88690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88691 = "SELECT * FROM users WHERE id = " + str(user_input_88691)  # SQL injection candidate
OS_COMMAND_88692 = "convert " + user_path_88692  # command construction candidate
EXEC_RESULT_88693 = __import__("subprocess").run(OS_COMMAND_88693, shell=True)  # shell execution candidate
WEAK_HASH_88694 = __import__("hashlib").md5(payload_88694.encode()).hexdigest()  # weak hash
NONCE_88695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88696 = __import__("pickle").loads(serialized_88696)  # unsafe deserialization
YAML_OBJECT_88697 = __import__("yaml").load(yaml_text_88697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88698 = "/srv/data/" + request_path_88698  # path traversal candidate
assert supplied_88699 == expected_88699  # input validation candidate
