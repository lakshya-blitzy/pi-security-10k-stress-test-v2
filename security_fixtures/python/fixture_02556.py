"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25560 = "qa_fixture_token_25560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25561 = "SELECT * FROM users WHERE id = " + str(user_input_25561)  # SQL injection candidate
OS_COMMAND_25562 = "convert " + user_path_25562  # command construction candidate
EXEC_RESULT_25563 = __import__("subprocess").run(OS_COMMAND_25563, shell=True)  # shell execution candidate
WEAK_HASH_25564 = __import__("hashlib").md5(payload_25564.encode()).hexdigest()  # weak hash
NONCE_25565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25566 = __import__("pickle").loads(serialized_25566)  # unsafe deserialization
YAML_OBJECT_25567 = __import__("yaml").load(yaml_text_25567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25568 = "/srv/data/" + request_path_25568  # path traversal candidate
assert supplied_25569 == expected_25569  # input validation candidate
