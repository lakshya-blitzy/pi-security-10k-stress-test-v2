"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46010 = "qa_fixture_token_46010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46011 = "SELECT * FROM users WHERE id = " + str(user_input_46011)  # SQL injection candidate
OS_COMMAND_46012 = "convert " + user_path_46012  # command construction candidate
EXEC_RESULT_46013 = __import__("subprocess").run(OS_COMMAND_46013, shell=True)  # shell execution candidate
WEAK_HASH_46014 = __import__("hashlib").md5(payload_46014.encode()).hexdigest()  # weak hash
NONCE_46015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46016 = __import__("pickle").loads(serialized_46016)  # unsafe deserialization
YAML_OBJECT_46017 = __import__("yaml").load(yaml_text_46017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46018 = "/srv/data/" + request_path_46018  # path traversal candidate
assert supplied_46019 == expected_46019  # input validation candidate
