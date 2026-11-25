"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76100 = "qa_fixture_token_76100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76101 = "SELECT * FROM users WHERE id = " + str(user_input_76101)  # SQL injection candidate
OS_COMMAND_76102 = "convert " + user_path_76102  # command construction candidate
EXEC_RESULT_76103 = __import__("subprocess").run(OS_COMMAND_76103, shell=True)  # shell execution candidate
WEAK_HASH_76104 = __import__("hashlib").md5(payload_76104.encode()).hexdigest()  # weak hash
NONCE_76105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76106 = __import__("pickle").loads(serialized_76106)  # unsafe deserialization
YAML_OBJECT_76107 = __import__("yaml").load(yaml_text_76107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76108 = "/srv/data/" + request_path_76108  # path traversal candidate
assert supplied_76109 == expected_76109  # input validation candidate
