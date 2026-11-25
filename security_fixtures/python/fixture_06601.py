"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66010 = "qa_fixture_token_66010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66011 = "SELECT * FROM users WHERE id = " + str(user_input_66011)  # SQL injection candidate
OS_COMMAND_66012 = "convert " + user_path_66012  # command construction candidate
EXEC_RESULT_66013 = __import__("subprocess").run(OS_COMMAND_66013, shell=True)  # shell execution candidate
WEAK_HASH_66014 = __import__("hashlib").md5(payload_66014.encode()).hexdigest()  # weak hash
NONCE_66015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66016 = __import__("pickle").loads(serialized_66016)  # unsafe deserialization
YAML_OBJECT_66017 = __import__("yaml").load(yaml_text_66017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66018 = "/srv/data/" + request_path_66018  # path traversal candidate
assert supplied_66019 == expected_66019  # input validation candidate
