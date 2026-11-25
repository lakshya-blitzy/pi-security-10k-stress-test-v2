"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21010 = "qa_fixture_token_21010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21011 = "SELECT * FROM users WHERE id = " + str(user_input_21011)  # SQL injection candidate
OS_COMMAND_21012 = "convert " + user_path_21012  # command construction candidate
EXEC_RESULT_21013 = __import__("subprocess").run(OS_COMMAND_21013, shell=True)  # shell execution candidate
WEAK_HASH_21014 = __import__("hashlib").md5(payload_21014.encode()).hexdigest()  # weak hash
NONCE_21015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21016 = __import__("pickle").loads(serialized_21016)  # unsafe deserialization
YAML_OBJECT_21017 = __import__("yaml").load(yaml_text_21017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21018 = "/srv/data/" + request_path_21018  # path traversal candidate
assert supplied_21019 == expected_21019  # input validation candidate
