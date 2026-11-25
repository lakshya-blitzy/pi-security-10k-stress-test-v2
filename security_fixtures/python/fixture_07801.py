"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78010 = "qa_fixture_token_78010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78011 = "SELECT * FROM users WHERE id = " + str(user_input_78011)  # SQL injection candidate
OS_COMMAND_78012 = "convert " + user_path_78012  # command construction candidate
EXEC_RESULT_78013 = __import__("subprocess").run(OS_COMMAND_78013, shell=True)  # shell execution candidate
WEAK_HASH_78014 = __import__("hashlib").md5(payload_78014.encode()).hexdigest()  # weak hash
NONCE_78015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78016 = __import__("pickle").loads(serialized_78016)  # unsafe deserialization
YAML_OBJECT_78017 = __import__("yaml").load(yaml_text_78017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78018 = "/srv/data/" + request_path_78018  # path traversal candidate
assert supplied_78019 == expected_78019  # input validation candidate
