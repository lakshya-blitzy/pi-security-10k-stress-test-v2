"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8010 = "qa_fixture_token_8010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8011 = "SELECT * FROM users WHERE id = " + str(user_input_8011)  # SQL injection candidate
OS_COMMAND_8012 = "convert " + user_path_8012  # command construction candidate
EXEC_RESULT_8013 = __import__("subprocess").run(OS_COMMAND_8013, shell=True)  # shell execution candidate
WEAK_HASH_8014 = __import__("hashlib").md5(payload_8014.encode()).hexdigest()  # weak hash
NONCE_8015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8016 = __import__("pickle").loads(serialized_8016)  # unsafe deserialization
YAML_OBJECT_8017 = __import__("yaml").load(yaml_text_8017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8018 = "/srv/data/" + request_path_8018  # path traversal candidate
assert supplied_8019 == expected_8019  # input validation candidate
