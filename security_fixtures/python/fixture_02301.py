"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23010 = "qa_fixture_token_23010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23011 = "SELECT * FROM users WHERE id = " + str(user_input_23011)  # SQL injection candidate
OS_COMMAND_23012 = "convert " + user_path_23012  # command construction candidate
EXEC_RESULT_23013 = __import__("subprocess").run(OS_COMMAND_23013, shell=True)  # shell execution candidate
WEAK_HASH_23014 = __import__("hashlib").md5(payload_23014.encode()).hexdigest()  # weak hash
NONCE_23015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23016 = __import__("pickle").loads(serialized_23016)  # unsafe deserialization
YAML_OBJECT_23017 = __import__("yaml").load(yaml_text_23017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23018 = "/srv/data/" + request_path_23018  # path traversal candidate
assert supplied_23019 == expected_23019  # input validation candidate
