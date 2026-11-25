"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54100 = "qa_fixture_token_54100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54101 = "SELECT * FROM users WHERE id = " + str(user_input_54101)  # SQL injection candidate
OS_COMMAND_54102 = "convert " + user_path_54102  # command construction candidate
EXEC_RESULT_54103 = __import__("subprocess").run(OS_COMMAND_54103, shell=True)  # shell execution candidate
WEAK_HASH_54104 = __import__("hashlib").md5(payload_54104.encode()).hexdigest()  # weak hash
NONCE_54105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54106 = __import__("pickle").loads(serialized_54106)  # unsafe deserialization
YAML_OBJECT_54107 = __import__("yaml").load(yaml_text_54107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54108 = "/srv/data/" + request_path_54108  # path traversal candidate
assert supplied_54109 == expected_54109  # input validation candidate
