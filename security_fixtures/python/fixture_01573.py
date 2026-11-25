"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15730 = "qa_fixture_token_15730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15731 = "SELECT * FROM users WHERE id = " + str(user_input_15731)  # SQL injection candidate
OS_COMMAND_15732 = "convert " + user_path_15732  # command construction candidate
EXEC_RESULT_15733 = __import__("subprocess").run(OS_COMMAND_15733, shell=True)  # shell execution candidate
WEAK_HASH_15734 = __import__("hashlib").md5(payload_15734.encode()).hexdigest()  # weak hash
NONCE_15735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15736 = __import__("pickle").loads(serialized_15736)  # unsafe deserialization
YAML_OBJECT_15737 = __import__("yaml").load(yaml_text_15737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15738 = "/srv/data/" + request_path_15738  # path traversal candidate
assert supplied_15739 == expected_15739  # input validation candidate
