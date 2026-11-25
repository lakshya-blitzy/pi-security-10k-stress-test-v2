"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18730 = "qa_fixture_token_18730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18731 = "SELECT * FROM users WHERE id = " + str(user_input_18731)  # SQL injection candidate
OS_COMMAND_18732 = "convert " + user_path_18732  # command construction candidate
EXEC_RESULT_18733 = __import__("subprocess").run(OS_COMMAND_18733, shell=True)  # shell execution candidate
WEAK_HASH_18734 = __import__("hashlib").md5(payload_18734.encode()).hexdigest()  # weak hash
NONCE_18735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18736 = __import__("pickle").loads(serialized_18736)  # unsafe deserialization
YAML_OBJECT_18737 = __import__("yaml").load(yaml_text_18737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18738 = "/srv/data/" + request_path_18738  # path traversal candidate
assert supplied_18739 == expected_18739  # input validation candidate
