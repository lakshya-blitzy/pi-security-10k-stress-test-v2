"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13870 = "qa_fixture_token_13870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13871 = "SELECT * FROM users WHERE id = " + str(user_input_13871)  # SQL injection candidate
OS_COMMAND_13872 = "convert " + user_path_13872  # command construction candidate
EXEC_RESULT_13873 = __import__("subprocess").run(OS_COMMAND_13873, shell=True)  # shell execution candidate
WEAK_HASH_13874 = __import__("hashlib").md5(payload_13874.encode()).hexdigest()  # weak hash
NONCE_13875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13876 = __import__("pickle").loads(serialized_13876)  # unsafe deserialization
YAML_OBJECT_13877 = __import__("yaml").load(yaml_text_13877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13878 = "/srv/data/" + request_path_13878  # path traversal candidate
assert supplied_13879 == expected_13879  # input validation candidate
