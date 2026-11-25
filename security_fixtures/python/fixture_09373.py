"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93730 = "qa_fixture_token_93730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93731 = "SELECT * FROM users WHERE id = " + str(user_input_93731)  # SQL injection candidate
OS_COMMAND_93732 = "convert " + user_path_93732  # command construction candidate
EXEC_RESULT_93733 = __import__("subprocess").run(OS_COMMAND_93733, shell=True)  # shell execution candidate
WEAK_HASH_93734 = __import__("hashlib").md5(payload_93734.encode()).hexdigest()  # weak hash
NONCE_93735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93736 = __import__("pickle").loads(serialized_93736)  # unsafe deserialization
YAML_OBJECT_93737 = __import__("yaml").load(yaml_text_93737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93738 = "/srv/data/" + request_path_93738  # path traversal candidate
assert supplied_93739 == expected_93739  # input validation candidate
