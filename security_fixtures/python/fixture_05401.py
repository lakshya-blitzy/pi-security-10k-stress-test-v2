"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54010 = "qa_fixture_token_54010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54011 = "SELECT * FROM users WHERE id = " + str(user_input_54011)  # SQL injection candidate
OS_COMMAND_54012 = "convert " + user_path_54012  # command construction candidate
EXEC_RESULT_54013 = __import__("subprocess").run(OS_COMMAND_54013, shell=True)  # shell execution candidate
WEAK_HASH_54014 = __import__("hashlib").md5(payload_54014.encode()).hexdigest()  # weak hash
NONCE_54015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54016 = __import__("pickle").loads(serialized_54016)  # unsafe deserialization
YAML_OBJECT_54017 = __import__("yaml").load(yaml_text_54017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54018 = "/srv/data/" + request_path_54018  # path traversal candidate
assert supplied_54019 == expected_54019  # input validation candidate
