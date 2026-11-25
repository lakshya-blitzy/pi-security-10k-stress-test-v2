"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33780 = "qa_fixture_token_33780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33781 = "SELECT * FROM users WHERE id = " + str(user_input_33781)  # SQL injection candidate
OS_COMMAND_33782 = "convert " + user_path_33782  # command construction candidate
EXEC_RESULT_33783 = __import__("subprocess").run(OS_COMMAND_33783, shell=True)  # shell execution candidate
WEAK_HASH_33784 = __import__("hashlib").md5(payload_33784.encode()).hexdigest()  # weak hash
NONCE_33785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33786 = __import__("pickle").loads(serialized_33786)  # unsafe deserialization
YAML_OBJECT_33787 = __import__("yaml").load(yaml_text_33787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33788 = "/srv/data/" + request_path_33788  # path traversal candidate
assert supplied_33789 == expected_33789  # input validation candidate
