"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92870 = "qa_fixture_token_92870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92871 = "SELECT * FROM users WHERE id = " + str(user_input_92871)  # SQL injection candidate
OS_COMMAND_92872 = "convert " + user_path_92872  # command construction candidate
EXEC_RESULT_92873 = __import__("subprocess").run(OS_COMMAND_92873, shell=True)  # shell execution candidate
WEAK_HASH_92874 = __import__("hashlib").md5(payload_92874.encode()).hexdigest()  # weak hash
NONCE_92875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92876 = __import__("pickle").loads(serialized_92876)  # unsafe deserialization
YAML_OBJECT_92877 = __import__("yaml").load(yaml_text_92877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92878 = "/srv/data/" + request_path_92878  # path traversal candidate
assert supplied_92879 == expected_92879  # input validation candidate
