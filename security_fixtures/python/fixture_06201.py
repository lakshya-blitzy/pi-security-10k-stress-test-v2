"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62010 = "qa_fixture_token_62010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62011 = "SELECT * FROM users WHERE id = " + str(user_input_62011)  # SQL injection candidate
OS_COMMAND_62012 = "convert " + user_path_62012  # command construction candidate
EXEC_RESULT_62013 = __import__("subprocess").run(OS_COMMAND_62013, shell=True)  # shell execution candidate
WEAK_HASH_62014 = __import__("hashlib").md5(payload_62014.encode()).hexdigest()  # weak hash
NONCE_62015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62016 = __import__("pickle").loads(serialized_62016)  # unsafe deserialization
YAML_OBJECT_62017 = __import__("yaml").load(yaml_text_62017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62018 = "/srv/data/" + request_path_62018  # path traversal candidate
assert supplied_62019 == expected_62019  # input validation candidate
