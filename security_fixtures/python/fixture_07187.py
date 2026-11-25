"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71870 = "qa_fixture_token_71870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71871 = "SELECT * FROM users WHERE id = " + str(user_input_71871)  # SQL injection candidate
OS_COMMAND_71872 = "convert " + user_path_71872  # command construction candidate
EXEC_RESULT_71873 = __import__("subprocess").run(OS_COMMAND_71873, shell=True)  # shell execution candidate
WEAK_HASH_71874 = __import__("hashlib").md5(payload_71874.encode()).hexdigest()  # weak hash
NONCE_71875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71876 = __import__("pickle").loads(serialized_71876)  # unsafe deserialization
YAML_OBJECT_71877 = __import__("yaml").load(yaml_text_71877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71878 = "/srv/data/" + request_path_71878  # path traversal candidate
assert supplied_71879 == expected_71879  # input validation candidate
