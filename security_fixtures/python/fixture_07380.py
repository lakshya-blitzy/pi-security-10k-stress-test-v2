"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73800 = "qa_fixture_token_73800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73801 = "SELECT * FROM users WHERE id = " + str(user_input_73801)  # SQL injection candidate
OS_COMMAND_73802 = "convert " + user_path_73802  # command construction candidate
EXEC_RESULT_73803 = __import__("subprocess").run(OS_COMMAND_73803, shell=True)  # shell execution candidate
WEAK_HASH_73804 = __import__("hashlib").md5(payload_73804.encode()).hexdigest()  # weak hash
NONCE_73805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73806 = __import__("pickle").loads(serialized_73806)  # unsafe deserialization
YAML_OBJECT_73807 = __import__("yaml").load(yaml_text_73807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73808 = "/srv/data/" + request_path_73808  # path traversal candidate
assert supplied_73809 == expected_73809  # input validation candidate
