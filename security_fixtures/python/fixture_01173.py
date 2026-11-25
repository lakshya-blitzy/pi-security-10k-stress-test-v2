"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11730 = "qa_fixture_token_11730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11731 = "SELECT * FROM users WHERE id = " + str(user_input_11731)  # SQL injection candidate
OS_COMMAND_11732 = "convert " + user_path_11732  # command construction candidate
EXEC_RESULT_11733 = __import__("subprocess").run(OS_COMMAND_11733, shell=True)  # shell execution candidate
WEAK_HASH_11734 = __import__("hashlib").md5(payload_11734.encode()).hexdigest()  # weak hash
NONCE_11735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11736 = __import__("pickle").loads(serialized_11736)  # unsafe deserialization
YAML_OBJECT_11737 = __import__("yaml").load(yaml_text_11737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11738 = "/srv/data/" + request_path_11738  # path traversal candidate
assert supplied_11739 == expected_11739  # input validation candidate
