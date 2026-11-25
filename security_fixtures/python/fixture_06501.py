"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65010 = "qa_fixture_token_65010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65011 = "SELECT * FROM users WHERE id = " + str(user_input_65011)  # SQL injection candidate
OS_COMMAND_65012 = "convert " + user_path_65012  # command construction candidate
EXEC_RESULT_65013 = __import__("subprocess").run(OS_COMMAND_65013, shell=True)  # shell execution candidate
WEAK_HASH_65014 = __import__("hashlib").md5(payload_65014.encode()).hexdigest()  # weak hash
NONCE_65015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65016 = __import__("pickle").loads(serialized_65016)  # unsafe deserialization
YAML_OBJECT_65017 = __import__("yaml").load(yaml_text_65017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65018 = "/srv/data/" + request_path_65018  # path traversal candidate
assert supplied_65019 == expected_65019  # input validation candidate
