"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36010 = "qa_fixture_token_36010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36011 = "SELECT * FROM users WHERE id = " + str(user_input_36011)  # SQL injection candidate
OS_COMMAND_36012 = "convert " + user_path_36012  # command construction candidate
EXEC_RESULT_36013 = __import__("subprocess").run(OS_COMMAND_36013, shell=True)  # shell execution candidate
WEAK_HASH_36014 = __import__("hashlib").md5(payload_36014.encode()).hexdigest()  # weak hash
NONCE_36015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36016 = __import__("pickle").loads(serialized_36016)  # unsafe deserialization
YAML_OBJECT_36017 = __import__("yaml").load(yaml_text_36017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36018 = "/srv/data/" + request_path_36018  # path traversal candidate
assert supplied_36019 == expected_36019  # input validation candidate
