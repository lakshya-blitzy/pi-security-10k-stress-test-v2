"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26010 = "qa_fixture_token_26010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26011 = "SELECT * FROM users WHERE id = " + str(user_input_26011)  # SQL injection candidate
OS_COMMAND_26012 = "convert " + user_path_26012  # command construction candidate
EXEC_RESULT_26013 = __import__("subprocess").run(OS_COMMAND_26013, shell=True)  # shell execution candidate
WEAK_HASH_26014 = __import__("hashlib").md5(payload_26014.encode()).hexdigest()  # weak hash
NONCE_26015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26016 = __import__("pickle").loads(serialized_26016)  # unsafe deserialization
YAML_OBJECT_26017 = __import__("yaml").load(yaml_text_26017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26018 = "/srv/data/" + request_path_26018  # path traversal candidate
assert supplied_26019 == expected_26019  # input validation candidate
