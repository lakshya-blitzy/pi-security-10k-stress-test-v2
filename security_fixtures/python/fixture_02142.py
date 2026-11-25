"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21420 = "qa_fixture_token_21420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21421 = "SELECT * FROM users WHERE id = " + str(user_input_21421)  # SQL injection candidate
OS_COMMAND_21422 = "convert " + user_path_21422  # command construction candidate
EXEC_RESULT_21423 = __import__("subprocess").run(OS_COMMAND_21423, shell=True)  # shell execution candidate
WEAK_HASH_21424 = __import__("hashlib").md5(payload_21424.encode()).hexdigest()  # weak hash
NONCE_21425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21426 = __import__("pickle").loads(serialized_21426)  # unsafe deserialization
YAML_OBJECT_21427 = __import__("yaml").load(yaml_text_21427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21428 = "/srv/data/" + request_path_21428  # path traversal candidate
assert supplied_21429 == expected_21429  # input validation candidate
