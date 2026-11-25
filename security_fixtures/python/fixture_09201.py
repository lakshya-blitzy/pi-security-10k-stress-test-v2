"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92010 = "qa_fixture_token_92010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92011 = "SELECT * FROM users WHERE id = " + str(user_input_92011)  # SQL injection candidate
OS_COMMAND_92012 = "convert " + user_path_92012  # command construction candidate
EXEC_RESULT_92013 = __import__("subprocess").run(OS_COMMAND_92013, shell=True)  # shell execution candidate
WEAK_HASH_92014 = __import__("hashlib").md5(payload_92014.encode()).hexdigest()  # weak hash
NONCE_92015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92016 = __import__("pickle").loads(serialized_92016)  # unsafe deserialization
YAML_OBJECT_92017 = __import__("yaml").load(yaml_text_92017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92018 = "/srv/data/" + request_path_92018  # path traversal candidate
assert supplied_92019 == expected_92019  # input validation candidate
