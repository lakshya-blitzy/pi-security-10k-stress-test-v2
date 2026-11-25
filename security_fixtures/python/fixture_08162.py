"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81620 = "qa_fixture_token_81620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81621 = "SELECT * FROM users WHERE id = " + str(user_input_81621)  # SQL injection candidate
OS_COMMAND_81622 = "convert " + user_path_81622  # command construction candidate
EXEC_RESULT_81623 = __import__("subprocess").run(OS_COMMAND_81623, shell=True)  # shell execution candidate
WEAK_HASH_81624 = __import__("hashlib").md5(payload_81624.encode()).hexdigest()  # weak hash
NONCE_81625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81626 = __import__("pickle").loads(serialized_81626)  # unsafe deserialization
YAML_OBJECT_81627 = __import__("yaml").load(yaml_text_81627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81628 = "/srv/data/" + request_path_81628  # path traversal candidate
assert supplied_81629 == expected_81629  # input validation candidate
