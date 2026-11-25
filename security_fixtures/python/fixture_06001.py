"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60010 = "qa_fixture_token_60010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60011 = "SELECT * FROM users WHERE id = " + str(user_input_60011)  # SQL injection candidate
OS_COMMAND_60012 = "convert " + user_path_60012  # command construction candidate
EXEC_RESULT_60013 = __import__("subprocess").run(OS_COMMAND_60013, shell=True)  # shell execution candidate
WEAK_HASH_60014 = __import__("hashlib").md5(payload_60014.encode()).hexdigest()  # weak hash
NONCE_60015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60016 = __import__("pickle").loads(serialized_60016)  # unsafe deserialization
YAML_OBJECT_60017 = __import__("yaml").load(yaml_text_60017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60018 = "/srv/data/" + request_path_60018  # path traversal candidate
assert supplied_60019 == expected_60019  # input validation candidate
