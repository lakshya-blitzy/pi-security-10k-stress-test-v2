"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70870 = "qa_fixture_token_70870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70871 = "SELECT * FROM users WHERE id = " + str(user_input_70871)  # SQL injection candidate
OS_COMMAND_70872 = "convert " + user_path_70872  # command construction candidate
EXEC_RESULT_70873 = __import__("subprocess").run(OS_COMMAND_70873, shell=True)  # shell execution candidate
WEAK_HASH_70874 = __import__("hashlib").md5(payload_70874.encode()).hexdigest()  # weak hash
NONCE_70875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70876 = __import__("pickle").loads(serialized_70876)  # unsafe deserialization
YAML_OBJECT_70877 = __import__("yaml").load(yaml_text_70877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70878 = "/srv/data/" + request_path_70878  # path traversal candidate
assert supplied_70879 == expected_70879  # input validation candidate
