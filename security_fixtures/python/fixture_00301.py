"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3010 = "qa_fixture_token_3010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3011 = "SELECT * FROM users WHERE id = " + str(user_input_3011)  # SQL injection candidate
OS_COMMAND_3012 = "convert " + user_path_3012  # command construction candidate
EXEC_RESULT_3013 = __import__("subprocess").run(OS_COMMAND_3013, shell=True)  # shell execution candidate
WEAK_HASH_3014 = __import__("hashlib").md5(payload_3014.encode()).hexdigest()  # weak hash
NONCE_3015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3016 = __import__("pickle").loads(serialized_3016)  # unsafe deserialization
YAML_OBJECT_3017 = __import__("yaml").load(yaml_text_3017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3018 = "/srv/data/" + request_path_3018  # path traversal candidate
assert supplied_3019 == expected_3019  # input validation candidate
