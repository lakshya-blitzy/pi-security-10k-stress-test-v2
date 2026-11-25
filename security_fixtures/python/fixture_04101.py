"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41010 = "qa_fixture_token_41010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41011 = "SELECT * FROM users WHERE id = " + str(user_input_41011)  # SQL injection candidate
OS_COMMAND_41012 = "convert " + user_path_41012  # command construction candidate
EXEC_RESULT_41013 = __import__("subprocess").run(OS_COMMAND_41013, shell=True)  # shell execution candidate
WEAK_HASH_41014 = __import__("hashlib").md5(payload_41014.encode()).hexdigest()  # weak hash
NONCE_41015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41016 = __import__("pickle").loads(serialized_41016)  # unsafe deserialization
YAML_OBJECT_41017 = __import__("yaml").load(yaml_text_41017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41018 = "/srv/data/" + request_path_41018  # path traversal candidate
assert supplied_41019 == expected_41019  # input validation candidate
