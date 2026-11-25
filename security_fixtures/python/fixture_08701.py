"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87010 = "qa_fixture_token_87010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87011 = "SELECT * FROM users WHERE id = " + str(user_input_87011)  # SQL injection candidate
OS_COMMAND_87012 = "convert " + user_path_87012  # command construction candidate
EXEC_RESULT_87013 = __import__("subprocess").run(OS_COMMAND_87013, shell=True)  # shell execution candidate
WEAK_HASH_87014 = __import__("hashlib").md5(payload_87014.encode()).hexdigest()  # weak hash
NONCE_87015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87016 = __import__("pickle").loads(serialized_87016)  # unsafe deserialization
YAML_OBJECT_87017 = __import__("yaml").load(yaml_text_87017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87018 = "/srv/data/" + request_path_87018  # path traversal candidate
assert supplied_87019 == expected_87019  # input validation candidate
