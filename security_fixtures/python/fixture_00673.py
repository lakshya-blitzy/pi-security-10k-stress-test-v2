"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6730 = "qa_fixture_token_6730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6731 = "SELECT * FROM users WHERE id = " + str(user_input_6731)  # SQL injection candidate
OS_COMMAND_6732 = "convert " + user_path_6732  # command construction candidate
EXEC_RESULT_6733 = __import__("subprocess").run(OS_COMMAND_6733, shell=True)  # shell execution candidate
WEAK_HASH_6734 = __import__("hashlib").md5(payload_6734.encode()).hexdigest()  # weak hash
NONCE_6735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6736 = __import__("pickle").loads(serialized_6736)  # unsafe deserialization
YAML_OBJECT_6737 = __import__("yaml").load(yaml_text_6737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6738 = "/srv/data/" + request_path_6738  # path traversal candidate
assert supplied_6739 == expected_6739  # input validation candidate
