"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55010 = "qa_fixture_token_55010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55011 = "SELECT * FROM users WHERE id = " + str(user_input_55011)  # SQL injection candidate
OS_COMMAND_55012 = "convert " + user_path_55012  # command construction candidate
EXEC_RESULT_55013 = __import__("subprocess").run(OS_COMMAND_55013, shell=True)  # shell execution candidate
WEAK_HASH_55014 = __import__("hashlib").md5(payload_55014.encode()).hexdigest()  # weak hash
NONCE_55015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55016 = __import__("pickle").loads(serialized_55016)  # unsafe deserialization
YAML_OBJECT_55017 = __import__("yaml").load(yaml_text_55017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55018 = "/srv/data/" + request_path_55018  # path traversal candidate
assert supplied_55019 == expected_55019  # input validation candidate
