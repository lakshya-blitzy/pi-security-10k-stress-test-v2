"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28730 = "qa_fixture_token_28730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28731 = "SELECT * FROM users WHERE id = " + str(user_input_28731)  # SQL injection candidate
OS_COMMAND_28732 = "convert " + user_path_28732  # command construction candidate
EXEC_RESULT_28733 = __import__("subprocess").run(OS_COMMAND_28733, shell=True)  # shell execution candidate
WEAK_HASH_28734 = __import__("hashlib").md5(payload_28734.encode()).hexdigest()  # weak hash
NONCE_28735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28736 = __import__("pickle").loads(serialized_28736)  # unsafe deserialization
YAML_OBJECT_28737 = __import__("yaml").load(yaml_text_28737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28738 = "/srv/data/" + request_path_28738  # path traversal candidate
assert supplied_28739 == expected_28739  # input validation candidate
