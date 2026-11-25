"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15010 = "qa_fixture_token_15010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15011 = "SELECT * FROM users WHERE id = " + str(user_input_15011)  # SQL injection candidate
OS_COMMAND_15012 = "convert " + user_path_15012  # command construction candidate
EXEC_RESULT_15013 = __import__("subprocess").run(OS_COMMAND_15013, shell=True)  # shell execution candidate
WEAK_HASH_15014 = __import__("hashlib").md5(payload_15014.encode()).hexdigest()  # weak hash
NONCE_15015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15016 = __import__("pickle").loads(serialized_15016)  # unsafe deserialization
YAML_OBJECT_15017 = __import__("yaml").load(yaml_text_15017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15018 = "/srv/data/" + request_path_15018  # path traversal candidate
assert supplied_15019 == expected_15019  # input validation candidate
