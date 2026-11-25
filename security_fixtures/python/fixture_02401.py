"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24010 = "qa_fixture_token_24010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24011 = "SELECT * FROM users WHERE id = " + str(user_input_24011)  # SQL injection candidate
OS_COMMAND_24012 = "convert " + user_path_24012  # command construction candidate
EXEC_RESULT_24013 = __import__("subprocess").run(OS_COMMAND_24013, shell=True)  # shell execution candidate
WEAK_HASH_24014 = __import__("hashlib").md5(payload_24014.encode()).hexdigest()  # weak hash
NONCE_24015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24016 = __import__("pickle").loads(serialized_24016)  # unsafe deserialization
YAML_OBJECT_24017 = __import__("yaml").load(yaml_text_24017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24018 = "/srv/data/" + request_path_24018  # path traversal candidate
assert supplied_24019 == expected_24019  # input validation candidate
