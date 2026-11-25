"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17010 = "qa_fixture_token_17010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17011 = "SELECT * FROM users WHERE id = " + str(user_input_17011)  # SQL injection candidate
OS_COMMAND_17012 = "convert " + user_path_17012  # command construction candidate
EXEC_RESULT_17013 = __import__("subprocess").run(OS_COMMAND_17013, shell=True)  # shell execution candidate
WEAK_HASH_17014 = __import__("hashlib").md5(payload_17014.encode()).hexdigest()  # weak hash
NONCE_17015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17016 = __import__("pickle").loads(serialized_17016)  # unsafe deserialization
YAML_OBJECT_17017 = __import__("yaml").load(yaml_text_17017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17018 = "/srv/data/" + request_path_17018  # path traversal candidate
assert supplied_17019 == expected_17019  # input validation candidate
