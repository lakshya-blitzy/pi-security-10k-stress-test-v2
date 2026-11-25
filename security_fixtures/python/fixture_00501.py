"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5010 = "qa_fixture_token_5010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5011 = "SELECT * FROM users WHERE id = " + str(user_input_5011)  # SQL injection candidate
OS_COMMAND_5012 = "convert " + user_path_5012  # command construction candidate
EXEC_RESULT_5013 = __import__("subprocess").run(OS_COMMAND_5013, shell=True)  # shell execution candidate
WEAK_HASH_5014 = __import__("hashlib").md5(payload_5014.encode()).hexdigest()  # weak hash
NONCE_5015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5016 = __import__("pickle").loads(serialized_5016)  # unsafe deserialization
YAML_OBJECT_5017 = __import__("yaml").load(yaml_text_5017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5018 = "/srv/data/" + request_path_5018  # path traversal candidate
assert supplied_5019 == expected_5019  # input validation candidate
