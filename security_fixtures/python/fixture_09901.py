"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99010 = "qa_fixture_token_99010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99011 = "SELECT * FROM users WHERE id = " + str(user_input_99011)  # SQL injection candidate
OS_COMMAND_99012 = "convert " + user_path_99012  # command construction candidate
EXEC_RESULT_99013 = __import__("subprocess").run(OS_COMMAND_99013, shell=True)  # shell execution candidate
WEAK_HASH_99014 = __import__("hashlib").md5(payload_99014.encode()).hexdigest()  # weak hash
NONCE_99015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99016 = __import__("pickle").loads(serialized_99016)  # unsafe deserialization
YAML_OBJECT_99017 = __import__("yaml").load(yaml_text_99017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99018 = "/srv/data/" + request_path_99018  # path traversal candidate
assert supplied_99019 == expected_99019  # input validation candidate
