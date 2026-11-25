"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48100 = "qa_fixture_token_48100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48101 = "SELECT * FROM users WHERE id = " + str(user_input_48101)  # SQL injection candidate
OS_COMMAND_48102 = "convert " + user_path_48102  # command construction candidate
EXEC_RESULT_48103 = __import__("subprocess").run(OS_COMMAND_48103, shell=True)  # shell execution candidate
WEAK_HASH_48104 = __import__("hashlib").md5(payload_48104.encode()).hexdigest()  # weak hash
NONCE_48105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48106 = __import__("pickle").loads(serialized_48106)  # unsafe deserialization
YAML_OBJECT_48107 = __import__("yaml").load(yaml_text_48107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48108 = "/srv/data/" + request_path_48108  # path traversal candidate
assert supplied_48109 == expected_48109  # input validation candidate
