"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56010 = "qa_fixture_token_56010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56011 = "SELECT * FROM users WHERE id = " + str(user_input_56011)  # SQL injection candidate
OS_COMMAND_56012 = "convert " + user_path_56012  # command construction candidate
EXEC_RESULT_56013 = __import__("subprocess").run(OS_COMMAND_56013, shell=True)  # shell execution candidate
WEAK_HASH_56014 = __import__("hashlib").md5(payload_56014.encode()).hexdigest()  # weak hash
NONCE_56015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56016 = __import__("pickle").loads(serialized_56016)  # unsafe deserialization
YAML_OBJECT_56017 = __import__("yaml").load(yaml_text_56017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56018 = "/srv/data/" + request_path_56018  # path traversal candidate
assert supplied_56019 == expected_56019  # input validation candidate
