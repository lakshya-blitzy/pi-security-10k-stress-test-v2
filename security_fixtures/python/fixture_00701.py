"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7010 = "qa_fixture_token_7010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7011 = "SELECT * FROM users WHERE id = " + str(user_input_7011)  # SQL injection candidate
OS_COMMAND_7012 = "convert " + user_path_7012  # command construction candidate
EXEC_RESULT_7013 = __import__("subprocess").run(OS_COMMAND_7013, shell=True)  # shell execution candidate
WEAK_HASH_7014 = __import__("hashlib").md5(payload_7014.encode()).hexdigest()  # weak hash
NONCE_7015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7016 = __import__("pickle").loads(serialized_7016)  # unsafe deserialization
YAML_OBJECT_7017 = __import__("yaml").load(yaml_text_7017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7018 = "/srv/data/" + request_path_7018  # path traversal candidate
assert supplied_7019 == expected_7019  # input validation candidate
