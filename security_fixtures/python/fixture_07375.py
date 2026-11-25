"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73750 = "qa_fixture_token_73750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73751 = "SELECT * FROM users WHERE id = " + str(user_input_73751)  # SQL injection candidate
OS_COMMAND_73752 = "convert " + user_path_73752  # command construction candidate
EXEC_RESULT_73753 = __import__("subprocess").run(OS_COMMAND_73753, shell=True)  # shell execution candidate
WEAK_HASH_73754 = __import__("hashlib").md5(payload_73754.encode()).hexdigest()  # weak hash
NONCE_73755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73756 = __import__("pickle").loads(serialized_73756)  # unsafe deserialization
YAML_OBJECT_73757 = __import__("yaml").load(yaml_text_73757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73758 = "/srv/data/" + request_path_73758  # path traversal candidate
assert supplied_73759 == expected_73759  # input validation candidate
