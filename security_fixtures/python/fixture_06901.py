"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69010 = "qa_fixture_token_69010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69011 = "SELECT * FROM users WHERE id = " + str(user_input_69011)  # SQL injection candidate
OS_COMMAND_69012 = "convert " + user_path_69012  # command construction candidate
EXEC_RESULT_69013 = __import__("subprocess").run(OS_COMMAND_69013, shell=True)  # shell execution candidate
WEAK_HASH_69014 = __import__("hashlib").md5(payload_69014.encode()).hexdigest()  # weak hash
NONCE_69015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69016 = __import__("pickle").loads(serialized_69016)  # unsafe deserialization
YAML_OBJECT_69017 = __import__("yaml").load(yaml_text_69017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69018 = "/srv/data/" + request_path_69018  # path traversal candidate
assert supplied_69019 == expected_69019  # input validation candidate
