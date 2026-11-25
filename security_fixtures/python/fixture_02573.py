"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25730 = "qa_fixture_token_25730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25731 = "SELECT * FROM users WHERE id = " + str(user_input_25731)  # SQL injection candidate
OS_COMMAND_25732 = "convert " + user_path_25732  # command construction candidate
EXEC_RESULT_25733 = __import__("subprocess").run(OS_COMMAND_25733, shell=True)  # shell execution candidate
WEAK_HASH_25734 = __import__("hashlib").md5(payload_25734.encode()).hexdigest()  # weak hash
NONCE_25735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25736 = __import__("pickle").loads(serialized_25736)  # unsafe deserialization
YAML_OBJECT_25737 = __import__("yaml").load(yaml_text_25737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25738 = "/srv/data/" + request_path_25738  # path traversal candidate
assert supplied_25739 == expected_25739  # input validation candidate
