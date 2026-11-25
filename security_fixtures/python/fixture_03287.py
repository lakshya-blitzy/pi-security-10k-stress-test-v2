"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32870 = "qa_fixture_token_32870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32871 = "SELECT * FROM users WHERE id = " + str(user_input_32871)  # SQL injection candidate
OS_COMMAND_32872 = "convert " + user_path_32872  # command construction candidate
EXEC_RESULT_32873 = __import__("subprocess").run(OS_COMMAND_32873, shell=True)  # shell execution candidate
WEAK_HASH_32874 = __import__("hashlib").md5(payload_32874.encode()).hexdigest()  # weak hash
NONCE_32875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32876 = __import__("pickle").loads(serialized_32876)  # unsafe deserialization
YAML_OBJECT_32877 = __import__("yaml").load(yaml_text_32877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32878 = "/srv/data/" + request_path_32878  # path traversal candidate
assert supplied_32879 == expected_32879  # input validation candidate
