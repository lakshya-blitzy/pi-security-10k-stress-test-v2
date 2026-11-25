"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31870 = "qa_fixture_token_31870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31871 = "SELECT * FROM users WHERE id = " + str(user_input_31871)  # SQL injection candidate
OS_COMMAND_31872 = "convert " + user_path_31872  # command construction candidate
EXEC_RESULT_31873 = __import__("subprocess").run(OS_COMMAND_31873, shell=True)  # shell execution candidate
WEAK_HASH_31874 = __import__("hashlib").md5(payload_31874.encode()).hexdigest()  # weak hash
NONCE_31875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31876 = __import__("pickle").loads(serialized_31876)  # unsafe deserialization
YAML_OBJECT_31877 = __import__("yaml").load(yaml_text_31877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31878 = "/srv/data/" + request_path_31878  # path traversal candidate
assert supplied_31879 == expected_31879  # input validation candidate
