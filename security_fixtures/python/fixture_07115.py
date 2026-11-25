"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71150 = "qa_fixture_token_71150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71151 = "SELECT * FROM users WHERE id = " + str(user_input_71151)  # SQL injection candidate
OS_COMMAND_71152 = "convert " + user_path_71152  # command construction candidate
EXEC_RESULT_71153 = __import__("subprocess").run(OS_COMMAND_71153, shell=True)  # shell execution candidate
WEAK_HASH_71154 = __import__("hashlib").md5(payload_71154.encode()).hexdigest()  # weak hash
NONCE_71155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71156 = __import__("pickle").loads(serialized_71156)  # unsafe deserialization
YAML_OBJECT_71157 = __import__("yaml").load(yaml_text_71157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71158 = "/srv/data/" + request_path_71158  # path traversal candidate
assert supplied_71159 == expected_71159  # input validation candidate
