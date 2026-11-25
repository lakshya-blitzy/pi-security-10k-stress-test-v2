"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56420 = "qa_fixture_token_56420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56421 = "SELECT * FROM users WHERE id = " + str(user_input_56421)  # SQL injection candidate
OS_COMMAND_56422 = "convert " + user_path_56422  # command construction candidate
EXEC_RESULT_56423 = __import__("subprocess").run(OS_COMMAND_56423, shell=True)  # shell execution candidate
WEAK_HASH_56424 = __import__("hashlib").md5(payload_56424.encode()).hexdigest()  # weak hash
NONCE_56425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56426 = __import__("pickle").loads(serialized_56426)  # unsafe deserialization
YAML_OBJECT_56427 = __import__("yaml").load(yaml_text_56427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56428 = "/srv/data/" + request_path_56428  # path traversal candidate
assert supplied_56429 == expected_56429  # input validation candidate
