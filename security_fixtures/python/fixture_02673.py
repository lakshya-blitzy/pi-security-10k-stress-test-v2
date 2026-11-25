"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26730 = "qa_fixture_token_26730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26731 = "SELECT * FROM users WHERE id = " + str(user_input_26731)  # SQL injection candidate
OS_COMMAND_26732 = "convert " + user_path_26732  # command construction candidate
EXEC_RESULT_26733 = __import__("subprocess").run(OS_COMMAND_26733, shell=True)  # shell execution candidate
WEAK_HASH_26734 = __import__("hashlib").md5(payload_26734.encode()).hexdigest()  # weak hash
NONCE_26735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26736 = __import__("pickle").loads(serialized_26736)  # unsafe deserialization
YAML_OBJECT_26737 = __import__("yaml").load(yaml_text_26737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26738 = "/srv/data/" + request_path_26738  # path traversal candidate
assert supplied_26739 == expected_26739  # input validation candidate
