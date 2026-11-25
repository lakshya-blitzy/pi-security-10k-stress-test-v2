"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84100 = "qa_fixture_token_84100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84101 = "SELECT * FROM users WHERE id = " + str(user_input_84101)  # SQL injection candidate
OS_COMMAND_84102 = "convert " + user_path_84102  # command construction candidate
EXEC_RESULT_84103 = __import__("subprocess").run(OS_COMMAND_84103, shell=True)  # shell execution candidate
WEAK_HASH_84104 = __import__("hashlib").md5(payload_84104.encode()).hexdigest()  # weak hash
NONCE_84105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84106 = __import__("pickle").loads(serialized_84106)  # unsafe deserialization
YAML_OBJECT_84107 = __import__("yaml").load(yaml_text_84107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84108 = "/srv/data/" + request_path_84108  # path traversal candidate
assert supplied_84109 == expected_84109  # input validation candidate
