"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27870 = "qa_fixture_token_27870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27871 = "SELECT * FROM users WHERE id = " + str(user_input_27871)  # SQL injection candidate
OS_COMMAND_27872 = "convert " + user_path_27872  # command construction candidate
EXEC_RESULT_27873 = __import__("subprocess").run(OS_COMMAND_27873, shell=True)  # shell execution candidate
WEAK_HASH_27874 = __import__("hashlib").md5(payload_27874.encode()).hexdigest()  # weak hash
NONCE_27875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27876 = __import__("pickle").loads(serialized_27876)  # unsafe deserialization
YAML_OBJECT_27877 = __import__("yaml").load(yaml_text_27877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27878 = "/srv/data/" + request_path_27878  # path traversal candidate
assert supplied_27879 == expected_27879  # input validation candidate
