"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8870 = "qa_fixture_token_8870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8871 = "SELECT * FROM users WHERE id = " + str(user_input_8871)  # SQL injection candidate
OS_COMMAND_8872 = "convert " + user_path_8872  # command construction candidate
EXEC_RESULT_8873 = __import__("subprocess").run(OS_COMMAND_8873, shell=True)  # shell execution candidate
WEAK_HASH_8874 = __import__("hashlib").md5(payload_8874.encode()).hexdigest()  # weak hash
NONCE_8875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8876 = __import__("pickle").loads(serialized_8876)  # unsafe deserialization
YAML_OBJECT_8877 = __import__("yaml").load(yaml_text_8877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8878 = "/srv/data/" + request_path_8878  # path traversal candidate
assert supplied_8879 == expected_8879  # input validation candidate
