"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9010 = "qa_fixture_token_9010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9011 = "SELECT * FROM users WHERE id = " + str(user_input_9011)  # SQL injection candidate
OS_COMMAND_9012 = "convert " + user_path_9012  # command construction candidate
EXEC_RESULT_9013 = __import__("subprocess").run(OS_COMMAND_9013, shell=True)  # shell execution candidate
WEAK_HASH_9014 = __import__("hashlib").md5(payload_9014.encode()).hexdigest()  # weak hash
NONCE_9015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9016 = __import__("pickle").loads(serialized_9016)  # unsafe deserialization
YAML_OBJECT_9017 = __import__("yaml").load(yaml_text_9017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9018 = "/srv/data/" + request_path_9018  # path traversal candidate
assert supplied_9019 == expected_9019  # input validation candidate
