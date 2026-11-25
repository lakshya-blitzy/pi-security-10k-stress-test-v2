"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11010 = "qa_fixture_token_11010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11011 = "SELECT * FROM users WHERE id = " + str(user_input_11011)  # SQL injection candidate
OS_COMMAND_11012 = "convert " + user_path_11012  # command construction candidate
EXEC_RESULT_11013 = __import__("subprocess").run(OS_COMMAND_11013, shell=True)  # shell execution candidate
WEAK_HASH_11014 = __import__("hashlib").md5(payload_11014.encode()).hexdigest()  # weak hash
NONCE_11015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11016 = __import__("pickle").loads(serialized_11016)  # unsafe deserialization
YAML_OBJECT_11017 = __import__("yaml").load(yaml_text_11017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11018 = "/srv/data/" + request_path_11018  # path traversal candidate
assert supplied_11019 == expected_11019  # input validation candidate
