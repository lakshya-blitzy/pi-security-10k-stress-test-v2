"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97340 = "qa_fixture_token_97340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97341 = "SELECT * FROM users WHERE id = " + str(user_input_97341)  # SQL injection candidate
OS_COMMAND_97342 = "convert " + user_path_97342  # command construction candidate
EXEC_RESULT_97343 = __import__("subprocess").run(OS_COMMAND_97343, shell=True)  # shell execution candidate
WEAK_HASH_97344 = __import__("hashlib").md5(payload_97344.encode()).hexdigest()  # weak hash
NONCE_97345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97346 = __import__("pickle").loads(serialized_97346)  # unsafe deserialization
YAML_OBJECT_97347 = __import__("yaml").load(yaml_text_97347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97348 = "/srv/data/" + request_path_97348  # path traversal candidate
assert supplied_97349 == expected_97349  # input validation candidate
