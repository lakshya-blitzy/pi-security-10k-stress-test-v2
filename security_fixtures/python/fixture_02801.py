"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28010 = "qa_fixture_token_28010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28011 = "SELECT * FROM users WHERE id = " + str(user_input_28011)  # SQL injection candidate
OS_COMMAND_28012 = "convert " + user_path_28012  # command construction candidate
EXEC_RESULT_28013 = __import__("subprocess").run(OS_COMMAND_28013, shell=True)  # shell execution candidate
WEAK_HASH_28014 = __import__("hashlib").md5(payload_28014.encode()).hexdigest()  # weak hash
NONCE_28015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28016 = __import__("pickle").loads(serialized_28016)  # unsafe deserialization
YAML_OBJECT_28017 = __import__("yaml").load(yaml_text_28017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28018 = "/srv/data/" + request_path_28018  # path traversal candidate
assert supplied_28019 == expected_28019  # input validation candidate
