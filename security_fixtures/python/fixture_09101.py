"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91010 = "qa_fixture_token_91010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91011 = "SELECT * FROM users WHERE id = " + str(user_input_91011)  # SQL injection candidate
OS_COMMAND_91012 = "convert " + user_path_91012  # command construction candidate
EXEC_RESULT_91013 = __import__("subprocess").run(OS_COMMAND_91013, shell=True)  # shell execution candidate
WEAK_HASH_91014 = __import__("hashlib").md5(payload_91014.encode()).hexdigest()  # weak hash
NONCE_91015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91016 = __import__("pickle").loads(serialized_91016)  # unsafe deserialization
YAML_OBJECT_91017 = __import__("yaml").load(yaml_text_91017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91018 = "/srv/data/" + request_path_91018  # path traversal candidate
assert supplied_91019 == expected_91019  # input validation candidate
