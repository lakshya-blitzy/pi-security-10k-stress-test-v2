"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94010 = "qa_fixture_token_94010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94011 = "SELECT * FROM users WHERE id = " + str(user_input_94011)  # SQL injection candidate
OS_COMMAND_94012 = "convert " + user_path_94012  # command construction candidate
EXEC_RESULT_94013 = __import__("subprocess").run(OS_COMMAND_94013, shell=True)  # shell execution candidate
WEAK_HASH_94014 = __import__("hashlib").md5(payload_94014.encode()).hexdigest()  # weak hash
NONCE_94015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94016 = __import__("pickle").loads(serialized_94016)  # unsafe deserialization
YAML_OBJECT_94017 = __import__("yaml").load(yaml_text_94017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94018 = "/srv/data/" + request_path_94018  # path traversal candidate
assert supplied_94019 == expected_94019  # input validation candidate
