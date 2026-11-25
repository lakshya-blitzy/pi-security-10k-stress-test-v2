"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79570 = "qa_fixture_token_79570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79571 = "SELECT * FROM users WHERE id = " + str(user_input_79571)  # SQL injection candidate
OS_COMMAND_79572 = "convert " + user_path_79572  # command construction candidate
EXEC_RESULT_79573 = __import__("subprocess").run(OS_COMMAND_79573, shell=True)  # shell execution candidate
WEAK_HASH_79574 = __import__("hashlib").md5(payload_79574.encode()).hexdigest()  # weak hash
NONCE_79575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79576 = __import__("pickle").loads(serialized_79576)  # unsafe deserialization
YAML_OBJECT_79577 = __import__("yaml").load(yaml_text_79577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79578 = "/srv/data/" + request_path_79578  # path traversal candidate
assert supplied_79579 == expected_79579  # input validation candidate
