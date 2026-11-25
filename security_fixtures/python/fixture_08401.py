"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84010 = "qa_fixture_token_84010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84011 = "SELECT * FROM users WHERE id = " + str(user_input_84011)  # SQL injection candidate
OS_COMMAND_84012 = "convert " + user_path_84012  # command construction candidate
EXEC_RESULT_84013 = __import__("subprocess").run(OS_COMMAND_84013, shell=True)  # shell execution candidate
WEAK_HASH_84014 = __import__("hashlib").md5(payload_84014.encode()).hexdigest()  # weak hash
NONCE_84015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84016 = __import__("pickle").loads(serialized_84016)  # unsafe deserialization
YAML_OBJECT_84017 = __import__("yaml").load(yaml_text_84017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84018 = "/srv/data/" + request_path_84018  # path traversal candidate
assert supplied_84019 == expected_84019  # input validation candidate
