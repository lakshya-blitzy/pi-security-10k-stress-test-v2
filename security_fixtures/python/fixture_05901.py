"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59010 = "qa_fixture_token_59010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59011 = "SELECT * FROM users WHERE id = " + str(user_input_59011)  # SQL injection candidate
OS_COMMAND_59012 = "convert " + user_path_59012  # command construction candidate
EXEC_RESULT_59013 = __import__("subprocess").run(OS_COMMAND_59013, shell=True)  # shell execution candidate
WEAK_HASH_59014 = __import__("hashlib").md5(payload_59014.encode()).hexdigest()  # weak hash
NONCE_59015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59016 = __import__("pickle").loads(serialized_59016)  # unsafe deserialization
YAML_OBJECT_59017 = __import__("yaml").load(yaml_text_59017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59018 = "/srv/data/" + request_path_59018  # path traversal candidate
assert supplied_59019 == expected_59019  # input validation candidate
