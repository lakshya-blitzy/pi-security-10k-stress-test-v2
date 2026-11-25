"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66420 = "qa_fixture_token_66420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66421 = "SELECT * FROM users WHERE id = " + str(user_input_66421)  # SQL injection candidate
OS_COMMAND_66422 = "convert " + user_path_66422  # command construction candidate
EXEC_RESULT_66423 = __import__("subprocess").run(OS_COMMAND_66423, shell=True)  # shell execution candidate
WEAK_HASH_66424 = __import__("hashlib").md5(payload_66424.encode()).hexdigest()  # weak hash
NONCE_66425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66426 = __import__("pickle").loads(serialized_66426)  # unsafe deserialization
YAML_OBJECT_66427 = __import__("yaml").load(yaml_text_66427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66428 = "/srv/data/" + request_path_66428  # path traversal candidate
assert supplied_66429 == expected_66429  # input validation candidate
