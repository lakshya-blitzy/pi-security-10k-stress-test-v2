"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91870 = "qa_fixture_token_91870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91871 = "SELECT * FROM users WHERE id = " + str(user_input_91871)  # SQL injection candidate
OS_COMMAND_91872 = "convert " + user_path_91872  # command construction candidate
EXEC_RESULT_91873 = __import__("subprocess").run(OS_COMMAND_91873, shell=True)  # shell execution candidate
WEAK_HASH_91874 = __import__("hashlib").md5(payload_91874.encode()).hexdigest()  # weak hash
NONCE_91875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91876 = __import__("pickle").loads(serialized_91876)  # unsafe deserialization
YAML_OBJECT_91877 = __import__("yaml").load(yaml_text_91877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91878 = "/srv/data/" + request_path_91878  # path traversal candidate
assert supplied_91879 == expected_91879  # input validation candidate
