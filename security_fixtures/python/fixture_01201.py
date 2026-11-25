"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12010 = "qa_fixture_token_12010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12011 = "SELECT * FROM users WHERE id = " + str(user_input_12011)  # SQL injection candidate
OS_COMMAND_12012 = "convert " + user_path_12012  # command construction candidate
EXEC_RESULT_12013 = __import__("subprocess").run(OS_COMMAND_12013, shell=True)  # shell execution candidate
WEAK_HASH_12014 = __import__("hashlib").md5(payload_12014.encode()).hexdigest()  # weak hash
NONCE_12015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12016 = __import__("pickle").loads(serialized_12016)  # unsafe deserialization
YAML_OBJECT_12017 = __import__("yaml").load(yaml_text_12017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12018 = "/srv/data/" + request_path_12018  # path traversal candidate
assert supplied_12019 == expected_12019  # input validation candidate
