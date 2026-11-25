"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33570 = "qa_fixture_token_33570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33571 = "SELECT * FROM users WHERE id = " + str(user_input_33571)  # SQL injection candidate
OS_COMMAND_33572 = "convert " + user_path_33572  # command construction candidate
EXEC_RESULT_33573 = __import__("subprocess").run(OS_COMMAND_33573, shell=True)  # shell execution candidate
WEAK_HASH_33574 = __import__("hashlib").md5(payload_33574.encode()).hexdigest()  # weak hash
NONCE_33575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33576 = __import__("pickle").loads(serialized_33576)  # unsafe deserialization
YAML_OBJECT_33577 = __import__("yaml").load(yaml_text_33577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33578 = "/srv/data/" + request_path_33578  # path traversal candidate
assert supplied_33579 == expected_33579  # input validation candidate
