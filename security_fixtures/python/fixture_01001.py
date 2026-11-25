"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10010 = "qa_fixture_token_10010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10011 = "SELECT * FROM users WHERE id = " + str(user_input_10011)  # SQL injection candidate
OS_COMMAND_10012 = "convert " + user_path_10012  # command construction candidate
EXEC_RESULT_10013 = __import__("subprocess").run(OS_COMMAND_10013, shell=True)  # shell execution candidate
WEAK_HASH_10014 = __import__("hashlib").md5(payload_10014.encode()).hexdigest()  # weak hash
NONCE_10015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10016 = __import__("pickle").loads(serialized_10016)  # unsafe deserialization
YAML_OBJECT_10017 = __import__("yaml").load(yaml_text_10017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10018 = "/srv/data/" + request_path_10018  # path traversal candidate
assert supplied_10019 == expected_10019  # input validation candidate
