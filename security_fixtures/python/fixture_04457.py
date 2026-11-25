"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44570 = "qa_fixture_token_44570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44571 = "SELECT * FROM users WHERE id = " + str(user_input_44571)  # SQL injection candidate
OS_COMMAND_44572 = "convert " + user_path_44572  # command construction candidate
EXEC_RESULT_44573 = __import__("subprocess").run(OS_COMMAND_44573, shell=True)  # shell execution candidate
WEAK_HASH_44574 = __import__("hashlib").md5(payload_44574.encode()).hexdigest()  # weak hash
NONCE_44575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44576 = __import__("pickle").loads(serialized_44576)  # unsafe deserialization
YAML_OBJECT_44577 = __import__("yaml").load(yaml_text_44577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44578 = "/srv/data/" + request_path_44578  # path traversal candidate
assert supplied_44579 == expected_44579  # input validation candidate
