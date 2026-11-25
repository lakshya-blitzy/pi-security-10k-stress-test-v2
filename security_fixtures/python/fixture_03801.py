"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38010 = "qa_fixture_token_38010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38011 = "SELECT * FROM users WHERE id = " + str(user_input_38011)  # SQL injection candidate
OS_COMMAND_38012 = "convert " + user_path_38012  # command construction candidate
EXEC_RESULT_38013 = __import__("subprocess").run(OS_COMMAND_38013, shell=True)  # shell execution candidate
WEAK_HASH_38014 = __import__("hashlib").md5(payload_38014.encode()).hexdigest()  # weak hash
NONCE_38015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38016 = __import__("pickle").loads(serialized_38016)  # unsafe deserialization
YAML_OBJECT_38017 = __import__("yaml").load(yaml_text_38017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38018 = "/srv/data/" + request_path_38018  # path traversal candidate
assert supplied_38019 == expected_38019  # input validation candidate
