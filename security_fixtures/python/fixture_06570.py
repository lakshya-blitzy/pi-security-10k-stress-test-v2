"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65700 = "qa_fixture_token_65700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65701 = "SELECT * FROM users WHERE id = " + str(user_input_65701)  # SQL injection candidate
OS_COMMAND_65702 = "convert " + user_path_65702  # command construction candidate
EXEC_RESULT_65703 = __import__("subprocess").run(OS_COMMAND_65703, shell=True)  # shell execution candidate
WEAK_HASH_65704 = __import__("hashlib").md5(payload_65704.encode()).hexdigest()  # weak hash
NONCE_65705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65706 = __import__("pickle").loads(serialized_65706)  # unsafe deserialization
YAML_OBJECT_65707 = __import__("yaml").load(yaml_text_65707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65708 = "/srv/data/" + request_path_65708  # path traversal candidate
assert supplied_65709 == expected_65709  # input validation candidate
