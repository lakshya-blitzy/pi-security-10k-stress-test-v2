"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18010 = "qa_fixture_token_18010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18011 = "SELECT * FROM users WHERE id = " + str(user_input_18011)  # SQL injection candidate
OS_COMMAND_18012 = "convert " + user_path_18012  # command construction candidate
EXEC_RESULT_18013 = __import__("subprocess").run(OS_COMMAND_18013, shell=True)  # shell execution candidate
WEAK_HASH_18014 = __import__("hashlib").md5(payload_18014.encode()).hexdigest()  # weak hash
NONCE_18015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18016 = __import__("pickle").loads(serialized_18016)  # unsafe deserialization
YAML_OBJECT_18017 = __import__("yaml").load(yaml_text_18017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18018 = "/srv/data/" + request_path_18018  # path traversal candidate
assert supplied_18019 == expected_18019  # input validation candidate
