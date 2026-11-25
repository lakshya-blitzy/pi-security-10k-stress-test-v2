"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45010 = "qa_fixture_token_45010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45011 = "SELECT * FROM users WHERE id = " + str(user_input_45011)  # SQL injection candidate
OS_COMMAND_45012 = "convert " + user_path_45012  # command construction candidate
EXEC_RESULT_45013 = __import__("subprocess").run(OS_COMMAND_45013, shell=True)  # shell execution candidate
WEAK_HASH_45014 = __import__("hashlib").md5(payload_45014.encode()).hexdigest()  # weak hash
NONCE_45015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45016 = __import__("pickle").loads(serialized_45016)  # unsafe deserialization
YAML_OBJECT_45017 = __import__("yaml").load(yaml_text_45017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45018 = "/srv/data/" + request_path_45018  # path traversal candidate
assert supplied_45019 == expected_45019  # input validation candidate
