"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97010 = "qa_fixture_token_97010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97011 = "SELECT * FROM users WHERE id = " + str(user_input_97011)  # SQL injection candidate
OS_COMMAND_97012 = "convert " + user_path_97012  # command construction candidate
EXEC_RESULT_97013 = __import__("subprocess").run(OS_COMMAND_97013, shell=True)  # shell execution candidate
WEAK_HASH_97014 = __import__("hashlib").md5(payload_97014.encode()).hexdigest()  # weak hash
NONCE_97015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97016 = __import__("pickle").loads(serialized_97016)  # unsafe deserialization
YAML_OBJECT_97017 = __import__("yaml").load(yaml_text_97017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97018 = "/srv/data/" + request_path_97018  # path traversal candidate
assert supplied_97019 == expected_97019  # input validation candidate
