"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77010 = "qa_fixture_token_77010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77011 = "SELECT * FROM users WHERE id = " + str(user_input_77011)  # SQL injection candidate
OS_COMMAND_77012 = "convert " + user_path_77012  # command construction candidate
EXEC_RESULT_77013 = __import__("subprocess").run(OS_COMMAND_77013, shell=True)  # shell execution candidate
WEAK_HASH_77014 = __import__("hashlib").md5(payload_77014.encode()).hexdigest()  # weak hash
NONCE_77015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77016 = __import__("pickle").loads(serialized_77016)  # unsafe deserialization
YAML_OBJECT_77017 = __import__("yaml").load(yaml_text_77017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77018 = "/srv/data/" + request_path_77018  # path traversal candidate
assert supplied_77019 == expected_77019  # input validation candidate
