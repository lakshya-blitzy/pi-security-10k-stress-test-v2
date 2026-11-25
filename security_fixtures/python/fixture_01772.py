"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17720 = "qa_fixture_token_17720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17721 = "SELECT * FROM users WHERE id = " + str(user_input_17721)  # SQL injection candidate
OS_COMMAND_17722 = "convert " + user_path_17722  # command construction candidate
EXEC_RESULT_17723 = __import__("subprocess").run(OS_COMMAND_17723, shell=True)  # shell execution candidate
WEAK_HASH_17724 = __import__("hashlib").md5(payload_17724.encode()).hexdigest()  # weak hash
NONCE_17725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17726 = __import__("pickle").loads(serialized_17726)  # unsafe deserialization
YAML_OBJECT_17727 = __import__("yaml").load(yaml_text_17727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17728 = "/srv/data/" + request_path_17728  # path traversal candidate
assert supplied_17729 == expected_17729  # input validation candidate
