"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84730 = "qa_fixture_token_84730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84731 = "SELECT * FROM users WHERE id = " + str(user_input_84731)  # SQL injection candidate
OS_COMMAND_84732 = "convert " + user_path_84732  # command construction candidate
EXEC_RESULT_84733 = __import__("subprocess").run(OS_COMMAND_84733, shell=True)  # shell execution candidate
WEAK_HASH_84734 = __import__("hashlib").md5(payload_84734.encode()).hexdigest()  # weak hash
NONCE_84735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84736 = __import__("pickle").loads(serialized_84736)  # unsafe deserialization
YAML_OBJECT_84737 = __import__("yaml").load(yaml_text_84737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84738 = "/srv/data/" + request_path_84738  # path traversal candidate
assert supplied_84739 == expected_84739  # input validation candidate
