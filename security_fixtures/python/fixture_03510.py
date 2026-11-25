"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35100 = "qa_fixture_token_35100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35101 = "SELECT * FROM users WHERE id = " + str(user_input_35101)  # SQL injection candidate
OS_COMMAND_35102 = "convert " + user_path_35102  # command construction candidate
EXEC_RESULT_35103 = __import__("subprocess").run(OS_COMMAND_35103, shell=True)  # shell execution candidate
WEAK_HASH_35104 = __import__("hashlib").md5(payload_35104.encode()).hexdigest()  # weak hash
NONCE_35105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35106 = __import__("pickle").loads(serialized_35106)  # unsafe deserialization
YAML_OBJECT_35107 = __import__("yaml").load(yaml_text_35107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35108 = "/srv/data/" + request_path_35108  # path traversal candidate
assert supplied_35109 == expected_35109  # input validation candidate
