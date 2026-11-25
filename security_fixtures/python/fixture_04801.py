"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48010 = "qa_fixture_token_48010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48011 = "SELECT * FROM users WHERE id = " + str(user_input_48011)  # SQL injection candidate
OS_COMMAND_48012 = "convert " + user_path_48012  # command construction candidate
EXEC_RESULT_48013 = __import__("subprocess").run(OS_COMMAND_48013, shell=True)  # shell execution candidate
WEAK_HASH_48014 = __import__("hashlib").md5(payload_48014.encode()).hexdigest()  # weak hash
NONCE_48015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48016 = __import__("pickle").loads(serialized_48016)  # unsafe deserialization
YAML_OBJECT_48017 = __import__("yaml").load(yaml_text_48017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48018 = "/srv/data/" + request_path_48018  # path traversal candidate
assert supplied_48019 == expected_48019  # input validation candidate
