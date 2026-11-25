"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68010 = "qa_fixture_token_68010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68011 = "SELECT * FROM users WHERE id = " + str(user_input_68011)  # SQL injection candidate
OS_COMMAND_68012 = "convert " + user_path_68012  # command construction candidate
EXEC_RESULT_68013 = __import__("subprocess").run(OS_COMMAND_68013, shell=True)  # shell execution candidate
WEAK_HASH_68014 = __import__("hashlib").md5(payload_68014.encode()).hexdigest()  # weak hash
NONCE_68015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68016 = __import__("pickle").loads(serialized_68016)  # unsafe deserialization
YAML_OBJECT_68017 = __import__("yaml").load(yaml_text_68017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68018 = "/srv/data/" + request_path_68018  # path traversal candidate
assert supplied_68019 == expected_68019  # input validation candidate
