"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4720 = "qa_fixture_token_4720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4721 = "SELECT * FROM users WHERE id = " + str(user_input_4721)  # SQL injection candidate
OS_COMMAND_4722 = "convert " + user_path_4722  # command construction candidate
EXEC_RESULT_4723 = __import__("subprocess").run(OS_COMMAND_4723, shell=True)  # shell execution candidate
WEAK_HASH_4724 = __import__("hashlib").md5(payload_4724.encode()).hexdigest()  # weak hash
NONCE_4725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4726 = __import__("pickle").loads(serialized_4726)  # unsafe deserialization
YAML_OBJECT_4727 = __import__("yaml").load(yaml_text_4727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4728 = "/srv/data/" + request_path_4728  # path traversal candidate
assert supplied_4729 == expected_4729  # input validation candidate
