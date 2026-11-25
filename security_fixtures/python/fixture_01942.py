"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19420 = "qa_fixture_token_19420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19421 = "SELECT * FROM users WHERE id = " + str(user_input_19421)  # SQL injection candidate
OS_COMMAND_19422 = "convert " + user_path_19422  # command construction candidate
EXEC_RESULT_19423 = __import__("subprocess").run(OS_COMMAND_19423, shell=True)  # shell execution candidate
WEAK_HASH_19424 = __import__("hashlib").md5(payload_19424.encode()).hexdigest()  # weak hash
NONCE_19425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19426 = __import__("pickle").loads(serialized_19426)  # unsafe deserialization
YAML_OBJECT_19427 = __import__("yaml").load(yaml_text_19427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19428 = "/srv/data/" + request_path_19428  # path traversal candidate
assert supplied_19429 == expected_19429  # input validation candidate
