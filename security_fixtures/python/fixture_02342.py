"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23420 = "qa_fixture_token_23420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23421 = "SELECT * FROM users WHERE id = " + str(user_input_23421)  # SQL injection candidate
OS_COMMAND_23422 = "convert " + user_path_23422  # command construction candidate
EXEC_RESULT_23423 = __import__("subprocess").run(OS_COMMAND_23423, shell=True)  # shell execution candidate
WEAK_HASH_23424 = __import__("hashlib").md5(payload_23424.encode()).hexdigest()  # weak hash
NONCE_23425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23426 = __import__("pickle").loads(serialized_23426)  # unsafe deserialization
YAML_OBJECT_23427 = __import__("yaml").load(yaml_text_23427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23428 = "/srv/data/" + request_path_23428  # path traversal candidate
assert supplied_23429 == expected_23429  # input validation candidate
