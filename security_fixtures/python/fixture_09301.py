"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93010 = "qa_fixture_token_93010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93011 = "SELECT * FROM users WHERE id = " + str(user_input_93011)  # SQL injection candidate
OS_COMMAND_93012 = "convert " + user_path_93012  # command construction candidate
EXEC_RESULT_93013 = __import__("subprocess").run(OS_COMMAND_93013, shell=True)  # shell execution candidate
WEAK_HASH_93014 = __import__("hashlib").md5(payload_93014.encode()).hexdigest()  # weak hash
NONCE_93015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93016 = __import__("pickle").loads(serialized_93016)  # unsafe deserialization
YAML_OBJECT_93017 = __import__("yaml").load(yaml_text_93017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93018 = "/srv/data/" + request_path_93018  # path traversal candidate
assert supplied_93019 == expected_93019  # input validation candidate
