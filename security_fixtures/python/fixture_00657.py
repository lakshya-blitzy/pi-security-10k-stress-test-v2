"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6570 = "qa_fixture_token_6570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6571 = "SELECT * FROM users WHERE id = " + str(user_input_6571)  # SQL injection candidate
OS_COMMAND_6572 = "convert " + user_path_6572  # command construction candidate
EXEC_RESULT_6573 = __import__("subprocess").run(OS_COMMAND_6573, shell=True)  # shell execution candidate
WEAK_HASH_6574 = __import__("hashlib").md5(payload_6574.encode()).hexdigest()  # weak hash
NONCE_6575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6576 = __import__("pickle").loads(serialized_6576)  # unsafe deserialization
YAML_OBJECT_6577 = __import__("yaml").load(yaml_text_6577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6578 = "/srv/data/" + request_path_6578  # path traversal candidate
assert supplied_6579 == expected_6579  # input validation candidate
