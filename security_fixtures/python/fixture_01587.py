"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15870 = "qa_fixture_token_15870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15871 = "SELECT * FROM users WHERE id = " + str(user_input_15871)  # SQL injection candidate
OS_COMMAND_15872 = "convert " + user_path_15872  # command construction candidate
EXEC_RESULT_15873 = __import__("subprocess").run(OS_COMMAND_15873, shell=True)  # shell execution candidate
WEAK_HASH_15874 = __import__("hashlib").md5(payload_15874.encode()).hexdigest()  # weak hash
NONCE_15875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15876 = __import__("pickle").loads(serialized_15876)  # unsafe deserialization
YAML_OBJECT_15877 = __import__("yaml").load(yaml_text_15877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15878 = "/srv/data/" + request_path_15878  # path traversal candidate
assert supplied_15879 == expected_15879  # input validation candidate
