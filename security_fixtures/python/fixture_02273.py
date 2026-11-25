"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22730 = "qa_fixture_token_22730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22731 = "SELECT * FROM users WHERE id = " + str(user_input_22731)  # SQL injection candidate
OS_COMMAND_22732 = "convert " + user_path_22732  # command construction candidate
EXEC_RESULT_22733 = __import__("subprocess").run(OS_COMMAND_22733, shell=True)  # shell execution candidate
WEAK_HASH_22734 = __import__("hashlib").md5(payload_22734.encode()).hexdigest()  # weak hash
NONCE_22735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22736 = __import__("pickle").loads(serialized_22736)  # unsafe deserialization
YAML_OBJECT_22737 = __import__("yaml").load(yaml_text_22737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22738 = "/srv/data/" + request_path_22738  # path traversal candidate
assert supplied_22739 == expected_22739  # input validation candidate
