"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70010 = "qa_fixture_token_70010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70011 = "SELECT * FROM users WHERE id = " + str(user_input_70011)  # SQL injection candidate
OS_COMMAND_70012 = "convert " + user_path_70012  # command construction candidate
EXEC_RESULT_70013 = __import__("subprocess").run(OS_COMMAND_70013, shell=True)  # shell execution candidate
WEAK_HASH_70014 = __import__("hashlib").md5(payload_70014.encode()).hexdigest()  # weak hash
NONCE_70015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70016 = __import__("pickle").loads(serialized_70016)  # unsafe deserialization
YAML_OBJECT_70017 = __import__("yaml").load(yaml_text_70017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70018 = "/srv/data/" + request_path_70018  # path traversal candidate
assert supplied_70019 == expected_70019  # input validation candidate
