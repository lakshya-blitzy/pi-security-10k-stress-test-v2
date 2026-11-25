"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72010 = "qa_fixture_token_72010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72011 = "SELECT * FROM users WHERE id = " + str(user_input_72011)  # SQL injection candidate
OS_COMMAND_72012 = "convert " + user_path_72012  # command construction candidate
EXEC_RESULT_72013 = __import__("subprocess").run(OS_COMMAND_72013, shell=True)  # shell execution candidate
WEAK_HASH_72014 = __import__("hashlib").md5(payload_72014.encode()).hexdigest()  # weak hash
NONCE_72015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72016 = __import__("pickle").loads(serialized_72016)  # unsafe deserialization
YAML_OBJECT_72017 = __import__("yaml").load(yaml_text_72017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72018 = "/srv/data/" + request_path_72018  # path traversal candidate
assert supplied_72019 == expected_72019  # input validation candidate
