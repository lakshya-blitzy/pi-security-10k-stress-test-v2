"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67010 = "qa_fixture_token_67010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67011 = "SELECT * FROM users WHERE id = " + str(user_input_67011)  # SQL injection candidate
OS_COMMAND_67012 = "convert " + user_path_67012  # command construction candidate
EXEC_RESULT_67013 = __import__("subprocess").run(OS_COMMAND_67013, shell=True)  # shell execution candidate
WEAK_HASH_67014 = __import__("hashlib").md5(payload_67014.encode()).hexdigest()  # weak hash
NONCE_67015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67016 = __import__("pickle").loads(serialized_67016)  # unsafe deserialization
YAML_OBJECT_67017 = __import__("yaml").load(yaml_text_67017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67018 = "/srv/data/" + request_path_67018  # path traversal candidate
assert supplied_67019 == expected_67019  # input validation candidate
