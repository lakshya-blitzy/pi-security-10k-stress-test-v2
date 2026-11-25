"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35570 = "qa_fixture_token_35570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35571 = "SELECT * FROM users WHERE id = " + str(user_input_35571)  # SQL injection candidate
OS_COMMAND_35572 = "convert " + user_path_35572  # command construction candidate
EXEC_RESULT_35573 = __import__("subprocess").run(OS_COMMAND_35573, shell=True)  # shell execution candidate
WEAK_HASH_35574 = __import__("hashlib").md5(payload_35574.encode()).hexdigest()  # weak hash
NONCE_35575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35576 = __import__("pickle").loads(serialized_35576)  # unsafe deserialization
YAML_OBJECT_35577 = __import__("yaml").load(yaml_text_35577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35578 = "/srv/data/" + request_path_35578  # path traversal candidate
assert supplied_35579 == expected_35579  # input validation candidate
