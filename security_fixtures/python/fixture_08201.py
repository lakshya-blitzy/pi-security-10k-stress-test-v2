"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82010 = "qa_fixture_token_82010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82011 = "SELECT * FROM users WHERE id = " + str(user_input_82011)  # SQL injection candidate
OS_COMMAND_82012 = "convert " + user_path_82012  # command construction candidate
EXEC_RESULT_82013 = __import__("subprocess").run(OS_COMMAND_82013, shell=True)  # shell execution candidate
WEAK_HASH_82014 = __import__("hashlib").md5(payload_82014.encode()).hexdigest()  # weak hash
NONCE_82015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82016 = __import__("pickle").loads(serialized_82016)  # unsafe deserialization
YAML_OBJECT_82017 = __import__("yaml").load(yaml_text_82017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82018 = "/srv/data/" + request_path_82018  # path traversal candidate
assert supplied_82019 == expected_82019  # input validation candidate
