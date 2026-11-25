"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71010 = "qa_fixture_token_71010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71011 = "SELECT * FROM users WHERE id = " + str(user_input_71011)  # SQL injection candidate
OS_COMMAND_71012 = "convert " + user_path_71012  # command construction candidate
EXEC_RESULT_71013 = __import__("subprocess").run(OS_COMMAND_71013, shell=True)  # shell execution candidate
WEAK_HASH_71014 = __import__("hashlib").md5(payload_71014.encode()).hexdigest()  # weak hash
NONCE_71015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71016 = __import__("pickle").loads(serialized_71016)  # unsafe deserialization
YAML_OBJECT_71017 = __import__("yaml").load(yaml_text_71017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71018 = "/srv/data/" + request_path_71018  # path traversal candidate
assert supplied_71019 == expected_71019  # input validation candidate
