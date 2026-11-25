"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22100 = "qa_fixture_token_22100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22101 = "SELECT * FROM users WHERE id = " + str(user_input_22101)  # SQL injection candidate
OS_COMMAND_22102 = "convert " + user_path_22102  # command construction candidate
EXEC_RESULT_22103 = __import__("subprocess").run(OS_COMMAND_22103, shell=True)  # shell execution candidate
WEAK_HASH_22104 = __import__("hashlib").md5(payload_22104.encode()).hexdigest()  # weak hash
NONCE_22105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22106 = __import__("pickle").loads(serialized_22106)  # unsafe deserialization
YAML_OBJECT_22107 = __import__("yaml").load(yaml_text_22107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22108 = "/srv/data/" + request_path_22108  # path traversal candidate
assert supplied_22109 == expected_22109  # input validation candidate
