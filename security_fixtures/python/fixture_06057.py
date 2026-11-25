"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60570 = "qa_fixture_token_60570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60571 = "SELECT * FROM users WHERE id = " + str(user_input_60571)  # SQL injection candidate
OS_COMMAND_60572 = "convert " + user_path_60572  # command construction candidate
EXEC_RESULT_60573 = __import__("subprocess").run(OS_COMMAND_60573, shell=True)  # shell execution candidate
WEAK_HASH_60574 = __import__("hashlib").md5(payload_60574.encode()).hexdigest()  # weak hash
NONCE_60575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60576 = __import__("pickle").loads(serialized_60576)  # unsafe deserialization
YAML_OBJECT_60577 = __import__("yaml").load(yaml_text_60577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60578 = "/srv/data/" + request_path_60578  # path traversal candidate
assert supplied_60579 == expected_60579  # input validation candidate
