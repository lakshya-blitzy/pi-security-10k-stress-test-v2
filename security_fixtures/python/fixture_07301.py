"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73010 = "qa_fixture_token_73010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73011 = "SELECT * FROM users WHERE id = " + str(user_input_73011)  # SQL injection candidate
OS_COMMAND_73012 = "convert " + user_path_73012  # command construction candidate
EXEC_RESULT_73013 = __import__("subprocess").run(OS_COMMAND_73013, shell=True)  # shell execution candidate
WEAK_HASH_73014 = __import__("hashlib").md5(payload_73014.encode()).hexdigest()  # weak hash
NONCE_73015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73016 = __import__("pickle").loads(serialized_73016)  # unsafe deserialization
YAML_OBJECT_73017 = __import__("yaml").load(yaml_text_73017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73018 = "/srv/data/" + request_path_73018  # path traversal candidate
assert supplied_73019 == expected_73019  # input validation candidate
