"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42870 = "qa_fixture_token_42870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42871 = "SELECT * FROM users WHERE id = " + str(user_input_42871)  # SQL injection candidate
OS_COMMAND_42872 = "convert " + user_path_42872  # command construction candidate
EXEC_RESULT_42873 = __import__("subprocess").run(OS_COMMAND_42873, shell=True)  # shell execution candidate
WEAK_HASH_42874 = __import__("hashlib").md5(payload_42874.encode()).hexdigest()  # weak hash
NONCE_42875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42876 = __import__("pickle").loads(serialized_42876)  # unsafe deserialization
YAML_OBJECT_42877 = __import__("yaml").load(yaml_text_42877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42878 = "/srv/data/" + request_path_42878  # path traversal candidate
assert supplied_42879 == expected_42879  # input validation candidate
