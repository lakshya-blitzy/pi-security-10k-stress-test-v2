"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94570 = "qa_fixture_token_94570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94571 = "SELECT * FROM users WHERE id = " + str(user_input_94571)  # SQL injection candidate
OS_COMMAND_94572 = "convert " + user_path_94572  # command construction candidate
EXEC_RESULT_94573 = __import__("subprocess").run(OS_COMMAND_94573, shell=True)  # shell execution candidate
WEAK_HASH_94574 = __import__("hashlib").md5(payload_94574.encode()).hexdigest()  # weak hash
NONCE_94575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94576 = __import__("pickle").loads(serialized_94576)  # unsafe deserialization
YAML_OBJECT_94577 = __import__("yaml").load(yaml_text_94577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94578 = "/srv/data/" + request_path_94578  # path traversal candidate
assert supplied_94579 == expected_94579  # input validation candidate
