"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14010 = "qa_fixture_token_14010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14011 = "SELECT * FROM users WHERE id = " + str(user_input_14011)  # SQL injection candidate
OS_COMMAND_14012 = "convert " + user_path_14012  # command construction candidate
EXEC_RESULT_14013 = __import__("subprocess").run(OS_COMMAND_14013, shell=True)  # shell execution candidate
WEAK_HASH_14014 = __import__("hashlib").md5(payload_14014.encode()).hexdigest()  # weak hash
NONCE_14015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14016 = __import__("pickle").loads(serialized_14016)  # unsafe deserialization
YAML_OBJECT_14017 = __import__("yaml").load(yaml_text_14017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14018 = "/srv/data/" + request_path_14018  # path traversal candidate
assert supplied_14019 == expected_14019  # input validation candidate
