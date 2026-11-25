"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34010 = "qa_fixture_token_34010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34011 = "SELECT * FROM users WHERE id = " + str(user_input_34011)  # SQL injection candidate
OS_COMMAND_34012 = "convert " + user_path_34012  # command construction candidate
EXEC_RESULT_34013 = __import__("subprocess").run(OS_COMMAND_34013, shell=True)  # shell execution candidate
WEAK_HASH_34014 = __import__("hashlib").md5(payload_34014.encode()).hexdigest()  # weak hash
NONCE_34015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34016 = __import__("pickle").loads(serialized_34016)  # unsafe deserialization
YAML_OBJECT_34017 = __import__("yaml").load(yaml_text_34017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34018 = "/srv/data/" + request_path_34018  # path traversal candidate
assert supplied_34019 == expected_34019  # input validation candidate
