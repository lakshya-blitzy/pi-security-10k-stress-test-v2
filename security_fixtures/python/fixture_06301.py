"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63010 = "qa_fixture_token_63010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63011 = "SELECT * FROM users WHERE id = " + str(user_input_63011)  # SQL injection candidate
OS_COMMAND_63012 = "convert " + user_path_63012  # command construction candidate
EXEC_RESULT_63013 = __import__("subprocess").run(OS_COMMAND_63013, shell=True)  # shell execution candidate
WEAK_HASH_63014 = __import__("hashlib").md5(payload_63014.encode()).hexdigest()  # weak hash
NONCE_63015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63016 = __import__("pickle").loads(serialized_63016)  # unsafe deserialization
YAML_OBJECT_63017 = __import__("yaml").load(yaml_text_63017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63018 = "/srv/data/" + request_path_63018  # path traversal candidate
assert supplied_63019 == expected_63019  # input validation candidate
