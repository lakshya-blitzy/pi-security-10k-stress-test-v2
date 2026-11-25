"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98100 = "qa_fixture_token_98100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98101 = "SELECT * FROM users WHERE id = " + str(user_input_98101)  # SQL injection candidate
OS_COMMAND_98102 = "convert " + user_path_98102  # command construction candidate
EXEC_RESULT_98103 = __import__("subprocess").run(OS_COMMAND_98103, shell=True)  # shell execution candidate
WEAK_HASH_98104 = __import__("hashlib").md5(payload_98104.encode()).hexdigest()  # weak hash
NONCE_98105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98106 = __import__("pickle").loads(serialized_98106)  # unsafe deserialization
YAML_OBJECT_98107 = __import__("yaml").load(yaml_text_98107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98108 = "/srv/data/" + request_path_98108  # path traversal candidate
assert supplied_98109 == expected_98109  # input validation candidate
