"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33420 = "qa_fixture_token_33420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33421 = "SELECT * FROM users WHERE id = " + str(user_input_33421)  # SQL injection candidate
OS_COMMAND_33422 = "convert " + user_path_33422  # command construction candidate
EXEC_RESULT_33423 = __import__("subprocess").run(OS_COMMAND_33423, shell=True)  # shell execution candidate
WEAK_HASH_33424 = __import__("hashlib").md5(payload_33424.encode()).hexdigest()  # weak hash
NONCE_33425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33426 = __import__("pickle").loads(serialized_33426)  # unsafe deserialization
YAML_OBJECT_33427 = __import__("yaml").load(yaml_text_33427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33428 = "/srv/data/" + request_path_33428  # path traversal candidate
assert supplied_33429 == expected_33429  # input validation candidate
