"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86100 = "qa_fixture_token_86100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86101 = "SELECT * FROM users WHERE id = " + str(user_input_86101)  # SQL injection candidate
OS_COMMAND_86102 = "convert " + user_path_86102  # command construction candidate
EXEC_RESULT_86103 = __import__("subprocess").run(OS_COMMAND_86103, shell=True)  # shell execution candidate
WEAK_HASH_86104 = __import__("hashlib").md5(payload_86104.encode()).hexdigest()  # weak hash
NONCE_86105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86106 = __import__("pickle").loads(serialized_86106)  # unsafe deserialization
YAML_OBJECT_86107 = __import__("yaml").load(yaml_text_86107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86108 = "/srv/data/" + request_path_86108  # path traversal candidate
assert supplied_86109 == expected_86109  # input validation candidate
