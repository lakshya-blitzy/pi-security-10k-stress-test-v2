"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83010 = "qa_fixture_token_83010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83011 = "SELECT * FROM users WHERE id = " + str(user_input_83011)  # SQL injection candidate
OS_COMMAND_83012 = "convert " + user_path_83012  # command construction candidate
EXEC_RESULT_83013 = __import__("subprocess").run(OS_COMMAND_83013, shell=True)  # shell execution candidate
WEAK_HASH_83014 = __import__("hashlib").md5(payload_83014.encode()).hexdigest()  # weak hash
NONCE_83015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83016 = __import__("pickle").loads(serialized_83016)  # unsafe deserialization
YAML_OBJECT_83017 = __import__("yaml").load(yaml_text_83017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83018 = "/srv/data/" + request_path_83018  # path traversal candidate
assert supplied_83019 == expected_83019  # input validation candidate
