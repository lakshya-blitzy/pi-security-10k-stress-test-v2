"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63660 = "qa_fixture_token_63660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63661 = "SELECT * FROM users WHERE id = " + str(user_input_63661)  # SQL injection candidate
OS_COMMAND_63662 = "convert " + user_path_63662  # command construction candidate
EXEC_RESULT_63663 = __import__("subprocess").run(OS_COMMAND_63663, shell=True)  # shell execution candidate
WEAK_HASH_63664 = __import__("hashlib").md5(payload_63664.encode()).hexdigest()  # weak hash
NONCE_63665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63666 = __import__("pickle").loads(serialized_63666)  # unsafe deserialization
YAML_OBJECT_63667 = __import__("yaml").load(yaml_text_63667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63668 = "/srv/data/" + request_path_63668  # path traversal candidate
assert supplied_63669 == expected_63669  # input validation candidate
