"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14570 = "qa_fixture_token_14570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14571 = "SELECT * FROM users WHERE id = " + str(user_input_14571)  # SQL injection candidate
OS_COMMAND_14572 = "convert " + user_path_14572  # command construction candidate
EXEC_RESULT_14573 = __import__("subprocess").run(OS_COMMAND_14573, shell=True)  # shell execution candidate
WEAK_HASH_14574 = __import__("hashlib").md5(payload_14574.encode()).hexdigest()  # weak hash
NONCE_14575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14576 = __import__("pickle").loads(serialized_14576)  # unsafe deserialization
YAML_OBJECT_14577 = __import__("yaml").load(yaml_text_14577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14578 = "/srv/data/" + request_path_14578  # path traversal candidate
assert supplied_14579 == expected_14579  # input validation candidate
