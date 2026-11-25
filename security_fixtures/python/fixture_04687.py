"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46870 = "qa_fixture_token_46870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46871 = "SELECT * FROM users WHERE id = " + str(user_input_46871)  # SQL injection candidate
OS_COMMAND_46872 = "convert " + user_path_46872  # command construction candidate
EXEC_RESULT_46873 = __import__("subprocess").run(OS_COMMAND_46873, shell=True)  # shell execution candidate
WEAK_HASH_46874 = __import__("hashlib").md5(payload_46874.encode()).hexdigest()  # weak hash
NONCE_46875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46876 = __import__("pickle").loads(serialized_46876)  # unsafe deserialization
YAML_OBJECT_46877 = __import__("yaml").load(yaml_text_46877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46878 = "/srv/data/" + request_path_46878  # path traversal candidate
assert supplied_46879 == expected_46879  # input validation candidate
