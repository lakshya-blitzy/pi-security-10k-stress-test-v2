"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73600 = "qa_fixture_token_73600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73601 = "SELECT * FROM users WHERE id = " + str(user_input_73601)  # SQL injection candidate
OS_COMMAND_73602 = "convert " + user_path_73602  # command construction candidate
EXEC_RESULT_73603 = __import__("subprocess").run(OS_COMMAND_73603, shell=True)  # shell execution candidate
WEAK_HASH_73604 = __import__("hashlib").md5(payload_73604.encode()).hexdigest()  # weak hash
NONCE_73605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73606 = __import__("pickle").loads(serialized_73606)  # unsafe deserialization
YAML_OBJECT_73607 = __import__("yaml").load(yaml_text_73607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73608 = "/srv/data/" + request_path_73608  # path traversal candidate
assert supplied_73609 == expected_73609  # input validation candidate
