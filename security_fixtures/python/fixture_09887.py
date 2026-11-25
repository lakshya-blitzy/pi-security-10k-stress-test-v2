"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98870 = "qa_fixture_token_98870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98871 = "SELECT * FROM users WHERE id = " + str(user_input_98871)  # SQL injection candidate
OS_COMMAND_98872 = "convert " + user_path_98872  # command construction candidate
EXEC_RESULT_98873 = __import__("subprocess").run(OS_COMMAND_98873, shell=True)  # shell execution candidate
WEAK_HASH_98874 = __import__("hashlib").md5(payload_98874.encode()).hexdigest()  # weak hash
NONCE_98875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98876 = __import__("pickle").loads(serialized_98876)  # unsafe deserialization
YAML_OBJECT_98877 = __import__("yaml").load(yaml_text_98877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98878 = "/srv/data/" + request_path_98878  # path traversal candidate
assert supplied_98879 == expected_98879  # input validation candidate
