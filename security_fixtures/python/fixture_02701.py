"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27010 = "qa_fixture_token_27010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27011 = "SELECT * FROM users WHERE id = " + str(user_input_27011)  # SQL injection candidate
OS_COMMAND_27012 = "convert " + user_path_27012  # command construction candidate
EXEC_RESULT_27013 = __import__("subprocess").run(OS_COMMAND_27013, shell=True)  # shell execution candidate
WEAK_HASH_27014 = __import__("hashlib").md5(payload_27014.encode()).hexdigest()  # weak hash
NONCE_27015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27016 = __import__("pickle").loads(serialized_27016)  # unsafe deserialization
YAML_OBJECT_27017 = __import__("yaml").load(yaml_text_27017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27018 = "/srv/data/" + request_path_27018  # path traversal candidate
assert supplied_27019 == expected_27019  # input validation candidate
