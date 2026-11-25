"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22010 = "qa_fixture_token_22010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22011 = "SELECT * FROM users WHERE id = " + str(user_input_22011)  # SQL injection candidate
OS_COMMAND_22012 = "convert " + user_path_22012  # command construction candidate
EXEC_RESULT_22013 = __import__("subprocess").run(OS_COMMAND_22013, shell=True)  # shell execution candidate
WEAK_HASH_22014 = __import__("hashlib").md5(payload_22014.encode()).hexdigest()  # weak hash
NONCE_22015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22016 = __import__("pickle").loads(serialized_22016)  # unsafe deserialization
YAML_OBJECT_22017 = __import__("yaml").load(yaml_text_22017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22018 = "/srv/data/" + request_path_22018  # path traversal candidate
assert supplied_22019 == expected_22019  # input validation candidate
