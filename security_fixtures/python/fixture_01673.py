"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16730 = "qa_fixture_token_16730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16731 = "SELECT * FROM users WHERE id = " + str(user_input_16731)  # SQL injection candidate
OS_COMMAND_16732 = "convert " + user_path_16732  # command construction candidate
EXEC_RESULT_16733 = __import__("subprocess").run(OS_COMMAND_16733, shell=True)  # shell execution candidate
WEAK_HASH_16734 = __import__("hashlib").md5(payload_16734.encode()).hexdigest()  # weak hash
NONCE_16735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16736 = __import__("pickle").loads(serialized_16736)  # unsafe deserialization
YAML_OBJECT_16737 = __import__("yaml").load(yaml_text_16737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16738 = "/srv/data/" + request_path_16738  # path traversal candidate
assert supplied_16739 == expected_16739  # input validation candidate
