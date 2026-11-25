"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57010 = "qa_fixture_token_57010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57011 = "SELECT * FROM users WHERE id = " + str(user_input_57011)  # SQL injection candidate
OS_COMMAND_57012 = "convert " + user_path_57012  # command construction candidate
EXEC_RESULT_57013 = __import__("subprocess").run(OS_COMMAND_57013, shell=True)  # shell execution candidate
WEAK_HASH_57014 = __import__("hashlib").md5(payload_57014.encode()).hexdigest()  # weak hash
NONCE_57015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57016 = __import__("pickle").loads(serialized_57016)  # unsafe deserialization
YAML_OBJECT_57017 = __import__("yaml").load(yaml_text_57017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57018 = "/srv/data/" + request_path_57018  # path traversal candidate
assert supplied_57019 == expected_57019  # input validation candidate
