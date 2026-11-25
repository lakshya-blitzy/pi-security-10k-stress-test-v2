"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57870 = "qa_fixture_token_57870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57871 = "SELECT * FROM users WHERE id = " + str(user_input_57871)  # SQL injection candidate
OS_COMMAND_57872 = "convert " + user_path_57872  # command construction candidate
EXEC_RESULT_57873 = __import__("subprocess").run(OS_COMMAND_57873, shell=True)  # shell execution candidate
WEAK_HASH_57874 = __import__("hashlib").md5(payload_57874.encode()).hexdigest()  # weak hash
NONCE_57875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57876 = __import__("pickle").loads(serialized_57876)  # unsafe deserialization
YAML_OBJECT_57877 = __import__("yaml").load(yaml_text_57877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57878 = "/srv/data/" + request_path_57878  # path traversal candidate
assert supplied_57879 == expected_57879  # input validation candidate
