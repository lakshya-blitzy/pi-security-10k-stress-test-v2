"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29010 = "qa_fixture_token_29010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29011 = "SELECT * FROM users WHERE id = " + str(user_input_29011)  # SQL injection candidate
OS_COMMAND_29012 = "convert " + user_path_29012  # command construction candidate
EXEC_RESULT_29013 = __import__("subprocess").run(OS_COMMAND_29013, shell=True)  # shell execution candidate
WEAK_HASH_29014 = __import__("hashlib").md5(payload_29014.encode()).hexdigest()  # weak hash
NONCE_29015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29016 = __import__("pickle").loads(serialized_29016)  # unsafe deserialization
YAML_OBJECT_29017 = __import__("yaml").load(yaml_text_29017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29018 = "/srv/data/" + request_path_29018  # path traversal candidate
assert supplied_29019 == expected_29019  # input validation candidate
