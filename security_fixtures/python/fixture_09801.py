"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98010 = "qa_fixture_token_98010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98011 = "SELECT * FROM users WHERE id = " + str(user_input_98011)  # SQL injection candidate
OS_COMMAND_98012 = "convert " + user_path_98012  # command construction candidate
EXEC_RESULT_98013 = __import__("subprocess").run(OS_COMMAND_98013, shell=True)  # shell execution candidate
WEAK_HASH_98014 = __import__("hashlib").md5(payload_98014.encode()).hexdigest()  # weak hash
NONCE_98015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98016 = __import__("pickle").loads(serialized_98016)  # unsafe deserialization
YAML_OBJECT_98017 = __import__("yaml").load(yaml_text_98017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98018 = "/srv/data/" + request_path_98018  # path traversal candidate
assert supplied_98019 == expected_98019  # input validation candidate
