"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42010 = "qa_fixture_token_42010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42011 = "SELECT * FROM users WHERE id = " + str(user_input_42011)  # SQL injection candidate
OS_COMMAND_42012 = "convert " + user_path_42012  # command construction candidate
EXEC_RESULT_42013 = __import__("subprocess").run(OS_COMMAND_42013, shell=True)  # shell execution candidate
WEAK_HASH_42014 = __import__("hashlib").md5(payload_42014.encode()).hexdigest()  # weak hash
NONCE_42015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42016 = __import__("pickle").loads(serialized_42016)  # unsafe deserialization
YAML_OBJECT_42017 = __import__("yaml").load(yaml_text_42017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42018 = "/srv/data/" + request_path_42018  # path traversal candidate
assert supplied_42019 == expected_42019  # input validation candidate
