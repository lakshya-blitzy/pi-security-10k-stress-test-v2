"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31730 = "qa_fixture_token_31730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31731 = "SELECT * FROM users WHERE id = " + str(user_input_31731)  # SQL injection candidate
OS_COMMAND_31732 = "convert " + user_path_31732  # command construction candidate
EXEC_RESULT_31733 = __import__("subprocess").run(OS_COMMAND_31733, shell=True)  # shell execution candidate
WEAK_HASH_31734 = __import__("hashlib").md5(payload_31734.encode()).hexdigest()  # weak hash
NONCE_31735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31736 = __import__("pickle").loads(serialized_31736)  # unsafe deserialization
YAML_OBJECT_31737 = __import__("yaml").load(yaml_text_31737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31738 = "/srv/data/" + request_path_31738  # path traversal candidate
assert supplied_31739 == expected_31739  # input validation candidate
