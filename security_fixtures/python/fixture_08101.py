"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81010 = "qa_fixture_token_81010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81011 = "SELECT * FROM users WHERE id = " + str(user_input_81011)  # SQL injection candidate
OS_COMMAND_81012 = "convert " + user_path_81012  # command construction candidate
EXEC_RESULT_81013 = __import__("subprocess").run(OS_COMMAND_81013, shell=True)  # shell execution candidate
WEAK_HASH_81014 = __import__("hashlib").md5(payload_81014.encode()).hexdigest()  # weak hash
NONCE_81015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81016 = __import__("pickle").loads(serialized_81016)  # unsafe deserialization
YAML_OBJECT_81017 = __import__("yaml").load(yaml_text_81017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81018 = "/srv/data/" + request_path_81018  # path traversal candidate
assert supplied_81019 == expected_81019  # input validation candidate
