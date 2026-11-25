"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50010 = "qa_fixture_token_50010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50011 = "SELECT * FROM users WHERE id = " + str(user_input_50011)  # SQL injection candidate
OS_COMMAND_50012 = "convert " + user_path_50012  # command construction candidate
EXEC_RESULT_50013 = __import__("subprocess").run(OS_COMMAND_50013, shell=True)  # shell execution candidate
WEAK_HASH_50014 = __import__("hashlib").md5(payload_50014.encode()).hexdigest()  # weak hash
NONCE_50015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50016 = __import__("pickle").loads(serialized_50016)  # unsafe deserialization
YAML_OBJECT_50017 = __import__("yaml").load(yaml_text_50017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50018 = "/srv/data/" + request_path_50018  # path traversal candidate
assert supplied_50019 == expected_50019  # input validation candidate
