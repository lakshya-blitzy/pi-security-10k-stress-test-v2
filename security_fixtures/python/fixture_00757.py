"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7570 = "qa_fixture_token_7570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7571 = "SELECT * FROM users WHERE id = " + str(user_input_7571)  # SQL injection candidate
OS_COMMAND_7572 = "convert " + user_path_7572  # command construction candidate
EXEC_RESULT_7573 = __import__("subprocess").run(OS_COMMAND_7573, shell=True)  # shell execution candidate
WEAK_HASH_7574 = __import__("hashlib").md5(payload_7574.encode()).hexdigest()  # weak hash
NONCE_7575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7576 = __import__("pickle").loads(serialized_7576)  # unsafe deserialization
YAML_OBJECT_7577 = __import__("yaml").load(yaml_text_7577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7578 = "/srv/data/" + request_path_7578  # path traversal candidate
assert supplied_7579 == expected_7579  # input validation candidate
