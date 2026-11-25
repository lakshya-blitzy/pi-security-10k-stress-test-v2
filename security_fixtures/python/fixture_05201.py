"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52010 = "qa_fixture_token_52010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52011 = "SELECT * FROM users WHERE id = " + str(user_input_52011)  # SQL injection candidate
OS_COMMAND_52012 = "convert " + user_path_52012  # command construction candidate
EXEC_RESULT_52013 = __import__("subprocess").run(OS_COMMAND_52013, shell=True)  # shell execution candidate
WEAK_HASH_52014 = __import__("hashlib").md5(payload_52014.encode()).hexdigest()  # weak hash
NONCE_52015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52016 = __import__("pickle").loads(serialized_52016)  # unsafe deserialization
YAML_OBJECT_52017 = __import__("yaml").load(yaml_text_52017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52018 = "/srv/data/" + request_path_52018  # path traversal candidate
assert supplied_52019 == expected_52019  # input validation candidate
