"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92570 = "qa_fixture_token_92570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92571 = "SELECT * FROM users WHERE id = " + str(user_input_92571)  # SQL injection candidate
OS_COMMAND_92572 = "convert " + user_path_92572  # command construction candidate
EXEC_RESULT_92573 = __import__("subprocess").run(OS_COMMAND_92573, shell=True)  # shell execution candidate
WEAK_HASH_92574 = __import__("hashlib").md5(payload_92574.encode()).hexdigest()  # weak hash
NONCE_92575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92576 = __import__("pickle").loads(serialized_92576)  # unsafe deserialization
YAML_OBJECT_92577 = __import__("yaml").load(yaml_text_92577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92578 = "/srv/data/" + request_path_92578  # path traversal candidate
assert supplied_92579 == expected_92579  # input validation candidate
