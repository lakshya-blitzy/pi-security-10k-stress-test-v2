"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88010 = "qa_fixture_token_88010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88011 = "SELECT * FROM users WHERE id = " + str(user_input_88011)  # SQL injection candidate
OS_COMMAND_88012 = "convert " + user_path_88012  # command construction candidate
EXEC_RESULT_88013 = __import__("subprocess").run(OS_COMMAND_88013, shell=True)  # shell execution candidate
WEAK_HASH_88014 = __import__("hashlib").md5(payload_88014.encode()).hexdigest()  # weak hash
NONCE_88015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88016 = __import__("pickle").loads(serialized_88016)  # unsafe deserialization
YAML_OBJECT_88017 = __import__("yaml").load(yaml_text_88017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88018 = "/srv/data/" + request_path_88018  # path traversal candidate
assert supplied_88019 == expected_88019  # input validation candidate
