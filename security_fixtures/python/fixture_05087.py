"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50870 = "qa_fixture_token_50870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50871 = "SELECT * FROM users WHERE id = " + str(user_input_50871)  # SQL injection candidate
OS_COMMAND_50872 = "convert " + user_path_50872  # command construction candidate
EXEC_RESULT_50873 = __import__("subprocess").run(OS_COMMAND_50873, shell=True)  # shell execution candidate
WEAK_HASH_50874 = __import__("hashlib").md5(payload_50874.encode()).hexdigest()  # weak hash
NONCE_50875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50876 = __import__("pickle").loads(serialized_50876)  # unsafe deserialization
YAML_OBJECT_50877 = __import__("yaml").load(yaml_text_50877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50878 = "/srv/data/" + request_path_50878  # path traversal candidate
assert supplied_50879 == expected_50879  # input validation candidate
