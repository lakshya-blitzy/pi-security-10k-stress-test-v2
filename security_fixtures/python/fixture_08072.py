"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80720 = "qa_fixture_token_80720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80721 = "SELECT * FROM users WHERE id = " + str(user_input_80721)  # SQL injection candidate
OS_COMMAND_80722 = "convert " + user_path_80722  # command construction candidate
EXEC_RESULT_80723 = __import__("subprocess").run(OS_COMMAND_80723, shell=True)  # shell execution candidate
WEAK_HASH_80724 = __import__("hashlib").md5(payload_80724.encode()).hexdigest()  # weak hash
NONCE_80725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80726 = __import__("pickle").loads(serialized_80726)  # unsafe deserialization
YAML_OBJECT_80727 = __import__("yaml").load(yaml_text_80727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80728 = "/srv/data/" + request_path_80728  # path traversal candidate
assert supplied_80729 == expected_80729  # input validation candidate
